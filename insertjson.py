import pymongo
import json
import pprint
from utilities import user_authentication, get_Client_uri
from pymongo import MongoClient
import sys

def Mongo_insert_json_file(filename, collection = 'test', database = 'medford-data', username = None, password = None):
	if (username == None or password == None):
		username, password = user_authentication()
	user_uri = get_Client_uri(username, password)
	client = MongoClient(user_uri)
	db = client[database]
	collection = db['test']
	job1 = json.loads(open(filename, 'r').read())
	collection.insert_one(job1)
	return 1
	#except:
	#	print("I am unable to insert that document. Make sure the document is in your file directory")
	#	return 0

def Mongo_query(query, database, collection, username = None, password = None):
	result = []
	if (username == None or password == None):
		username, password = user_authentication()
	user_uri = get_Client_uri(username, password)
	client = MongoClient(user_uri)
	db=client[database]
	collection = db[collection]
	pp = pprint.PrettyPrinter()
	for post in collection.find(query):
		#print(type(post))
		result.append(post)
	pp.pprint('total documents found: ' + str(len(result)))
	return result

def Mongo_delete(query,database = 'medford-data', collection = 'test', username = None, password = None):
	if username == None or password == None:
		username, password = user_authentication()
	user_uri  = get_Client_uri(username, password)
	client = MongoClient(user_uri)
	db=client[database]
	collection = db[collection]
	pp = pprint.PrettyPrinter()
	delete_number = collection.find(query).count()
	pp.pprint('')
	pp.pprint('**** WARNING ****: you are about to delete {} documents!!'.format(delete_number))
	pp.pprint('You are abusolutly sure about what you are doing right?')
	
	if sys.version_info[0] == 3:
		if delete_number <= 3:
			check = input('y/n: ')
			if check == 'y':
				collection.delete_many(query)
				pp.pprint('Documents deleted')
			else:
				pp.pprint('Documents Not deleted')
	
		else:
			check = input('type [YesDelete] to delete: ')
			if check == 'YesDelete':
				collection.delete_many(query)
				pp.pprint('Documents deleted')
			else:
				pp.pprint('Documents Not deleted')     
	
	else:
		if delete_number <= 3:
			check = raw_input('y/n: ')
			if check == 'y':
				collection.delete_many(query)
				pp.pprint('Documents deleted')
			else:
				pp.pprint('Documents Not deleted')
	
		else:
			check = raw_input('type [YesDelete] to delete: ')
			if check == 'YesDelete':
				collection.delete_many(query)
				pp.pprint('Documents deleted')
			else:
				pp.pprint('Documents Not deleted')         
	return