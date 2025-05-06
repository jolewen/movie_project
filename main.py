# Run the CLI to interact with the movie database
from src.CLI import CLI
from src.MovieManager import MovieManager


def main():
    movie_manager = MovieManager()
    cli = CLI(movie_manager)
    cli.run_cli()


if __name__ == '__main__':
    main()
