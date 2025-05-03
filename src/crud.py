# Methods contained are meant to provide CRUD interaction with the movie database (data/movies.py)
from data.movies import movies


def list_movies() -> None:
    """lists the number of movies, as well as their title and rating"""
    print(f"{len(movies)} movies in total")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def find_movie_by_full_title(title: str) -> tuple[str, str]:
    return title, movies.get(title, '')


def find_movies_by_title_part(part_of_name: str) -> list:
    """Search all the movies in the database that matched the user’s query, along with the rating.
    The search is case-insensitive."""
    query = part_of_name.lower()
    return [key for key in movies.keys() if query in key.lower()]


def find_movie_by_index(idx) -> str:
    """Get a movie by its constructed index."""
    movie = list(movies.keys())[idx]
    return movie


def add_movie(movie: str, rating: float) -> None:
    """Add a movie to the db."""
    movies[movie] = rating


def delete_movie(title: str) -> bool:
    """Remove movie from db if it exists."""
    if title in movies.keys():
        del movies[title]
        return True
    return False


def update_movie_rating(title: str, new_rating: float) -> bool:
    """Update the rating of a movie if it exists."""
    if title in movies.keys():
        movies[title] = new_rating
        return True
    return False


if __name__ == '__main__':
    list_movies()
    add_movie(movie='Life of Brian', rating=9.7)
    list_movies()
