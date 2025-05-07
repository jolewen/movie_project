"""Run the CLI to interact with the movie database"""
from src.cli import CLI
from src.movie_manager import MovieManager


def main():
    """Main function, instantiate and run the MovieManager & CLI program."""
    movie_manager = MovieManager()
    cli = CLI(movie_manager)
    cli.run_cli()


if __name__ == '__main__':
    main()
