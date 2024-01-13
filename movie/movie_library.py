import sqlite3
from movie.movie import Movie

class MovieLibrary:
    def __init__(self, db_name="movie_library.db", table_exists="movies", counter=0):
        self._conn = sqlite3.connect(db_name)
        self._cursor = self._conn.cursor()
        self.db_name = db_name
        self._movies = []
        self._counter = counter
        self._table_exists = table_exists

        self._cursor.execute("SELECT db_name FROM sqlite3_master WHERE type='table' AND name='movies'")
        if table_exists == "movies":
            self._cursor.execute("SELECT * FROM movies")
            self._movies = [Movie(*row) for row in self._cursor.fetchall()]

        else:
            self._cursor.execute("CREATE TABLE 'movies'")
            self._cursor.execute("SELECT * FROM movies")
            self._movies = []

        self._conn.commit()
        self._conn.close()

    def _create_table(self):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()

        """Create the movies table if it doesn't exist."""
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS 'movies' (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,        
                director TEXT NOT NULL,
                release_date INTEGER NOT NULL,
                genre TEXT,
                user_likes INTEGER DEFAULT 0, CONSTRAINT valid_user_likes CHECK (user_likes >= 0)
            )
        ''')
        self._conn.commit()
        self._conn.close()

    def movadd_command(self, movie):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Add a movie to the library."""
        self._cursor.execute('''
            INSERT INTO movies (movie_id, name, release_date, director, genre, user_likes) VALUES (?, ?, ?, ?, ?, ?)
        ''', (movie.movie_id, movie.name, movie.release_date, movie.director, movie.genre, movie.user_likes))
        self._conn.commit()
        self._conn.close()
        print("Success!Movie added to library!")

    def movrmv_command(self, movie_id):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Remove a movie from the library by movie_id."""
        self._cursor.execute('DELETE FROM movies WHERE id=?', (movie_id,))
        self._conn.commit()
        self._conn.close()
        print("Success!Movie removed from library!")

    def fetchall(self):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Get all movies in the library."""
        self._cursor.execute('SELECT * FROM movies')
        return [Movie(*row) for row in self._cursor.fetchall()]
        self._conn.commit()
        self._conn.close()

    def movlst_command(self):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Get the list of movies in the library."""
        self._cursor.execute('SELECT * FROM movies')
        return [Movie(*row) for row in self._cursor.fetchall()]

        self._conn.close()

    def movdt_command(self, movie_id):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Get a movie by its ID."""
        self._cursor.execute('SELECT * FROM movies WHERE movie_id=?', (movie_id,))
        movie_data = self._cursor.fetchone()
        if movie_data:
            return Movie(*movie_data)
        return None
        self._conn.commit()
        self._conn.close()

    def movsrch_command(self, name):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Search for a movie by title."""
        self._cursor.execute('SELECT * FROM movies WHERE name=?', (name,))
        return [Movie(*row) for row in self._cursor.fetchall()]
        self._conn.commit()
        self._conn.close()

#    def movsrch_command(self, director):
#        self._conn = sqlite3.connect(self.db_name)
#        self._cursor = self._conn.cursor()
#        """Search for a movie by director."""
#        self._cursor.execute('SELECT * FROM movies WHERE director=?', (director,))
#        return [Movie(*row) for row in self._cursor.fetchall()]
#        self._conn.commit()
#        self._conn.close()

    def clear_library(self):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Clear all movies from the library."""
        self._cursor.execute('DELETE FROM movies')
        self._conn.commit()
        self._conn.close()
        print("Success!Library cleared!")


    def movfv_command(self, movie_id):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Mark a movie as liked."""
        self._cursor.execute('UPDATE movies SET user_likes=user_likes+1 WHERE movie_id=?', (movie_id,))
        self._conn.commit()
        self._conn.close()
        print("Success!Movie marked as liked!")


    def get_top_movies(self, category, genre=None):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Get the top 5 movies in the specified category."""
        if category == "liked":
            self._cursor.execute('SELECT * FROM movies ORDER BY user_likes DESC LIMIT 5')
        elif category == "newest":
            self._cursor.execute('SELECT * FROM movies ORDER BY release_date DESC LIMIT 5')
        elif category == "genre":
            self._cursor.execute('SELECT * FROM movies WHERE genre=? ORDER BY user_likes DESC LIMIT 5', (genre,))
        return [Movie(*row) for row in self._cursor.fetchall()]
        self._conn.commit()


    def movcat_command(self, category, genre=None):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Get the top 5 movies in the specified category."""
        if category == "liked":
            self._cursor.execute('SELECT * FROM movies ORDER BY user_likes DESC LIMIT 5')
        elif category == "newest":
            self._cursor.execute('SELECT * FROM movies ORDER BY release_date DESC LIMIT 5')
        elif category == "genre":
            self._cursor.execute('SELECT * FROM movies WHERE genre=? ORDER BY user_likes DESC LIMIT 5', (genre,))
        return [Movie(*row) for row in self._cursor.fetchall()]
        self._conn.commit()
        self._conn.close()


    def get_movie_by_id(self, movie_id):
        self._conn = sqlite3.connect(self.db_name)
        self._cursor = self._conn.cursor()
        """Get a movie by its ID."""
        self._cursor.execute('SELECT * FROM movies WHERE movie_id=?', (movie_id,))
        movie_data = self._cursor.fetchone()
        if movie_data:
            return Movie(*movie_data)
        return None

    #       if movie_data:
    #           return {
    #           'movie_ID': movie_id[0],
    #           'title': title[1],
    #           'director': director[2],
    #           'release_year': release_year[3],
    #           'genre': genre[4],
    #           'rating': user_likes[5]
    #       }
    #       else:
    #           return None

    def get_movie_by_title(self, name):
        """Get a movie by its title."""
        self._cursor.execute('SELECT * FROM movies WHERE name=?', (name,))
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
            UPDATE movies SET name=?, release_date=?, director=?, genre=?, user_likes=? WHERE movie_id=?
        ''', (movie.name, movie.date, movie.director, movie.genre, movie.user_likes, movie.movie_id))
        self._conn.commit()

    def __str__(self):
        return f"MovieLibrary({self._movies})"

    def __del__(self):
        """Close the database connection."""
        if self._conn:
            self._conn.close()
            print("Connection closed!")
        else:
            print("Error.No connection to close!")
