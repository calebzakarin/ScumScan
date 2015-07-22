import os
from PIL import Image
import csv

r = csv.reader(open("ScumScan.csv"))
ScumWorkingData = [l for l in r]

wr = csv.writer(open('ScumScanOutput.csv','wb'))

def display(imgPath, x_min, y_min, x_max, y_max):

	im = Image.open(imgPath)
	#print im.format, im.size, im.mode
	im.crop((x_min, y_min, x_max, y_max)).show()

def identify(idNum):
	if idNum == 1:
		outp = ("null","Chlorophyceae","null","Green algae (with flagella, small)")
	elif idNum == 2:
		outp = ("null","Chlorophyceae","null","Green algae (with flagella)")
	elif idNum == 3:
		outp = ("null","Chlorophyceae","null","Green algae (no flagella)")
	elif idNum == 4:
		outp = ("null","Gamophyceae","null","Filamentous green algae")
	elif idNum == 5:
		outp = ("null","Gamophyceae","null","Desmids")
	elif idNum == 6:
		outp = ("null","Bacillariophyceae","null","Diatoms")
	elif idNum == 7:
		outp = ("null","Zoomastigophora","null","Flagellates")
	elif idNum == 8:
		outp = ("Amoebina","Sacrodina","null","Amoeba")
	elif idNum == 9:
		outp = ("Testacea","Sacrodina","null","Shelled Amoeba")
	elif idNum == 10:
		outp = ("Heliozoea","Sacrodina","null","Heliozoans")
	elif idNum == 11:
		outp = ("Peritrichida","Ciliophora","null","Ciliates Peritrich")
	elif idNum == 12:
		outp = ("Eridogenida","Ciliophora","null","Ciliates Suctoria")
	elif idNum == 13:
		outp = ("Oliogohymenophorea","Ciliophora","null","Ciliates Paramecium")
	elif idNum == 14:
		outp = ("Heterotrichea","Ciliophora","null","Ciliates Stentor")
	elif idNum == 15:
		outp = ("Prostomatea","Ciliophora","null","Ciliates Coleps")
	elif idNum == 16:
		outp = ("null","null","null","Blue-green algae (cyanobacteria)")
	elif idNum == 17:
		outp = ("null","Euglenida","null","Euglenoids")
	elif idNum == 18:
		outp = ("null","Dinoflagellate","null","Dinoflagellates")
	elif idNum == 19:
		outp = ("null","Rotifer","null","Rotifers")
	elif idNum == 20:
		outp = ("null","Cnidaria","null","Hydra")
	elif idNum == 21:
		outp = ("null","Platyhelminthes","null","Flatworms")
	return outp


startingRow = input("what row would you like to start with?  ")
doContinue = True 
counter = 0
while doContinue:
	curRow = startingRow + counter
	if str(ScumWorkingData[curRow][13]) == "" or str(ScumWorkingData[curRow][14]) == "" or str(ScumWorkingData[curRow][15]) == "" or str(ScumWorkingData[curRow][16]) == "":

		display(ScumWorkingData[curRow][17],int(ScumWorkingData[curRow][8]),int(ScumWorkingData[curRow][10]),int(ScumWorkingData[curRow][9]),int(ScumWorkingData[curRow][11]))

		doesRecognize = raw_input("do you recognize this object? (y/n) ")


		if doesRecognize == "y":
			databaseNumber = input("Can you identify the entry on the key? (1-?, or n)")
			if databaseNumber != "n":
				identity = identify(databaseNumber)
				print identity[0]
				ScumWorkingData[curRow][13] = identity[0]
				ScumWorkingData[curRow][14] = identity[1]
				ScumWorkingData[curRow][15] = identity[2]
				ScumWorkingData[curRow][16] = identity[3]
				
				#(ScumWorkingData[curRow][13], ScumWorkingData[curRow][14], ScumWorkingData[curRow][15], ScumWorkingData[curRow][16]) = identify(databaseNumber)

			else:	
				order = raw_input("order? ")
				phylum = raw_input("phylum? ")
				genus = raw_input("genus? ")
				spp = raw_input("species? ")
				if order != "":
					ScumWorkingData[curRow][13] = order
				if phylum != "":
					ScumWorkingData[curRow][14] = phylum
				if genus != "":
					ScumWorkingData[curRow][15] = genus
				if spp != "":
					ScumWorkingData[curRow][16] = spp

		if str(raw_input('continue? (y/n)  ')) == 'n':
			doContinue = False

	counter = counter + 1
print "Thank you! You saw ", counter, " rows!"
wr.writerows(ScumWorkingData)