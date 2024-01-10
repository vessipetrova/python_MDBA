import argparse
import sqlite3
import pycounter

from movie.movie_library import MovieLibrary
from movie.user import User
from sqlite3_db.create_db import movies

def main():
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
    parser_movcat.add_argument("--category",type=str, choices=["liked", "newest", "genre"], help="Available category")

    # Parse command-line arguments
    args = parser.parse_args()

    # Execute the corresponding function based on each command
    if args.command == "movlst":
        movlst_command(args)
    elif args.command == "movdt":
        movdt_command(args.movie_id)
    elif args.command == "movsrch":
        movsrch_command(args.sql_query)
    elif args.command == "movadd":
        movadd_command(args.title)
    elif args.command == "movrmv":
        movrmv_command(args.movie_id)
    elif args.command == "movfv":
        movfv_command(args.movie_id)
    elif args.command == "movcat":
        movcat_command(args.category)
    else:
        print("Error. Command not found.")

if __name__ == '__main__':
    main()

def movlst_command(args):
    print("Structured Representation of Movies:")
    for movie in movies:
        print(
            f"Movie_id: {args.movie_id}, Title: {args.title}, \
            Release_date: {args.release_date}, Director: {args.director}, Genre: {args.genre}, user_likes: {args.user_likes}")

def movdt_command(args):
    movie = next((m for m in movie_library.get_movies() if movie_id == args.movie_id), None)
    if movie:
        print(f"Details of Movie: {args.movie_id}")
        print(f"Title: {args.title}")
        print(f"release_date: {args.release_date}")
        print(f"Director: {args.director}")
        print(f"Genre: {args.genre}")
        print(f"User_likes: {args.user_likes}")
    else:
        print(f"Movie with ID: {args.movie_id} not found.")

def movsrch_command(movie_library, query):
    search_results = movie_library.search_movie(query)
    if search_results:
        print(f"Search Results for '{query}':")
        movie_library.search_movie = search_results [0]
        return search_results
    else:
        print(f"No movies found for '{query}'.")

#def __getattr__(movies):
 #   return movie_library.get_movies()

def movadd_command(args):
#    new_movie = MovieLibrary.add_new_movie
    print(f"title={args.title}, movie_id={args.movie_id}, release_date={args.release_date}, director={args.director}, genre={args.genre}, user_likes={args.user_likes}")
    print("Movie added successfully.")

def movrmv_command(args):
    movie = next((m for m in movie_library.get_movies() if m.id == movie_id), None)
    if movie:
        movie_library.remove_movie(movie)
        print(f"Movie {args.movie_id} removed successfully.")
    else:
        print(f"Movie with ID {args.movie_id} not found.")

def movfv_command(args):
    user = User.User("ExampleUser")
    movie = next((m for m in movie_library.get_movies() if m.id == movie_id), None)
    if movie:
        user_likes = movie_library.get_movies()
        user_likes = args.user_likes
#        assert true user.like_movie(movie)
#        print(f"Movie {movie_id} marked as a favorite for User {user.id}.")
        print(f"Movie {args.movie_id} marked as 'liked' {args.user_likes}.")
    else:
        print(f"Movie with ID {args.movie_id} not found.")
#def list_top_movies(movie_library, category):
def movcat_command(movie_library, category, top_movies):
    if category == "liked":
        top_movies = movie_library.get_top_movies("liked")
        print("Top 5 Liked Movies:")
        list_top_movies = top_movies[0]
     elif category == "newest":
        top_movies = movie_library.get_top_movies("newest")
        print("Top 5 Newest Movies:")
        list_top_movies = top_movies[0]
    elif category == "genre":
        genre = input("Enter the genre: ")
        top_movies = movie_library.get_top_movies("genre", genre)
        print(f"Top 5 Movies in Genre '{genre}':")
        list_top_movies = top_movies[0]
    else:
        print(f"Error. Category '{category}' not found.")
        allowed_categories = ["liked", "newest", "genre"]
        if args.category not in allowed_categories:
            print(f"Error. Category '{args.category}' not found.")
        else:
            movcat_command(args.category)
            print(f"Top 5 Movies in Genre '{args.category}':")
            list_top_movies = top_movies[0]
