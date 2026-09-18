class Movie:
    def __init__(self, id=None, title=None, year=None, genres=None,
                 href=None, extract=None, cover=None):
        self.id = id
        self.title = title
        self.year = year
        self.genres = genres
        self.href = href
        self.extract = extract
        self.cover = cover

    @classmethod
    def from_tuple(cls, row):
        """
        Crée une instance de Movie à partir d'un tuple
        (résultat brut d'une requête SQL, ex: cursor.fetchone()).
        L'ordre des champs doit correspondre à l'ordre des colonnes
        dans la table SQL : id, title, year, genres, href, extract, cover.
        """
        return cls(
            id=row[0],
            title=row[1],
            year=row[2],
            genres=row[3],
            href=row[4],
            extract=row[5],
            cover=row[6],
        )

    @classmethod
    def from_dict(cls, data):
        """
        Crée une instance de Movie à partir d'un dictionnaire
        (utile si tu utilises un curseur qui retourne des dict,
        ex: sqlite3.Row ou psycopg2 avec RealDictCursor).
        """
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            year=data.get("year"),
            genres=data.get("genres"),
            href=data.get("href"),
            extract=data.get("extract"),
            cover=data.get("cover"),
        )

    def to_dict(self):
        """Pratique pour sérialiser en JSON (ex: réponse d'API Flask/FastAPI)."""
        return self.__dict__

    def __repr__(self):
        return f"<Movie id={self.id} title='{self.title}' year={self.year}>"