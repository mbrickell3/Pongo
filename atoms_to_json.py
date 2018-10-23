import collections
from utilities import MyEncoder, atoms_to_dict, calc_to_dict, dict_to_atoms, format_metadata
from ase.io.trajectory import Trajectory
from collections import OrderedDict
#from bson import json_util
#from bson import Binary, Code
#from bson.json_util import dumps
import datetime
import json
import pprint
import sys

def main(argv):
	trajfile = sys.argv[1]
	jsonfile = sys.argv[2]
	traj = Trajectory(trajfile)
	with open(jsonfile, 'w') as out:
		for atoms in traj:
			atom_dict = atoms_to_dict(atoms)
			print(dict_to_atoms(atom_dict))
			#calc_dict = calc_to_dict(atoms)
			#meta_dict = format_metadata()
			y = OrderedDict([("atoms",atom_dict)])
			#out.write(dumps(y))
			#List = dumps(y)
			#print(List)
			#print(type(List))
			#x = type(List)
			#print(x)
			json.dump(y, out, cls = MyEncoder)
if __name__ == "__main__":
	main(sys.argv[1:])
