import sqlite3
from movie.movie_library import MovieLibrary
from movie.movie import Movie


class User:
    def __init__(self, username, liked_movies=None):
        self._id = None
        self._username = username
        self._liked_movies = liked_movies if liked_movies else []

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    def like_movie(self, movie):
        """Like a movie."""
        if movie.id not in self._liked_movies:
            self._liked_movies.append(movie.id)

    def unlike_movie(self, movie):
        """Unlike a movie."""
        if movie.id in self._liked_movies:
            self._liked_movies.remove(movie.id)

    def get_liked_movies(self, movie_library):
        """Get the list of movies liked by the user."""
        liked_movies = []
        for movie_id in self._liked_movies:
            movie = next((m for m in movie_library.get_movies() if m.id == movie_id), None)
            if movie:
                liked_movies.append(movie)
        return liked_movies


class Users:
    def __init__(self, db_filename="users.db", id=[0], username="", liked_movies=[0]):
        self._id = id
        self._username = username
        self._liked_movies = liked_movies
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                liked_movies INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_user(self, user):
        self.cursor.execute('''
            INSERT INTO users (username, liked) VALUES (?, ?)
        ''', (user.username, ','.join(map(str, user.get_liked_movies()))))
        self.connection.commit()

    def update_user(self, user):
        self.cursor.execute('''
            UPDATE users SET username=?, liked=? WHERE id=?
        ''', (user.username, ','.join(map(str, user.get_liked_movies())), user.id))
        self.connection.commit()

    def get_user_by_id(self, user_id):
        self.cursor.execute('''
            SELECT * FROM users WHERE id=?
        ''', (user_id,))
        user_data = self.cursor.fetchone()
        if user_data:
            return self._create_user_object(user_data)
        return None

    def get_user_by_username(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username=?
        ''', (username,))
        user_data = self.cursor.fetchone()
        if user_data:
            return self._create_user_object(user_data)
        return None

    def __str__(self, id, username, liked_movies=[]):
        return f"User id= {self._id}, username= {self._username}, liked_movies= {self._liked_movies}"

    # Add other methods for retrieving user data based on different criteria

    def _create_user_object(self, user_data):
        user = User(user_data[1], list(map(int, user_data[2].split(','))))
        user._id = user_data[0]
        return user

    def close_connection(self):
        self.connection.close()
