from pymongo import MongoClient
import logging as log
from bson import ObjectId
import os


class MongoAPI:
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s\n')
        if 'PRODUCTION' in os.environ:
            print("Using remote MongoDB")
            self.client = MongoClient(os.getenv('MONGODB_ENV'))
        else:
            print("Using local MongoDB")
            self.client = MongoClient('localhost')
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read_all(self):
        log.info('Rading all data')
        documents = self.collection.find()
        output = [{item: data[item] for item in data} for data in documents]
        return output

    def write(self, data):
        log.info('Writing data')
        new_document = data['document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def get_node(self, id):
        log.info('Retriving a single document.')
        obj = ObjectId(id)
        response = self.collection.find_one(obj)
        del response['_id']
        return response

    def get_root(self):
        log.info("Retriving root node")
        return self.collection.find_one({"root": "true"})

    def update(self, id, data):
        log.info('Updating document')
        filt = {"_id": ObjectId(id)}
        new_data = {"$set": data}
        response = self.collection.update_one(filt, new_data)
        output = {'Status': 'Successfully Updated' if response.modified_count >
                  0 else "Nothing was updated."}
        return output


if __name__ == "__main__":
    db = MongoAPI({'database': 'akifruits', 'collection': 'tree'})

    db.collection.drop()

    dataLeft = {
        "text": "fresa",
        "img": "https://pixabay.com/get/g8469cf79723db7ff919ec3152b38dd3132d0258bb9563968ef698a0c0110a2fe515fc0369af3b81cefbe3af46d313024_640.jpg",
    }

    nLeft = db.write({"document": dataLeft})

    dataRight = {
        "text": "jícama",
        "img": "https://pixabay.com/get/g50eaab83c66d05532fede4f7e221edf77ca52e00111c2868ec1a6e607a16b57ed8c6e8c1c60682422b59013628bd1431_640.jpg",
    }

    nRight = db.write({"document": dataRight})

    root = {
        "text": "es dulce",
        "nLeft": nLeft['Document_ID'],
        "nRight": nRight['Document_ID'],
        "root": "true"
    }

    father = db.write({"document": root})