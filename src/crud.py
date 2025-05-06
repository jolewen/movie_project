# Methods contained are meant to provide CRUD interaction with the movie database (data/movies.json)
import json

TEMPLATE = {
    "rating": 0.1,
    "year": 0,
    "actors": [],
    "director": "",
    "gross": 0
}


def load_movies_json(db_path: str = '../data/movies.json') -> dict:
    """Read movie data from json file, i.e. database."""
    with open(db_path, 'r') as json_file:
        movie_data = json.load(json_file)
    return movie_data


def _print_requested_details(movie, info_list):
    """Print valid (i.e. templated) additional movie information."""
    _movie_details_to_show = {value: movie[value] for value in info_list if movie.get(value)}
    for key, value in _movie_details_to_show.items():
        print(f"{key}: {value}")
    if _movie_details_to_show:
        # space out for readability
        print()


def list_movies(movies: dict, info_query: list = None) -> None:
    """Lists the number of movies, as well as their title and rating.
    Print further details if specified and found in db.
    """
    if info_query is None:
        info_query = []
    print(f"{len(movies)} movies in total")
    for movie_title, movie in movies.items():
        print(f"{movie_title} ({movie['year']}): {movie['rating']}")
        if info_query:
            _print_requested_details(movie, info_query)


def find_movie_by_full_title(movies: dict, title: str) -> tuple[str, str]:
    """Finds a movie by its full title."""
    return title, movies.get(title, '')


def find_movies_by_title_part(movies: dict, part_of_name: str) -> list:
    """Search all the movies in the database that matched the user’s query, along with the rating.
    The search is case-insensitive."""
    query = part_of_name.lower()
    return [key for key in movies.keys() if query in key.lower()]


def find_movie_by_index(movies: dict, idx: int) -> str:
    """Get a movie by its constructed index."""
    movie = list(movies.keys())[idx]
    return movie


def add_movie(movies: dict, title: str, rating: float, year: int, addition_info: dict = None) -> None:
    """Add a movie to the db. To be identifiable it needs to have rating and release year.
    If there is more information provided than rating and release year,
    put said info into the db, too - if valid, i.e. templated.
    """
    if addition_info is None:
        addition_info = {}
    movie_info = {key: value for key, value in TEMPLATE.items() if key not in ['rating', 'year']}
    movie_info['rating'] = rating
    movie_info['year'] = year
    for key, value in addition_info.items():
        movie_info[key] = value
    movies[title] = movie_info


def delete_movie(movies: dict, title: str) -> bool:
    """Remove movie from db if it exists."""
    if title in movies.keys():
        del movies[title]
        return True
    return False


def update_movie_info(movies: dict, title: str, new_info: dict = None) -> bool:
    """Update the information of a movie if it exists.
    Cannot add information arbitrarily.
    """
    if new_info is None:
        new_info = {}
    if title in movies.keys():
        _info_to_update = {key: value for key, value in new_info.items() if key in movies[title].keys()}
        _info_to_update = {key: value for key, value in _info_to_update.items() if
                           type(movies[title][key]) == type(value)}
        for _info_key, _info_value in _info_to_update.items():
            movies[title][_info_key] = _info_value
        return True
    return False


if __name__ == '__main__':
    data = load_movies_json()
    list_movies(data)
    additional_info = {'actors': ["Graham Chapman",
                                  "John Cleese",
                                  "Terry Gilliam",
                                  "Eric Idle",
                                  "Terry Jones",
                                  "Michael Palin"]}
    add_movie(data,
              title='Life of Brian',
              rating=8.0,
              year=1979,
              addition_info=additional_info
              )
    info_query :list = ['actors', 'gross']
    list_movies(data, info_query)
