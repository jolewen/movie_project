# Run the CLI to interact with the movie database
from random import randint

from data.movies import movies
from src.analytics import (calculate_median_rating,
                           calculate_average_rating,
                           get_max_rated_movie,
                           get_min_rated_movie,
                           get_movies_by_rating)
from src.crud import (list_movies,
                      find_movie_by_index,
                      find_movie_by_full_title,
                      find_movies_by_title_part,
                      add_movie,
                      delete_movie,
                      update_movie_rating)


class CLI:
    def __init__(self):
        print('********** My Movies Database **********')
        self.menu = {1: self.list_movies_flow,
                     2: self.add_movie_flow,
                     3: self.delete_movie_flow,
                     4: self.update_movie_flow,
                     5: self.stats_flow,
                     6: self.random_movie_flow,
                     7: self.search_movie_flow,
                     8: self.movies_by_rating_flow}
        self.menu_names = {1: "List movies",
                           2: "Add movie",
                           3: "Delete movie",
                           4: "Update movie",
                           5: "Stats",
                           6: "Random movie",
                           7: "Search movie",
                           8: "Movies sorted by rating"}
        self.menu_len = len(self.menu)
        self.print_options()

    @staticmethod
    def list_movies_flow():
        """Lists all the movies in the database."""
        list_movies()

    @staticmethod
    def add_movie_flow():
        """Adds a movie to the database."""
        title = input("Enter movie title: ")
        rating = float(input("Enter rating (0-10): "))
        add_movie(title, rating)
        print(f"Movie {title} successfully added.")

    @staticmethod
    def delete_movie_flow():
        """Deletes a movie from the database."""
        title = input("Enter movie title to delete: ")
        res = delete_movie(title)
        if res:
            print(f"Movie {title} successfully deleted.")
        else:
            print(f"Movie '{title}' doesn't exist!.")

    @staticmethod
    def update_movie_flow():
        """Update the rating of a movie.
        Case-sensitive and full movie name matching."""
        title = input("Enter the movie's title to update: ")
        _, rating = find_movie_by_full_title(title)
        if rating:
            new_rating = float(input(f"Enter the new rating for {title} (0-10): "))
            _ = update_movie_rating(title, new_rating)
            print(f"Movie '{title}' successfully updated!")
        else:
            print(f"Movie '{title}' doesn't exist!.")

    @staticmethod
    def stats_flow():
        """Print a formatted overview of database statistics to stdout.
        Average, median, best and worst ratings."""
        print(f"\nAverage rating: {calculate_average_rating()}")
        print(f"Median rating: {calculate_median_rating()}")
        best_movies, best_rating = get_max_rated_movie()
        print(f"Best movie(s): {best_movies[0]}, {best_rating}")
        for movie in range(1, len(best_movies)):
            print(f"\t\t\t   {best_movies[movie]}, {best_rating}")
        worst_movies, worst_rating = get_min_rated_movie()
        print(f"Worst movie(s): {worst_movies[0]}, {worst_rating}")
        for movie in range(1, len(worst_movies)):
            print(f"\t\t\t\t{worst_movies[movie]}, {worst_rating}")

    @staticmethod
    def random_movie_flow():
        """Select a random movie for the user to watch tonight."""
        random_pick = randint(0, len(movies))
        movie = find_movie_by_index(random_pick)
        print(f"\nYour movie for tonight: {movie}, it's rated {movies[movie]}")

    @staticmethod
    def search_movie_flow():
        """Print all movies matching the search criteria provided by the user.
        The search is case-insensitive."""
        part_of_movie_name = input("Enter a (part of) movie title to search: ")
        matching_movies = find_movies_by_title_part(part_of_movie_name)
        if matching_movies:
            for movie in matching_movies:
                print(f"{movie}, {movies[movie]}")
        else:
            print(f"No movies matching '{part_of_movie_name}' found.")

    @staticmethod
    def movies_by_rating_flow():
        """Print all movies sorted by rating"""
        sorted_movies = get_movies_by_rating()
        print()
        for movie in sorted_movies:
            print(f"{movie}: {movies[movie]}")

    def print_options(self):
        """Print the options menu to stdout."""
        print('\nMenu:')
        for key, value in self.menu_names.items():
            print(f"{key}: {value}")

    def run_cli(self):
        """Run the CLI program by calling for user input
        and use the function dispatcher pattern to call the corresponding method."""
        print()
        while True:
            choice = int(input(f"Enter choice (1-{self.menu_len}): "))
            if 1 <= choice <= self.menu_len:
                self.menu[choice]()
            input("\nPress enter to continue")
            self.print_options()
            print()


def main():
    cli = CLI()
    cli.run_cli()


if __name__ == '__main__':
    main()
