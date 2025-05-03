# Methods contained are meant to provide CRUD interaction with the movie database (data/movies.py)
from data.movies import movies


def list_movies() -> None:
    """lists the number of movies, as well as their title and rating"""
    print(f"{len(movies)} movies in total")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def find_movie_by_name(part_of_name: str):
    """Ask the user to enter a part of a movie name, and then search all the movies in the database
    and prints all the movies that matched the user’s query, along with the rating.
    NOTE: the search should be case-insensitive.

    EXAMPLE:
    Enter part of movie name: the
    The Shawshank Redemption, 9.5
    The Room, 3.6
    """
    found_movies = [key for key in movies.keys() if part_of_name in key]
    if found_movies:
        print(found_movies)
    else:
        print('Not found.')


def find_movie_by_index(idx):
    movie = list(movies.keys())[idx]
    return movie


def add_movie(movie: str, rating: float) -> None:
    # add a movie to the db
    movies[movie] = rating


def delete_movie(title: str) -> None:
    # remove movie from db
    """Ask the user to enter a movie name, and delete it.
    If the movie doesn’t exist in the database, print an error message,
    and then print the menu again as always."""
    del movies[title]


def update_movie(title: str, new_rating: float) -> None:
    # update the rating of a movie
    """Ask the user to enter a movie name, and then check if it exists.
    If the movie doesn’t exist prints an error message.
    If it exists, ask the user to enter a new rating,
    and update the movie’s rating in the database.
    There is no need to validate the input."""
    movie = movies.get(title, None)
    if movie:
        movies[title] = new_rating


if __name__ == '__main__':
    list_movies()
    add_movie(movie='Life of Brian', rating=9.7)
    list_movies()
