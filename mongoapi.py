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
        "text": "manzana",
        "img": "link:manzana",
    }

    nLeft = db.write({"document": dataLeft})

    dataRight = {
        "text": "platano",
        "img": "link:platano",
    }

    nRight = db.write({"document": dataRight})

    root = {
        "text": "es rojo",
        "nLeft": nLeft['Document_ID'],
        "nRight": nRight['Document_ID'],
        "root": "true"
    }

    father = db.write({"document": root})