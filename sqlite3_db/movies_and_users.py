import sqlite3

# connect to SQLite database (or create it if not exists)
conn = sqlite3.connect('movies_and_users.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()
# Create a table named 'movies and users' if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS 'movies and users' (
        movie_id INTEGER,
        user_id INTEGER,        
        PRIMARY KEY (movie_id, user_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (user_id) REFERENCES users(id)        
        )
''')
conn.commit()
conn.close()

# Path: sqlite3_db/movies_and_users.py

conn = sqlite3.connect('movies_and_users.db')
cursor = conn.cursor()

# Insert data into 'movies and users' table
cursor.execute('''
    INSERT or REPLACE INTO 'movies and users' (movie_id, user_id)
    VALUES (1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 2), (3, 3)
''')
conn.commit()
conn.close()
