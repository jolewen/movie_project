# Run the CLI to interact with the movie database
from random import randint

from src.analytics import (calculate_median_rating,
                           calculate_average_rating,
                           get_max_rated_movie,
                           get_min_rated_movie,
                           sort_movies,
                           histogram_ratings)
from src.crud import (load_movies_json,
                      list_movies,
                      find_movie_by_index,
                      find_movie_by_full_title,
                      find_movies_by_title_part,
                      add_movie,
                      delete_movie,
                      update_movie_info,
                      TEMPLATE)


class CLI:
    def __init__(self):
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
        self.movies = load_movies_json(db_path='data/movies.json')
        self.msg_invalid_choice = "Invalid choice!\nPlease enter a number from the menu."
        self.print_options()

    def exit_flow(self):
        print('Thank you and goodbye!')
        self._running = False

    @staticmethod
    def _query_additional_movie_info(key_value=False) -> dict:
        """Option to ask the user to enter
        additional information about the movie.

        :returns: additional movie information as dict
        """
        _ask_more_input = True
        info_dict = {}
        _options = {key for key in TEMPLATE.keys() if key not in ['rating', 'year']}
        while _ask_more_input:
            key = input('\n(ENTER to skip, help to see options)\nInformation key : ')
            if key == '':
                _ask_more_input = False
            elif key == 'help':
                for _opt in _options:
                    print(f'\t {_opt}')
            else:
                value = key if key_value else input('Information value: ')
                info_dict[key] = value
        print()
        return info_dict

    def list_movies_flow(self):
        """Lists all the movies in the database with year and rating.
        Optionally, show requested details."""
        info_list = list(self._query_additional_movie_info(key_value=True).keys())
        list_movies(self.movies, info_list)

    def add_movie_flow(self):
        """Adds a movie to the database. It needs to have a release year and rating
        and optionally queries for key value pairs to add.
        Acceptance of specific keys & values is handled in the CRUD module."""
        title = input("Enter movie title: ")
        rating = float(input("Enter rating (0-10): "))
        year = int(input("Enter release year: "))
        info_dict = self._query_additional_movie_info()
        add_movie(self.movies, title, rating, year, info_dict)
        print(f"Movie {title} successfully added.")

    def delete_movie_flow(self):
        """Deletes a movie from the database."""
        title = input("Enter movie title to delete: ")
        res = delete_movie(self.movies, title)
        if res:
            print(f"Movie {title} successfully deleted.")
        else:
            print(f"Movie '{title}' doesn't exist!.")

    def update_movie_flow(self):
        """Update the rating of a movie.
        Case-sensitive and full movie name matching."""
        title = input("Enter the movie's title to update: ")
        _, rating = find_movie_by_full_title(self.movies, title)
        if rating:
            info_dict = self._query_additional_movie_info()
            _ = update_movie_info(self.movies, title, info_dict)
            print(f"Movie '{title}' successfully updated!")
        else:
            print(f"Movie '{title}' doesn't exist!.")

    def stats_flow(self):
        """Print a formatted overview of database statistics to stdout.
        Average, median, best and worst ratings."""
        print(f"\nAverage rating: {calculate_average_rating(self.movies)}")
        print(f"Median rating: {calculate_median_rating(self.movies)}")
        best_movies, best_rating = get_max_rated_movie(self.movies)
        print(f"Best movie(s): {best_movies[0]}, {best_rating}")
        for movie in range(1, len(best_movies)):
            print(f"\t\t\t   {best_movies[movie]}, {best_rating}")
        worst_movies, worst_rating = get_min_rated_movie(self.movies)
        print(f"Worst movie(s): {worst_movies[0]}, {worst_rating}")
        for movie in range(1, len(worst_movies)):
            print(f"\t\t\t\t{worst_movies[movie]}, {worst_rating}")

    def random_movie_flow(self):
        """Select a random movie for the user to watch tonight."""
        random_pick = randint(0, len(self.movies))
        movie = find_movie_by_index(self.movies, random_pick)
        print(f"\nYour movie for tonight: {movie}, it's rated {self.movies[movie]['rating']}")

    def search_movie_flow(self):
        """Print all movies matching the search criteria provided by the user.
        The search is case-insensitive."""
        part_of_movie_name = input("Enter a (part of) movie title to search: ")
        matching_movies = find_movies_by_title_part(self.movies, part_of_movie_name)
        if matching_movies:
            for movie in matching_movies:
                print(f"{movie} ({self.movies[movie]['year']}), {self.movies[movie]['rating']}")
        else:
            print(f"No movies matching '{part_of_movie_name}' found.")

    def movies_by_rating_flow(self):
        """Print all movies sorted by rating"""
        sorted_movies = sort_movies(self.movies)
        print()
        for movie in sorted_movies:
            print(f"{movie} ({self.movies[movie]['year']}), {self.movies[movie]['rating']}")

    def create_histogram_flow(self):
        """Create a histogram of the rating of the movies."""
        destination = input("Enter a file name for the histogram output: ")
        if destination == '':
            destination = 'movie_ratings.png'
        histogram_ratings(self.movies, destination)
        print(f"\nHistogram saved to: data/{destination}.png")

    def print_options(self):
        """Print the options menu to stdout."""
        print('\nMenu:')
        for key, value in self.menu_names.items():
            print(f"{key}: {value}")
        print()

    def run_cli(self):
        """Run the CLI program by calling for user input
        and use the function dispatcher pattern to call the corresponding method."""
        while self._running:
            try:
                choice = int(input(f"Enter choice (0-{self.menu_len-1}): "))
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


def main():
    cli = CLI()
    cli.run_cli()


if __name__ == '__main__':
    main()
