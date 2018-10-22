from pickle import load
from ase import Atoms
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor
from utilities import atoms_to_dict, MyEncoder
from collections import OrderedDict
import json

def pcklfile_to_dict():
    l = load(open('refingerprinted_database.pckl','r'))
    return l

def dict_to(dictionary):
    file_object = open("new_output.txt", "w")
    x = 0
    for key in dictionary.keys():
        y = dictionary[key]['surface']
        if (isinstance(y, dict) == False):
            w = AseAtomsAdaptor.get_atoms(y)
            z = atoms_to_dict(w)
            add_everything_to_dict(key, dictionary[key], z)
            #print(type(z))
        else:
            y = dictionary[key]['surface']
            add_everything_to_dict(key, dictionary[key], y)

def add_everything_to_dict(elem, dictionary, atoms_dict):
    newDict = {'surface' : atoms_dict}
    with open('test.json', 'a') as out:
        for key in dictionary.keys():
            if (key != 'surface'):
                #print(key)
                #json.dump(dictionary[key], out, cls = MyEncoder)
                newDict[key] = dictionary[key]
        y = OrderedDict({elem : newDict})
        json.dump(y, out, cls = MyEncoder)
  
def main():
    diction = pcklfile_to_dict()
    dict_to(diction)
    
if __name__== "__main__":
    main()
