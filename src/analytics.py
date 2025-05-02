# Methods to receive basic analytics about the movie database
from data.movies import movies


"""Stats
Print statistics about the movies in the database:
* Average rating in the database.
* Median rating in the database. Read about median, and notice the difference between even number of movies and odd number of movies.
* The best movie by rating. If there are multiple movies with the maximum rate, print all of them.
* The worst movie by rating. If there are multiple movies with the minimum rate, print all of them.
"""


def print_movies_by_rating():
    """Print all the movies and their ratings, in descending order by the rating."""
    pass


def calculate_average_rating():
    """Calculate the average rating of a movie."""
    return sum(movies.values())/len(movies)



def calculate_median_rating():
    """Calculate the median rating of a movie."""
    sorted_values = sorted(list(movies.values()))
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def get_max_rated_movie():
    best_movie = max(movies, key=movies.get)
    rating = movies[best_movie]
    return best_movie, rating


def get_min_rated_movie():
    worst_movie = min(movies, key=movies.get)
    rating = movies[worst_movie]
    return worst_movie, rating


if __name__ == '__main__':
    print_movies_by_rating()
    # calculate_average_rating()
    # calculate_median_rating()
    # get_max_rated_movies(3)
    # get_worst_rated_movies(3)