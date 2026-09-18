from flask import Blueprint, render_template, abort
from app.services.MovieServices import MovieServices
from app.models.MovieDAO import MovieDAO

movies_bp = Blueprint("movies", __name__, url_prefix="/movies", template_folder="templates")

movie_dao = MovieDAO("app/movies.db")
movie_service = MovieServices(movie_dao)


@movies_bp.route("/")
def movies():
    all_movies = movie_service.get_all_movies()
    return render_template("list.html", movies=all_movies)


@movies_bp.route("/<int:year>")
def movies_by_year(year):
    """
    Affiche les films sortis une année donnée.
    Accessible via http://localhost:8000/movies/<year>
    """
    movies = movie_service.get_movies_by_year(year)

    if not movies:
        abort(404)

    return render_template("by_year.html", year=year, movies=movies)

@movies_bp.route("/first/<int:n>")
def list_first_movies(n):
    movies = movie_service.get_first_n_movies(n)
    return render_template("movies_view.html", movies=movies)