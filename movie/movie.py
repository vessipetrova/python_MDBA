import sqlite3
from sqlite3_db.create_db import movies

class Movie:
    def __init__(self, movie_id=0, name="", release_date=0, director="", genre="", user_likes=0):
        self._movie_id = movie_id
        self._name = name
        self._release_date = release_date
        self._director = director
        self._genre = genre
        self._user_likes = user_likes

    """ Setters and Getters for all the properties we defined above """
    @property
    def movie_id(self):
        return self._movie_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def user_likes(self):
        return self._user_likes

    def add_user_like(self, user_id):
        """Add a user ID to the user_likes array."""
        if user_id not in self._user_likes:
            self._user_likes.append(user_id)

    def remove_user_likes(self, user_id):
        if user_id in self.user_likes:
            self.user_likes.remove(user_id)

    """ End Setters and Getters """

    def __str__(self, movie_id=0, name="", release_date=0, director="", genre="", user_likes=0):
        return f"{self.movie_id}, {self.name}, {self.release_date}, {self.director}, {self.genre}, {self.user_likes}"

    def args_tuple(self):
        """Convert Movie object for SQL storage"""
        return self.movie_id, self._name, self._release_date, self._director, self._genre, self._user_likes


def movlst_command():
    """Get all movies from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_id(movie_id):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE movie_id=?", (movie_id,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_name(name):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE name=?", (name,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_release_date(release_date):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE release_date=?", (release_date,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_director(director):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE director=?", (director,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_genre(genre):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE genre=?", (genre,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_user_likes(user_likes):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE user_likes=?", (user_likes,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_category(category):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE category=?", (category,))
    rows = c.fetchall()
    conn.close()
    return rows


def get_movie_by_query(query):
    """Get a movie from the database"""
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE query=?", (query,))
    rows = c.fetchall()
    conn.close()
    return rows

