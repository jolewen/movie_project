# Methods to receive basic analytics about the movie database
from data.movies import movies


def get_movies_by_rating():
    """Sort movies in descending order by the rating."""
    return sorted(movies, key=movies.get, reverse=True)


def calculate_average_rating():
    """Calculate the average rating of a movie."""
    return sum(movies.values()) / len(movies)


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
    """Determine the movie(s) with the highest rating."""
    max_rating = max(movies.values())
    best_movies = [movie for movie, rating in movies.items() if rating == max_rating]
    return best_movies, max_rating


def get_min_rated_movie():
    """Determine the movie(s) with the lowest rating."""
    min_rating = min(movies.values())
    worst_movies = [movie for movie, rating in movies.items() if rating == min_rating]
    return worst_movies, min_rating


if __name__ == '__main__':
    get_movies_by_rating()
    # calculate_average_rating()
    # calculate_median_rating()
    # get_max_rated_movies(3)
    # get_worst_rated_movies(3)
