#!/bin/bash

cp mongo.py json/
cp utilities.py json/
cd json/
for i in *.json
do
	echo $(basename "$i")
	python mongo.py "$i"
done
rm mongo.py
rm utilities.py

cd ..

