import sqlite3

# connect to SQLite database (or create it if not exists)
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()
# Create a table named 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        liked_movies INTEGER NOT NULL
        )
''')
conn.commit()
conn.close()


conn = sqlite3.connect('users.db')
cursor = conn.cursor()
# Insert sample data into the table

users = [
    (1, "Victor", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (2, "Vanesa", "16,17,18,19,20,21,22,23,24,25,26,27"),
    (3, "Ivan", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (4, "Georgi", "16,17,18,19,20,21,22,23,24,25,26,27"),
    (5, "Alexander", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (6, "Antonia", "16,17,18,19,20,21,22,23,24,25,26,27"),
    (7, "Martin", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (8, "Elica", "16,17,18,19,20,21,22,23,24,25,26,27"),
    (9, "Isabela", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (10, "Kalina", "16,17,18,19,20,21,22,23,24,25,26,27"),
    (11, "Mariyan", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (12, "Daniel", "16,17,18,19,20,21,22,23,24,25,26,27"),
    (13, "Dimitar", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
    (14, "Christian", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"),
]

for user in users:
    cursor.execute('''
        INSERT or REPLACE INTO users (id, username, liked_movies)
        VALUES (?, ?, ?)   
    ''', user)

conn.commit()
conn.close()
# Path: movie/user.py
