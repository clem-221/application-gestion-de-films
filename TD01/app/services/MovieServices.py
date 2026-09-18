from app.models.MovieDAO import MovieDAO


class MovieServices:
    def __init__(self, movie_dao: MovieDAO):
        """
        Le service reçoit le DAO en dépendance plutôt que de le créer
        lui-même : ça facilite les tests (on peut injecter un faux DAO)
        et ça évite de coupler le service à une base de données précise.
        """
        self.movie_dao = movie_dao

    def get_all_movies(self):
        """Retourne la liste complète des films."""
        return self.movie_dao.get_all_movies()

    def get_first_n_movies(self, n):
        """
        Retourne les n premiers films.
        La logique de "combien de films" est une règle métier,
        donc elle a sa place ici plutôt que dans le contrôleur.
        """
        movies = self.movie_dao.get_all_movies()
        return movies[:n]

    def get_all_years(self):
        """
        Retourne la liste des années distinctes présentes en BDD,
        triées par ordre croissant.
        """
        movies = self.movie_dao.get_all_movies()
        years = {movie.year for movie in movies if movie.year is not None}
        return sorted(years)

    def get_movies_by_year(self, year):
        return [m for m in self.movie_dao.get_all_movies() if m.year == year]