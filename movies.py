import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId


class MovieCollection:

    def __init__(self, database):
        self.database = database
        self.collection = database.movies

    def list(self):
        return self.convert(self.collection.find())

    def read(self, imdb):
        movie = self.collection.find_one({ 'imdb': imdb })
        return self.convert(movie)

    def update(self):
        pass

    def delete(self):
        pass

    def convert(self, result):
        return json.loads(json_util.dumps(result))
