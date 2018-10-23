import collections
from utilities import dict_to_atoms
import json
import pprint
import sys
from ase import atoms
from ase.io import read, write

def main(argv):
	json_file = open(sys.argv[1])
	elem = sys.argv[2]
	traj_file = elem + '.traj'
	for element in json_file:
		json_data = json.loads(element)
		atoms = dict_to_atoms(json_data[elem]['surface'])
		write(traj_file, atoms)

if __name__ == "__main__":
	main(sys.argv[1:])
