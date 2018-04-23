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

    def update(self, data):
        imdb = data.get('imdb', None)

        new_data = {
            'title': data.get('title', None),
            'year': data.get('year', None),
            'type': data.get('type', None)
        }

        matched_count = self.collection.update_one(
            { 'imdb': imdb }, { "$set": new_data }
        ).matched_count

        if matched_count > 0:
            movie = self.collection.find_one({ 'imdb': imdb })
            return self.convert(movie)

        return None

    def delete(self):
        pass

    def convert(self, result):
        return json.loads(json_util.dumps(result))
