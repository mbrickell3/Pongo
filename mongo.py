import pymongo
from pymongo import MongoClient
from collections import OrderedDict
from utilities import MyEncoder
import os.path
import sys
import json
import pprint

def get_Client_uri():
    return "mongodb://127.0.0.1:27017"

def Mongo_insert_json_file(filename, collection = 'test', database = 'admin'):
        user_uri = get_Client_uri()
        client = MongoClient(user_uri)
        db = client[database]
        collection = db['test']
        job1 = json.loads(open(filename, 'r').read())
        collection.insert_one(job1)
        return 1

def Mongo_query(query = None, database = 'admin', collection = 'test'):
        result = []
        user_uri = get_Client_uri()
        client = MongoClient(user_uri)
        db=client[database]
        collection = db[collection]
        for post in collection.find():
                result.append(post)
                for key in post.keys():
                    if key != '_id':
                        y = OrderedDict({key : post[key]})
                        file = create_file(key)
                        with open(file, 'w') as out:
                            json.dump(y, out, cls = MyEncoder)

        return result

def create_file(elem):
    file = elem + '.json'
    os_path = os.path.abspath('~') + '/mongo_json'
    script_path = os.path.dirname(os.path.abspath( 'mongo.py' )) + '/mongo_json'
    completeName = os.path.join(script_path, file)
    return completeName


def main(argv):
    try:
        Mongo_insert_json_file(sys.argv[1])
    except:
        Mongo_query()
    
if __name__== "__main__":
    main(sys.argv[1:])

