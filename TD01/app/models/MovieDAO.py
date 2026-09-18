import sqlite3
from app.models.Movie import Movie


class MovieDAO:
    def __init__(self, db_path):
        """
        db_path : chemin vers le fichier de base de données SQLite
        (ex: 'database.db').
        """
        self.db_path = db_path

    def _get_connection(self):
        """
        Ouvre une nouvelle connexion à la base de données.
        row_factory permet de récupérer les résultats sous forme
        de dictionnaires plutôt que de tuples bruts.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_all_movies(self):
        """
        Récupère tous les films de la base de données.
        Retourne une liste d'instances de Movie.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        conn.close()

        return [Movie.from_dict(dict(row)) for row in rows]

    def get_movie_by_id(self, movie_id):
        """
        Récupère un film spécifique via son id.
        Retourne une instance de Movie, ou None si aucun film trouvé.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        return Movie.from_dict(dict(row))