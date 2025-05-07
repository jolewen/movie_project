"""Decouple manger from database interaction
in terms of I/O processes. This way the DB could be swapped
without touching the logic of interaction, i.e. MovieManager."""

import json


class MovieStorage:
    def __init__(self, db_path='data/movies.json'):
        self.db_path = db_path
        self.movies = self.get_movies()

    def get_movies(self) -> dict:
        """Read movie data from json file, i.e. database."""
        with open(self.db_path, 'r', encoding='utf-8') as json_file:
            movie_data = json.load(json_file)
        return movie_data

    def _save_movies(self, movies: dict):
        with open(self.db_path, 'w', encoding='utf-8') as json_file:
            json.dump(movies, json_file)

    def add_movie(self, title: str, movie_info: dict):
        """Add movie to database."""
        self.movies = self.get_movies()
        self.movies[title] = movie_info
        self._save_movies(self.movies)

    def update_movie(self, title: str, movie_info: dict):
        self.movies = self.get_movies()
        self.movies[title] = movie_info
        self._save_movies(self.movies)

    def delete_movie(self, title: str):
        self.movies = self.get_movies()
        del self.movies[title]
        self._save_movies(self.movies)