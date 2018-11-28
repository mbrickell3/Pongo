from pickle import load
from ase import Atoms
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor
from utilities import atoms_to_dict, MyEncoder, format_metadata
from collections import OrderedDict
import sys
import json
import os.path
import hashlib

def pcklfile_to_dict(pckl_file):
    l = load(open(pckl_file,'r'))
    return l

def dict_to(dictionary):
    x = 0
    for key in dictionary.keys():
        y = dictionary[key]['surface']
        if (isinstance(y, dict) == False):
            w = AseAtomsAdaptor.get_atoms(y)
            z = atoms_to_dict(w)
            atom_hash = get_hash(w)
            add_everything_to_dict(key, dictionary[key], z, atom_hash)
        else:
            y = dictionary[key]['surface']
            w = AseAtomsAdaptor.get_atoms(Structure.from_dict(y))
            z = atoms_to_dict(w)
            atom_hash = get_hash(w)
            add_everything_to_dict(key, dictionary[key], z, atom_hash)

def add_everything_to_dict(elem, dictionary, atoms_dict, atom_hash = None):
    newDict = {'surface' : atoms_dict, 'hash' : atom_hash, 'metadata' : format_metadata()}
    file = elem + '.json'
    os_path = os.path.abspath('~') + '/pckl_json'
    script_path = os.path.dirname(os.path.abspath( 'convert.py' )) + '/pckl_json'
    completeName = os.path.join(script_path, file)
    with open(completeName, 'w') as out:
        for key in dictionary.keys():
            if (key != 'surface'):
                newDict[key] = dictionary[key]
        y = OrderedDict({elem : newDict})
        json.dump(y, out, cls = MyEncoder)

def get_hash(atoms):
  string = str(atoms.pbc)
  for number in atoms.cell.flatten():
    string += '%.15f' % number
#  for number in atoms.get_atomic_number():
#    string += '%3d' % number
#  for number in atoms.get_positions():
#    string += '%.15f' % number
  
  md5 = hashlib.md5(string.encode('utf-8'))
  hash = md5.hexdigest()
  return hash

def main(argv):
    diction = pcklfile_to_dict(sys.argv[1])
    dict_to(diction)
    
if __name__== "__main__":
    main(sys.argv[1:])
