import sqlite3

class Movie:
    def __init__(self, movie_id=0, title="", release_date=0, director="", genre="", user_likes=0):
        self._movie_id = movie_id
        self._title = title
        self._release_date = release_date
        self._director = director
        self._genre = genre
        self._user_likes = user_likes

    """ Setters and Getters for all the properties we defined above """
    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

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

    def __str__(self):
        return f"{self.title} ({self.movie_id})"

    def to_tuple(self):
        """Convert Movie object for SQL storage"""
        return self.movie_id, self._title, self._release_date, self._director, self._genre, self._user_likes

