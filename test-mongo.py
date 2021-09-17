from bson.objectid import ObjectId
import mongoapi


def get_database():
    from pymongo import MongoClient
    from bson.objectid import ObjectId

    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "localhost"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['akifruits']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # # Get the database
    # dbname = get_database()
    # collection_name = dbname["test"]

    # nLeft = {
    # "text" : "Platano",
    # "img" : "http://imagen.html"
    # }

    # nRight = {
    # "text" : "Pepino",
    # "img" : "http://imagen.html"
    # }

    # _ids = collection_name.insert_many([nLeft, nRight])
    # sons = _ids.inserted_ids

    # father = {
    # "text" : "es amarillo",
    # "img" : "http://imagen.html",
    # "nLeft" : sons[0],
    # "nRight" : sons[1]
    # }

    # _id = collection_name.insert_one(father)
    # print(_ids.inserted_ids)

    # item = collection_name.find()
    # for it in item:
    #     print(type(it['_id']))

    # item = collection_name.find()
    # print(item)

    # nodo = ObjectId('6143b1ecd6d2ef892c01fd06')
    # item = collection_name.find_one(nodo)
    # print("father: "+item['text'])
    # hijo = ObjectId(str(item['nLeft']))
    # h = collection_name.find_one(hijo)
    # print("Son: "+h['text'])
    # print(item)
    db = mongoapi.MongoAPI({'database':'akifruits', 'collection':'test'})
    print(db.read())