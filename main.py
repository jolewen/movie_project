# Run the CLI to interact with the movie database
from random import randint

from src.crud import *
from src.analytics import *
# FIXME: change to specific methods when done


class CLI:
    def __init__(self):
        print('********** My Movies Database **********')
        self.menu = {1: self.list_movies_flow,
            2: self.add_movie_flow,
            3: self.delete_movie_flow,
            4: self.update_movie_flow,
            5: self.stats_flow,
            6: self.random_movie,
            7: self.search_movie,
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
        list_movies()

    @staticmethod
    def add_movie_flow():
        title = input("Enter movie title: ")
        rating = float(input("Enter rating (0-10): "))
        add_movie(title, rating)

    @staticmethod
    def delete_movie_flow():
        title = input("Enter movie title to delete: ")
        delete_movie(title)

    @staticmethod
    def update_movie_flow():
        title = input("Enter the movie's title to update: ")
        new_rating = float(input(f"Enter the new rating for {title} (0-10): "))
        update_movie(title, new_rating)

    @staticmethod
    def stats_flow():
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
    def random_movie():
        random_pick = randint(0,len(movies))
        print(f"Random movie chosen is: {get_movie_by_index(random_pick)}")

    @staticmethod
    def search_movie():
        part_of_movie_name = input("Enter a (part of) movie title to search: ")
        find_movie_by_name(part_of_movie_name)

    @staticmethod
    def movies_by_rating_flow():
        sorted_movies = get_movies_by_rating()
        print()
        for movie in sorted_movies:
            print(f"{movie}: {movies[movie]}")

    def run_cli(self):
        """Run the CLI program by calling for user input
        and use the function dispatcher pattern to call the corresponding method.
        """
        while True:
            choice = int(input(f"\nEnter choice (1-{self.menu_len}): "))
            if 1 <= choice <= self.menu_len:
                self.menu[choice]()


    def print_options(self):
        print()
        for key, value in self.menu_names.items():
            print(f"{key}: {value}")


def main():
    cli = CLI()
    cli.run_cli()


if __name__ == '__main__':
    main()
