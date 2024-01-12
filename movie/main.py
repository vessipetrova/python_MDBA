import argparse

import movie_library as MovieLibrary
from movie.user import User
from sqlite3_db.create_db import movies


def main():
    movie_library = MovieLibrary.MovieLibrary("movies.db")
    # set up parser to handle command-line arguments
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: movlst
    subparsers.add_parser("movlst", help="Get a structured representation of all movies")

    # Command: movdt
    parser_movdt = subparsers.add_parser("movdt", help="Get the details of a movie by its id")
    parser_movdt.add_argument("--movie_id", type=int, help="Movie ID")

    # Command: movsrch
    parser_movsrch = subparsers.add_parser("movsrch", help="Search for a movie by title")
    parser_movsrch.add_argument("--query", type=str, help="Search query")

    # Command: movadd
    parser_movadd = subparsers.add_parser("movadd", help="Add a movie")
    parser_movadd.add_argument("--title", required=True, type=str, help="Movie title")
    parser_movadd.add_argument("--release_date", type=int, help="Release date")
    parser_movadd.add_argument("--director", required=True, type=str, help="Director")
    parser_movadd.add_argument("--genre", type=str, help="Genre")
    parser_movadd.add_argument("--user_likes", type=int, help="User likes")

    # Command: movrmv
    parser_movrmv = subparsers.add_parser("movrmv", help="Remove a movie")
    parser_movrmv.add_argument("--movie_id", type=int, help="Movie id")

    # Command: movfv
    parser_movfv = subparsers.add_parser("movfv", help="Mark a movie as liked/favoritized")
    parser_movfv.add_argument("--movie_id", type=int, help="Movie id")

    # Command: movcat
    parser_movcat = subparsers.add_parser("movcat", help="List top 5 movies from the specified category")
    parser_movcat.add_argument("--category", type=str, choices=["liked", "newest", "genre"], help="Available category")

    # Parse command-line arguments
    args = parser.parse_args()

    # Execute the corresponding function based on each command
    if args.command == "movlst":
        movlst_command(movie_library)
    elif args.command == "movdt":
        movdt_command(args.movie_id, movie_library)
    elif args.command == "movsrch":
        movsrch_command(movie_library, args.query)
    elif args.command == "movadd":
        movadd_command(movie_library, args)
    elif args.command == "movrmv":
        movrmv_command(movie_library, args.movie_id)
    elif args.command == "movfv":
        movfv_command(movie_library, args.movie_id)
    elif args.command == "movcat":
        movcat_command(movie_library, args.category)
    else:
        print("Invalid command.")


if __name__ == '__main__':
    main()


def movlst_command(movie_library):
    print("Structured Representation of Movies:")
    for args in movies:
        print(
            f"Movie_id: {args.movie_id}, Title: {args.title}, \
            Release_date: {args.release_date}, Director: {args.director}, Genre: {args.genre}, user_likes: {args.user_likes}")


def movdt_command(movie_id, movie_library):
    movie = next((m for m in movie_library.get_movies() if movie_id == movie_id), None)
    if movie:
        print(f"Details of Movie: {movie.movie_id}")
        print(f"Title: {movie.title}")
        print(f"release_date: {movie.release_date}")
        print(f"Director: {movie.director}")
        print(f"Genre: {movie.genre}")
        print(f"User_likes: {movie.user_likes}")
    else:
        print(f"Movie with ID: {movie.movie_id} not found.")


def movsrch_command(movie_library, query):
    search_results = movie_library.search_movie(query)
    if search_results:
        print(f"Search Results for '{query}':")
        movie_library.search_movie = search_results[0]
        return search_results
    else:
        print(f"No movies found for '{query}'.")


# def __getattr__(movies):
#   return movie_library.get_movies()

def movadd_command(movie_library, args):
    print(
        f"title={args.title}, movie_id={args.movie_id}, release_date={args.release_date}, director={args.director}, genre={args.genre}, user_likes={args.user_likes}")
    print("Movie added successfully.")
    movie_library.add_movie(args.title, args.movie_id, args.release_date, args.director, args.genre, args.user_likes)


def movrmv_command(movie_library, movie_id):
    movie = next((m for m in movie_library.get_movies() if m.id == movie_id), None)
    if movie:
        movie_library.remove_movie(movie_id)
        print(f"Movie {movie_id} removed successfully.")
    else:
        print(f"Movie with ID {movie_id} not found.")


def movfv_command(movie_library, movie_id):
    user = User("ExampleUser")
    movie = next((m for m in movie_library.get_movies() if m.id == movie_id), None)
    if movie:
        user.like_movie(movie)
        print(f"Movie {movie_id} marked as a favorite for User {user.id}.")
    else:
        print(f"Movie with ID {movie_id} not found.")

# def list_top_movies(movie_library, category):
def movcat_command(movie_library, category):
    if category == "liked":
        print("Top 5 movies by likes:")
        movie_library.get_top_movies(category)
    elif category == "newest":
        print("Top 5 newest movies:")
        movie_library.get_top_movies(category)
    elif category == "genre":
        print("Top 5 movies by genre:")
        movie_library.get_top_movies(category)
    else:
        print(f"Category {category} not found.")

# def movcat_command(movie_library, category):
#   available categories = ["liked", "newest", "genre"]
#      if category != "liked" or category != "newest" or category != "genre":
#         print(f"Error.Category {category} not found.")
#      else:
#         print("Top 5 movies by likes:")
#         movie_library.get_top_movies(category)
#         print("Top 5 newest movies:")
#         movie_library.get_top_movies(category)
#         print("Top 5 movies by genre:")
#         movie_library.get_top_movies(category)
