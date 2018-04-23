from flask import Flask, jsonify, request, redirect, url_for, render_template
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
    return jsonify(movie_collection.list())


@app.route('/movies/<imdb>', methods=['GET', 'PUT'])
def retrieve_single_movie(imdb):
    """Return a specific movie based on IMDB id."""
    if request.method == 'GET':
        return jsonify(movie_collection.read(imdb))


@app.errorhandler(404)
def page_not_found_error(error):
    """Render a personalized template for 404 status code.

        Flask look for templates on 'templates' directory.
    """
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run()
