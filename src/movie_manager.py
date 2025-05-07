"""MovieManager - interaction with the movie database"""
import numpy as np
import matplotlib.pyplot as plt

from movie_storage import MovieStorage


class MovieManager(MovieStorage):
    """MovieManager - interaction with the movie "database" (data/movies.json).
    Contains methods meant to provide CRUD interactions.
    Additionally, holds basic analytical functionality.
    """

    def __init__(self, db_path='data/movies.json'):
        super().__init__(db_path)
        self.template = {
            "rating": 0.1,
            "year": 0,
            "actors": [],
            "director": "",
            "gross": 0
        }

    @staticmethod
    def _print_requested_details(movie, info_list):
        """Print valid (i.e. templated) additional movie information."""
        _movie_details_to_show = {value: movie[value] for value in info_list if
                                  movie.get(value)}
        for key, value in _movie_details_to_show.items():
            print(f"{key}: {value}")
        if _movie_details_to_show:
            # space out for readability
            print()

    def list_movies(self, info_query: list = None) -> None:
        """Lists the number of movies, as well as their title and rating.
        Print further details if specified and found in db.
        """
        if info_query is None:
            info_query = []
        print(f"{len(self.movies)} movies in total")
        for movie_title, movie in self.movies.items():
            print(f"{movie_title} ({movie['year']}): {movie['rating']}")
            if info_query:
                self._print_requested_details(movie, info_query)

    def find_movie_by_full_title(self, title: str) -> tuple[str, str]:
        """Finds a movie by its full title."""
        return title, self.movies.get(title, '')

    def find_movies_by_title_part(self, part_of_name: str) -> list:
        """Search all the movies in the database that matched the user’s query,
        along with the rating. The search is case-insensitive."""
        query = part_of_name.lower()
        return [key for key in self.movies.keys() if query in key.lower()]

    def find_movie_by_index(self, idx: int) -> str:
        """Get a movie by its constructed index."""
        movie = list(self.movies.keys())[idx]
        return movie

    def manage_add_movie(self,
                         title: str,
                         rating: float,
                         year: int,
                         addition_info: dict = None) -> None:
        """Add a movie to the db. To be identifiable it needs to have
        rating and release year. If there is more information provided
        than rating and release year, put said info into the db, too
        - if valid, i.e. templated.
        """

        if addition_info is None:
            addition_info = {}
        if title not in self.movies:
            new_movie_info = {key: value for key, value in self.template.items()
                              if key not in ['rating', 'year']}
            new_movie_info['rating'] = rating
            new_movie_info['year'] = year
            for key, value in addition_info.items():
                new_movie_info[key] = value
            self.add_movie(title, new_movie_info)

    def manage_delete_movie(self, title: str) -> bool:
        """Remove movie from db if it exists."""
        if title in self.movies.keys():
            self.delete_movie(title)
            return True
        return False

    def manage_update_movie(self, title: str, new_info: dict = None) -> bool:
        """Update the information of a movie if it exists.
        Cannot add information arbitrarily.
        """
        if new_info is None:
            new_info = {}
        if title in self.movies:
            _update_info = {key: value for key, value in new_info.items()
                            if key in self.template.keys()}
            _update_info = {key: value for key, value in _update_info.items()
                            if isinstance(self.movies[title][key], type(value))}
            for _info_key, _info_value in _update_info.items():
                self.movies[title][_info_key] = _info_value
            return True
        return False

    def sort_movies(self, order_key: str = None) -> dict:
        """Sort movies' item tuples by their values (item[1]),
        and as default take the value 'rating' to determine the order.
        Sort movies in descending order.

        :param order_key: optionally order by specific key, default is 'rating'

        :returns: sorted list of tuples,
                  which contain movie title and the info dict
        """
        if order_key is None:
            order_key = 'rating'
        sorted_movies = sorted(self.movies.items(),
                               key=lambda item: item[1][order_key],
                               reverse=True)
        sorted_movies = dict(sorted_movies)
        return sorted_movies

    def calculate_average_rating(self):
        """Calculate the average rating of a movie."""
        ratings = [info_item['rating'] for info_item in self.movies.values()]
        return round(sum(ratings) / len(self.movies), 1)

    def calculate_median_rating(self):
        """Calculate the median rating of a movie."""
        sorted_movies = self.sort_movies(order_key='rating')
        sorted_info = [item['rating'] for movie, item in sorted_movies.items()]
        data_length = len(sorted_info)
        mid = data_length // 2
        if data_length % 2 == 1:
            return sorted_info[mid]
        return (sorted_info[mid - 1] + sorted_info[mid]) / 2

    def get_max_rated_movie(self):
        """Determine the movie(s) with the highest rating."""
        max_rating = max([item['rating'] for item in self.movies.values()])
        best_rated_movies = [movie for movie, item in self.movies.items()
                             if item['rating'] == max_rating]
        return best_rated_movies, max_rating

    def get_min_rated_movie(self):
        """Determine the movie(s) with the lowest rating."""
        min_rating = min([item['rating'] for item in self.movies.values()])
        worst_rated_movies = [movie for movie, item in self.movies.items()
                              if item['rating'] == min_rating]
        return worst_rated_movies, min_rating

    def histogram_ratings(self, name: str = 'movie_ratings'):
        """Create a rating histogram
        and save it as .png under the given name."""
        bins = np.arange(1, 10.5, 0.5)
        ratings = [item['rating'] for item in self.movies.values()]
        plt.hist(ratings,
                 range=(1, 10),
                 bins=bins,
                 color='darkorchid',
                 linewidth=0.33)
        plt.title('Distribution of Movie Ratings')
        plt.xlabel('Movie Rating (1-10)')
        plt.ylabel('Occurrence')
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.savefig(f"data/{name}.png")


if __name__ == '__main__':
    movie_manager = MovieManager(db_path='data/movies.json')

    movie_manager.list_movies()
    additional_info = {'actors': ["Graham Chapman",
                                  "John Cleese",
                                  "Terry Gilliam",
                                  "Eric Idle",
                                  "Terry Jones",
                                  "Michael Palin"]}
    movie_manager.manage_add_movie(
        title='Life of Brian',
        rating=8.0,
        year=1979,
        addition_info=additional_info
    )
    info_query: list = ['actors', 'gross']
    movie_manager.list_movies(info_query)
    movie_manager.histogram_ratings('movie_ratings')
