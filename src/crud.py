# Methods contained are meant to provide CRUD interaction with the movie database (data/movies.py)
from data.movies import movies

def list_movies() -> None:
    """lists the number of movies, as well as their title and rating"""
    print(f"{len(movies)} movies in total")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie(movie: str, rating: float) -> None:
    # add a movie to the db
    """Ask the user to enter a movie name and a rating.
    There is no need to validate the input (assume that the rating is a number between 1-10)."""
    movies[movie] = rating


def delete_movie(title: str) -> None:
    # remove movie from db
    """Ask the user to enter a movie name, and delete it.
    If the movie doesn’t exist in the database, print an error message,
    and then print the menu again as always."""
    pass


def update_movie():
    # update the rating of a movie
    """Ask the user to enter a movie name, and then check if it exists.
    If the movie doesn’t exist prints an error message.
    If it exist, ask the user to enter a new rating,
    and update the movie’s rating in the database.
    There is no need to validate the input."""
    pass


def print_random_movie():
    """Print a random movie and it’s rating."""
    pass


def find_movie_by_name(name: str):
    """Ask the user to enter a part of a movie name, and then search all the movies in the database
    and prints all the movies that matched the user’s query, along with the rating.
    NOTE: the search should be case-insensitive.
    If I search the and the name if the movie is The Shawshank Redemption, I should find the movie.

    For example:
    Enter part of movie name: the
    The Shawshank Redemption, 9.5
    The Room, 3.6
    """
    print(name)


if __name__ == '__main__':
    list_movies()
    # add_movie()
    # delete_movie()
    # update_movie()
