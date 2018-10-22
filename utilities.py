import pymongo
from datetime import datetime
from pymongo import MongoClient
from collections import OrderedDict
import getpass
import os
import json
import numpy as np
import sys
from ase import Atoms,Atom
from ase.constraints import dict2constraint

class MyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.integer):
      return int(obj)
    elif isinstance(obj, np.floating):
      return float(obj)
    elif isinstance(obj, np.ndarray):
      return obj.tolist()
    else:
      return super(MyEncoder, self).default(obj)

def user_authentication():
    if sys.version_info[0] == 3:
        username = input('user name: ')
        password= getpass.getpass('Password: ')
    else:
        username = raw_input('user name: ')
        password= getpass.getpass('Password: ')
    return username, password

def get_Client_uri(username,password):
    return "mongodb://" + username + ":" + password + "@54.201.152.64/medford-data"

def dict_to_atoms(d):
    atoms=Atoms([Atom(symbol=atom['symbol'],
                      position=atom['position'],
                      tag=atom['tag'],
                      index=atom['index'],
                      charge=atom['charge'],
                      momentum=atom['momentum'],
                      magmom=atom['magmom'])
                      for atom in d['atoms']],
                          cell=d['cell'],
                          pbc=d['pbc'],
                          info=d['info'],
                          constraint=[dict2constraint(c) for c in d['constraints']])
    return atoms

def atoms_to_dict(atoms):
    d=OrderedDict(atoms=[{'symbol':atom.symbol,
                          'position':atom.position.tolist(),
                          'tag':atom.tag,
                          'index':atom.index,
                          'charge':atom.charge,
                          'momentum':atom.momentum.tolist(),
                          'magmom':atom.magmom}
                            for atom in atoms],
                            cell=atoms.cell.tolist(),
                            pbc=atoms.pbc.tolist(),
                            info=atoms.info,
                            constraints=[c.todict() for c in atoms.constraints])
    d['natoms']=len(atoms)
    cell=atoms.get_cell()
    if cell is not None and np.linalg.det(cell) > 0:
        d['volume']=atoms.get_volume()
        
    d['mass']=sum(atoms.get_masses())
    syms=atoms.get_chemical_symbols()
    d['chemical_symbols']=list(set(syms))
    #d['spacegroup']=spglib.get_spacegroup(atoms)
    
    return d

def calc_to_dict(calc):
    # check to see if calc is espresso
    try:
       calc = calc.get_calculator()
    except:
        pass
    try:
       d = calc.todict()
    except:
        try:
            d = calc.todict_()
        except:
            raise IOError('calculator does not have todict imprementation')
    return d

def format_metadata():
    return {
        'user': getpass.getuser(),
        'time': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    }
