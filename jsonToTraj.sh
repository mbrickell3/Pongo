#!/bin/bash

cp json_to_atoms.py json/
cp utilities.py json/
cd json/
mkdir traj/
for i in *.json
do
	echo $(basename "$i")
	python json_to_atoms.py "$i"
done
rm json_to_atoms.py
rm utilities.py

cd ..
mv json/traj/ . 
