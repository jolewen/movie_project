from ast import literal_eval
from random import randint

from src.MovieManager import MovieManager


class CLI:
    def __init__(self, movie_manager: MovieManager):
        self._running = True
        print('********** My Movies Database **********')
        self.menu = {0: self.exit_flow,
                     1: self.list_movies_flow,
                     2: self.add_movie_flow,
                     3: self.delete_movie_flow,
                     4: self.update_movie_flow,
                     5: self.stats_flow,
                     6: self.random_movie_flow,
                     7: self.search_movie_flow,
                     8: self.movies_by_rating_flow,
                     9: self.create_histogram_flow}
        self.menu_names = {0: "Exit",
                           1: "List movies",
                           2: "Add movie",
                           3: "Delete movie",
                           4: "Update movie",
                           5: "Stats",
                           6: "Random movie",
                           7: "Search movie",
                           8: "Movies sorted by rating",
                           9: "Create ratings histogram"}
        self.menu_len = len(self.menu)
        self.movie_manager = movie_manager
        self.msg_invalid_choice = "Invalid choice!\nPlease enter a number from the menu."
        self.print_options()

    def print_options(self):
        """Print the options menu to stdout."""
        print('\nMenu:')
        for key, value in self.menu_names.items():
            print(f"{key}: {value}")
        print()

    def exit_flow(self):
        print('Thank you and goodbye!')
        self._running = False

    def _query_additional_movie_info(self, key_is_value=False) -> dict:
        """Option to ask the user to enter
        additional information about the movie.
        Note: List additions are currently not supported.

        :returns: additional movie information as dict
        """
        _ask_more_input = True
        info_dict = {}
        _options = {key for key in self.movie_manager.template.keys() if key not in ['rating', 'year']}
        print("\n[optional] Query additional information about your movie."
              "\nPress ENTER to confirm/skip, type 'help' to see options.")
        while _ask_more_input:
            key = input('\nAdditional information key: ')
            if key == '':
                _ask_more_input = False
            elif key == 'help':
                for _opt in _options:
                    print(f'\t {_opt}')
            else:
                value = key if key_is_value else literal_eval(input('Additional information value: '))
                info_dict[key] = value
        print()
        return info_dict

    def list_movies_flow(self):
        """Lists all the movies in the database with year and rating.
        Optionally, show requested details."""
        info_list = list(self._query_additional_movie_info(key_is_value=True).keys())
        self.movie_manager.list_movies(info_list)

    def add_movie_flow(self):
        """Adds a movie to the database. It needs to have a release year and rating
        and optionally queries for key value pairs to add.
        Acceptance of specific keys & values is handled in the CRUD module."""
        title = input("Enter movie title: ")
        rating = float(input("Enter rating (0-10): "))
        year = int(input("Enter release year: "))
        info_dict = self._query_additional_movie_info()
        self.movie_manager.add_movie(title, rating, year, info_dict)
        print(f"Movie {title} successfully added.")

    def delete_movie_flow(self):
        """Deletes a movie from the database."""
        title = input("Enter movie title to delete: ")
        res = self.movie_manager.delete_movie(title)
        if res:
            print(f"Movie {title} successfully deleted.")
        else:
            print(f"Movie '{title}' doesn't exist!.")

    def update_movie_flow(self):
        """Update the rating of a movie.
        Case-sensitive and full movie name matching."""
        title = input("Enter the movie's title to update: ")
        _, rating = self.movie_manager.find_movie_by_full_title(title)
        if rating:
            info_dict = self._query_additional_movie_info()
            _ = self.movie_manager.update_movie_info(title, info_dict)
            print(f"Movie '{title}' successfully updated!")
        else:
            print(f"Movie '{title}' doesn't exist!.")

    def stats_flow(self):
        """Print a formatted overview of database statistics to stdout.
        Average, median, best and worst ratings."""
        print(f"\nAverage rating: {self.movie_manager.calculate_average_rating()}")
        print(f"Median rating: {self.movie_manager.calculate_median_rating()}")
        best_movies, best_rating = self.movie_manager.get_max_rated_movie()
        print(f"Best movie(s): {best_movies[0]}, {best_rating}")
        for movie in range(1, len(best_movies)):
            print(f"\t\t\t   {best_movies[movie]}, {best_rating}")
        worst_movies, worst_rating = self.movie_manager.get_min_rated_movie()
        print(f"Worst movie(s): {worst_movies[0]}, {worst_rating}")
        for movie in range(1, len(worst_movies)):
            print(f"\t\t\t\t{worst_movies[movie]}, {worst_rating}")

    def random_movie_flow(self):
        """Select a random movie for the user to watch tonight."""
        random_pick = randint(0, len(self.movie_manager.movies))
        movie = self.movie_manager.find_movie_by_index(random_pick)
        print(f"\nYour movie for tonight: {movie}, it's rated {self.movie_manager.movies[movie]['rating']}")

    def search_movie_flow(self):
        """Print all movies matching the search criteria provided by the user.
        The search is case-insensitive."""
        part_of_movie_name = input("Enter a (part of) movie title to search: ")
        matching_movies = self.movie_manager.find_movies_by_title_part(part_of_movie_name)
        if matching_movies:
            for movie in matching_movies:
                print(
                    f"{movie} ({self.movie_manager.movies[movie]['year']}), {self.movie_manager.movies[movie]['rating']}")
        else:
            print(f"No movies matching '{part_of_movie_name}' found.")

    def movies_by_rating_flow(self):
        """Print all movies sorted by rating"""
        sorted_movies = self.movie_manager.sort_movies()
        print()
        for movie in sorted_movies:
            print(f"{movie} ({self.movie_manager.movies[movie]['year']}), {self.movie_manager.movies[movie]['rating']}")

    def create_histogram_flow(self):
        """Create a histogram of the rating of the movies."""
        destination = input("Enter a file name for the histogram output: ")
        if destination == '':
            destination = 'movie_ratings.png'
        self.movie_manager.histogram_ratings(destination)
        print(f"\nHistogram saved to: data/{destination}.png")

    def run_cli(self):
        """Run the CLI program by calling for user input
        and use the function dispatcher pattern to call the corresponding method."""
        while self._running:
            try:
                choice = int(input(f"Enter choice (0-{self.menu_len - 1}): "))
                action = self.menu.get(choice)
                if action:
                    action()
                else:
                    print(self.msg_invalid_choice)
            except ValueError:
                print(self.msg_invalid_choice)

            if self._running:
                input("\nPress enter to continue")
                self.print_options()


if __name__ == '__main__':
    movie_manager = MovieManager(db_path='data/movies.json')
    cli = CLI(movie_manager)
    cli.run_cli()
