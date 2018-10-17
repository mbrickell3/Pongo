from pickle import load
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor

def pcklfile_to_dict():
    l = load(open('refingerprinted_database.pckl','r'))
    return l

def dict_to(dictionary):
    x = 0
    for key in dictionary.keys():
        if (x == 20):
            y = dictionary[key]['surface']
            w = AseAtomsAdaptor.get_atoms(y)
            print(w)
            #if (isinstance(pymatgen.core.strcture.Structure, type(y))):
            #        print("yay")
        x = x + 1

def main():
    diction = pcklfile_to_dict()
    dict_to(diction)
    
if __name__== "__main__":
    main()
