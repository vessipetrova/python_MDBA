import sqlite3

# connect to SQLite database (or create it if not exists)
conn = sqlite3.connect('movie_library.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()
# Create a table named 'movies'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS 'movies' (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        director TEXT NOT NULL,
        release_date INTEGER NOT NULL,
        genre TEXT,
        user_likes INTEGER DEFAULT 0, CONSTRAINT valid_user_likes CHECK (user_likes >= 0)              
        )
''')
conn.commit()
conn.close()

conn = sqlite3.connect('movie_library.db')
cursor = conn.cursor()
# Insert sample data into the table
movies = [
    (1, "Star Wars: Return of the Jedi Ep.6", "Richard Marquand", 1983, "Sci-Fi,Adventure,Action", 11300),
    (2, "Star Wars: The Rise of Skywalker Ep.9", "Daisy Ridley, John Boyega", 2019, "Action,Adventure,Sci-Fi", 11180),
    (3, "Star Wars: The Last Jedi Ep.8", "Rian Johnson", 2017, "Action,Adventure,Sci-Fi", 12307),
    (4, "Jupiter Ascending", "The Washowskies", 2015, "Action,Adventure,Sci-Fi", 1132),
    (5, "The Matrix", "The Washowskies", 1999, "Action,Adventure,Sci-Fi", 3481),
    (6, "The Matrix: Revolutions", "The Wachowskies", 2003, "Action,Adventure,Sci-Fi", 2237),
    (7, "The Matrix: Resurrections", "The Wachowskies", 2021, "Action,Adventure,Sci-Fi", 16735),
    (8, "In Time", "Andrew Niccol", 2011, "Action,Thriller,Sci-Fi", 614),
    (9, "Valerian and The City of Thousand Planets", "Luc Besson", 2017, "Action,Fantasy,Sci-Fi", 1614),
    (10, "Heat", "Michael Mann", 1995, "Action,Crime,Drama", 980),
    (11, "Avatar", "James Cameron", 2009, "Action,Adventure,Fantasy,Sci-Fi", 8000),
    (12, "Avatar: The Way of The Water", "James Cameron", 2022, "Action,Adventure,Fantasy,Sci-Fi", 20830),
    (13, "Inception", "Christopher Nolan", 2010, "Action,Adventure,Sci-Fi", 6580),
    (14, "Tenet", "Christopher Nolan", 2020, "Action,Sci-Fi,Thriller", 1780),
    (15, "The Lord of The Rings:Fellowship of The Ring", "Peter Jackson", 2001, "Adventure,Fantasy,Drama", 1980),
    (16, "The Lord of The Rings:The Return of The King", "Peter Jackson", 2003, "Adventure,Fantasy,Drama", 2580),
    (17, "Interstellar", "Christopher Nolan", 2014, "Adventure,Drama,Sci-Fi", 2300),
    (18, "The Dark Knight", "Christopher Nolan", 2008, "Action,Crime,Drama,Thriller", 1300),
    (19, "Ender's Game", "Gavin Hood", 2013, "Action,Adventure,Sci-Fi", 590),
    (20, "Passengers", "Morten Tyldum", 2016, "Drama,Romance,Sci-Fi,Thriller", 639),
    (21, "The 5th Element", "Luc Besson", 1997, "Action,Adventure,Sci-Fi", 1000),
    (22, "Men In Black", "Barry Sonnenfield", 1997, "Action,Adventure,Sci-Fi,Comedy", 3000),
    (23, "Doctor Strange", "Scott Derrickson", 1995, "Action,Adventure,Fantasy,Sci-Fi", 1850),
    (24, "Star Gate", "Roland Emmerich", 1994, "Action,Fantasy,Horror,Mystery", 2700),
    (25, "Constantine", "Francis Lawrence", 2005, "Action,Crime,Drama", 1666),
    (26, "Man of Steel", "Zack Snyder", 2013, "Action,Adventure,Sci-Fi", 2288),
    (27, "Riders of The Lost Ark", "Steven Spielberg", 1981, "Action,Adventure,Sci-Fi", 2011),
]
for movie in movies:
    cursor.execute('''
        INSERT or REPLACE INTO movies (movie_id, name, director, release_date, genre, user_likes)
        VALUES (?, ?, ?, ?, ?, ?)   
    ''', movie)

conn.commit()
conn.close()
