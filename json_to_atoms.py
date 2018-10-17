import collections
from utilities import dict_to_atoms
import json
import pprint
import sys

def main(argv):
	json_file = open(sys.argv[1])
	for element in json_file:
		json_data = json.loads(element)
		for doc in json_data:
			atoms = dict_to_atoms(doc['atoms'])
			user = doc['metadata']['user']
			print(atoms)

if __name__ == "__main__":
	main(sys.argv[1:])
