from flask import (Flask, jsonify, request, redirect, url_for, render_template,
                   abort)
from pymongo import MongoClient
from movies import MovieCollection


app = Flask(__name__)
client = MongoClient('mongodb://localhost')
database = client.video
movie_collection = MovieCollection(database)


@app.route('/')
def index():
    """Index page. It will be redirected to /movies."""
    return redirect(url_for('list_all_movies'))


@app.route('/movies')
def list_all_movies():
    """Return a list of movies."""
    app.logger.debug("Method list_all_movies")

    return jsonify(movie_collection.list())


@app.route('/movies/<imdb>', methods=['GET', 'PUT', 'DELETE'])
def retrieve_single_movie(imdb):
    """Return a specific movie based on IMDB id."""

    if request.method == 'GET':
        movie = movie_collection.read(imdb)

        if movie:
            return jsonify(movie)
    elif request.method == 'PUT':
        movie = movie_collection.update(request.json)

        if movie:
            return jsonify(movie)

    return abort(404)


@app.errorhandler(404)
def page_not_found_error(error):
    """Render a personalized template for 404 status code.

        Flask look for templates on 'templates' directory.
    """
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run()
