import collections
from utilities import dict_to_atoms
import json
import pprint
import sys
from ase import atoms
from ase.io import read, write
import os.path


def main(argv):
	json_file = open(sys.argv[1])
	temp = sys.argv[1].split(".")
	elem = os.path.splitext(sys.argv[1])[0]
	traj_file = elem + '.traj'
	script_path = os.path.dirname(os.path.abspath('convert.py' )) + '/traj'
	completeName = os.path.join(script_path, traj_file)
	for element in json_file:
		json_data = json.loads(element)
		atoms = dict_to_atoms(json_data[elem]['surface'])
		write(completeName, atoms)

if __name__ == "__main__":
	main(sys.argv[1:])
