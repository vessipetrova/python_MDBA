from movie.movie import Movie
import sqlite3
import json

class MovieLibrary:
    def __init__(self, db_name="movie_library.db", table_exists="movies", counter=0):
        self._conn = sqlite3.connect(db_name)
        self._cursor = self._conn.cursor()

        self._cursor.execute("SELECT db_name FROM sqlite3_master WHERE type='table' AND name='movies'")
        if table_exists == "movies":
            self._cursor.execute("SELECT * FROM movies")
            self._movies = [Movie(*row) for row in self._cursor.fetchall()]

        else:
            self._cursor._create_table()
            self._movies = []
            self._counter = counter
            self._conn.commit()

    def _create_table(self):
        """Create the movies table if it doesn't exist."""
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS 'movies' (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,        
                director TEXT NOT NULL,
                release_date INTEGER NOT NULL,
                genre TEXT,
                user_likes INTEGER CHECK (user_likes >= 0) COUNTER DEFAULT 0,
            )
        ''')
        self._conn.commit()

    def add_movie(self, movie):
        """Add a movie to the library."""
        self._cursor.execute('''
            INSERT INTO movies (title, release_date, director, genre, user_likes) VALUES (?, ?, ?, ?, ?)
        ''', (movie.title, movie.release_date, movie.director, movie.genre, movie.user_likes))
        self._conn.commit()

    def remove_movie(self, movie_id):
        """Remove a movie from the library by movie_id."""
        self._cursor.execute('DELETE FROM movies WHERE id=?', (movie_id,))
        self._conn.commit()

    def get_movies(self):
        """Get the list of movies in the library."""
        self._cursor.execute('SELECT * FROM movies')
        return [Movie(*row) for row in self._cursor.fetchall()]

    def search_movie(self, title):
        """Search for a movie by title."""
        self._cursor.execute('SELECT * FROM movies WHERE title=?', (title,))
        return [Movie(*row) for row in self._cursor.fetchall()]

    def clear_library(self):
        """Clear all movies from the library."""
        self._cursor.execute('DELETE FROM movies')
        self._conn.commit()

    def get_top_movies(self, category, genre=None):
        """Get the top 5 movies in the specified category."""
        if category == "liked":
            self._cursor.execute('SELECT * FROM movies ORDER BY user_likes DESC LIMIT 5')
        elif category == "newest":
            self._cursor.execute('SELECT * FROM movies ORDER BY release_date DESC LIMIT 5')
        elif category == "genre":
            self._cursor.execute('SELECT * FROM movies WHERE genre=? ORDER BY user_likes DESC LIMIT 5', (genre,))
        return [Movie(*row) for row in self._cursor.fetchall()]

    def get_movie_by_id(self, movie_id):
        """Get a movie by its ID."""
        self._cursor.execute('SELECT * FROM movies WHERE movie_id=?', (movie_id,))
        movie_data = self._cursor.fetchone()
        if movie_data:
            return Movie(*movie_data)
        return None

    def get_movie_by_title(self, title):
        """Get a movie by its title."""
        self._cursor.execute('SELECT * FROM movies WHERE title=?', (title,))
        movie_data = self._cursor.fetchone()
        if movie_data:
            return Movie(*movie_data)
        return None

    def get_movie_by_director(self, director):
        """Get a movie by its director."""
        self._cursor.execute('SELECT * FROM movies WHERE director=?', (director,))
        movie_data = self._cursor.fetchone()
        if movie_data:
            return Movie(*movie_data)
        return None

    def get_movie_by_genre(self, genre):
        """Get a movie by its genre."""
        self._cursor.execute('SELECT * FROM movies WHERE genre=?', (genre,))
        movie_data = self._cursor.fetchone()
        if movie_data:
            return Movie(*movie_data)
        return None

    def mark_movie_as_liked(self, movie_id):
        """Mark a movie as liked."""
        self._cursor.execute('UPDATE movies SET user_likes=user_likes+1 WHERE movie_id=?', (movie_id,))
        self._conn.commit()

    def mark_movie_as_unliked(self, movie_id):
        """Mark a movie as unliked."""
        self._cursor.execute('UPDATE movies SET user_likes=user_likes-1 WHERE movie_id=?', (movie_id,))
        self._conn.commit()

    def update_movie(self, movie):
        """Update a movie in the library."""
        self._cursor.execute('''
            UPDATE movies SET title=?, release_date=?, director=?, genre=?, user_likes=? WHERE movie_id=?
        ''', (movie.title, movie.date, movie.director, movie.genre, movie.user_likes, movie.movie_id))
        self._conn.commit()

    def __str__(self):
        return f"MovieLibrary({self._movies})"

    def __del__(self):
        """Close the database connection."""
        self._conn.close()
