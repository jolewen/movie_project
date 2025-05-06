# Methods to receive basic analytics about the movie database
import numpy as np
import matplotlib.pyplot as plt


def sort_movies(movies: dict, order_key: str = None) -> dict:
    """Sort movies' item tuples by their values (item[1]),
    and as default take the value 'rating' to determine the order.
    Sort movies in descending order.

    :param movies: movies from db
    :param order_key: optionally order by specific key, default is 'rating'

    :returns: sorted list of tuples, which contain movie title nd  the coinfo dict
    """
    if order_key is None:
        order_key = 'rating'
    sorted_movies = sorted(movies.items(), key=lambda item: item[1][order_key], reverse=True)
    sorted_movies = {key: value for key, value in sorted_movies}
    return sorted_movies


def calculate_average_rating(movies: dict):
    """Calculate the average rating of a movie."""
    movie_ratings = [info_item['rating'] for info_item in movies.values()]
    return round(sum(movie_ratings) / len(movies), 1)


def calculate_median_rating(movies: dict):
    """Calculate the median rating of a movie."""
    sorted_movies = sort_movies(movies, order_key='rating')
    sorted_values = [item['rating'] for movie, item in sorted_movies.items()]
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def get_max_rated_movie(movies: dict):
    """Determine the movie(s) with the highest rating."""
    max_rating = max([item['rating'] for item in movies.values()])
    best_rated_movies = [movie for movie, item in movies.items() if item['rating'] == max_rating]
    return best_rated_movies, max_rating


def get_min_rated_movie(movies: dict):
    """Determine the movie(s) with the lowest rating."""
    min_rating = min([item['rating'] for item in movies.values()])
    worst_rated_movies = [movie for movie, item in movies.items() if item['rating'] == min_rating]
    return worst_rated_movies, min_rating


def histogram_ratings(movies: dict, name: str = 'movie_ratings'):
    bins = np.arange(1, 10.5, 0.5)
    ratings = [item['rating'] for item in movies.values()]
    plt.hist(ratings, range=(1,10), bins=bins, color='darkorchid', linewidth=0.33)
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Movie Rating (1-10)')
    plt.ylabel('Occurrence')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.savefig(f"data/{name}.png")


if __name__ == '__main__':
    histogram_ratings({}, 'movie_ratings')
    # get_movies_by_rating()
    # calculate_average_rating()
    # calculate_median_rating()
    # get_max_rated_movies(3)
    # get_worst_rated_movies(3)
