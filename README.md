### This is the documentation for my CLI project: 
## Description
This is a project for a CLI (Command Line Interface) Application that allows you to search for a movie in a database and get information about it. Users can also add and remove movies and mark them as liked or favourized. The application will also recommend movies based on the user's preferences or by number of likes, genre or the top 5 newest movies.

## Installation
Before you start this CLI App you need to run this script once in order to populate the database with the movies and generate the test data:
'''create_db.py'''

## Commands
* command 1: **movlst** - This command will list all the movies in the database. It will also show the user's liked and favourized movies.
* command 2: **movdt** - This command will show the full details of a particular movie chosen by the user /movie id#, title, director, genre, release date, likes, etc./
* command 3: **movsrch** - This command will allow the user to search for a movie.
* command 4: **movadd** - This command will allow the user to add a movie to the database.
* command 5: **movrmv** - This command will allow the user to remove a movie from the database.
* command 6: **movfv** - This command will allow the user to like a movie or mark it as favourized.
* command 7: **movcat** - This command will allow the user to search for movies by category: 'genre', 'liked' or 'newest'.

## Usage

To start the application run the following script:
'''main.py/run'''

## Contributing

Bug reports and pull requests are very welcome on GitHub at:
www.github.com/vessi_petrova/python_MDBA
