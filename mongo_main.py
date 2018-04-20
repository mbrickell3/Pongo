import sys
import pprint
import datetime
import json
from insertjson import Mongo_insert_json_file, Mongo_query, Mongo_delete
from utilities import MyEncoder

def main(argv):
	if (sys.argv[1] == "query"):
		x = datetime.datetime(2015, 7, 8, 11, 17, 42, 911000)
		#print(x)
		#i = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
		#beg = '2018-04-08T15:09:50'
		#end = '0000-00-00T00:00:00'
		#i = x < d
		#query = {'atoms' : {'atoms':  {"$all": [{u'charge': 0.0,
                       
		#query = {'metadata': {u'user': u'mbrickell3', {u'time': {"$date": 1523654054983}}}}
		query = {}
		filename = input("Please give me a file to output to: ")
		x = Mongo_query(query, 'medford-data', 'test')
		#print(type(x[0]))
		temp = []
		with open(filename, 'w') as io:
			for elem in x:
				del(elem['_id'])
				temp.append(elem)
				#print(elem)
			#print(temp)
			json.dump(temp, io)
	elif (sys.argv[1] == "delete"):
		Mongo_delete({})
	elif (sys.argv[1] == "insert"):
		x = 0
		while (x == 0):
			#try:
			filename = input("Please give me a json file to insert: ")
			if (filename[-4::] != "json"):
				print("That is not a recognized file name, please try again")
			else:
				x = Mongo_insert_json_file(filename)
				print("Document Inserted!")
			#except:
			#	print("Remember you need to give me a string")
	else:
		print("I don't recognize that option, either say 'query', 'insert', or 'delete")


if __name__ == "__main__":
	main(sys.argv[1:])
