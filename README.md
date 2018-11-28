 Pongo
 
 Pongo is a tool used be the Medford Group at the Georgia Institute of Technology. The purpose of this repository is to:
 	1) convert a pckl file to a json file
	2) insert a json file or group of json files into a MongoDB database
	3) query all json objects from a MongoDB database and create traj objects
	4) If you run into the problem where it looks like there are carriage returns on the bash scripts run the following command:
		dos2unix bash.sh

 Preface:
 	To use any of these scripts and functions please make sure you have python, ase, and pymatgen installed

 Part 1: Convert a pckl file to a json file
 	Run the bash script pcklToJson.sh with the argument of your pckl file
	Example:
	./pcklToJson.sh medford.pckl

	This will create a json object for every object in the pckl file and place it in the directory pckl_json
	TODO:
	    Put more explanation of what this does

Part 2: Insert a json file or group of json files into a MongoDB database
	Beforehands:
		a) Make sure your json file(s) is located in a directory called json
		b) In the function get_Client_Uri() in the mongo.py file, replace the default url with the url of your MongoDB database
		c) Make sure your Mongo Server is running
	
	Run the bash script jsonToMongo.sh to insert all json objects located in the json/ directory into your MongoDB database
	./jsonToMongo.sh

Part 3: Query all json objects from a MongoDB database
	Beforehands:
		a) In the function get_Client_Uri() in the mongo.py file, replace the default url with the url of your MongoDB database
		b) Make sure your Mongo Server is running
	To grab all json objects from a MongoDB database, run the script mongoToJson.sh
	Example:
	./mongoToJson.sh

	This will grab all json objects from a MongoDB database and place them in a directory mongo_json/
	
	TODO
		- enable more querying abilities

Part 4: Create traj objects from json ones
	Beforehands:
		a) Make sure all of your json file(s) are located in a directory called json
	
	Run the bash script jsonToTraj.sh to convert all json objects located in the json/ directory into traj objects and place them into the traj/ directory
	./jsonToTraj.sh

