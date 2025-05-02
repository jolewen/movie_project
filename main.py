# Run the CLI to interact with the movie database
from src.crud import *
# FIXME: change to specific methods when done


class CLI:
    def __init__(self):
        print('********** My Movies Database **********')
        self.menu = {1: self.list_movies_flow,
            2: self.add_movie_flow,
            3: self.delete_movie_flow,
            4: "Update movie",
            5: "Stats",
            6: "Random movie",
            7: "Search movie",
            8: "Movies sorted by rating"}
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
    def add_movie_flow():
        title = input("Enter movie title: ")
        rating = float(input("Enter rating (0-10): "))
        add_movie(title, rating)


    @staticmethod
    def list_movies_flow():
        list_movies()

    @staticmethod
    def delete_movie_flow():
        title = input("Enter movie title to delete: ")
        delete_movie(title)

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
