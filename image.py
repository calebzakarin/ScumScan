import os
from PIL import Image
import csv

r = csv.reader(open("ScumScan.csv"))
ScumWorkingData = [l for l in r]
#ScumWorkingData is a list of the data loaded from the CSV that can manipulated, then later saved in full

#Displays the croped version of the image. May require XV on non-mac opperating systems. Takes the full path and pixel extermities as input.
def display(imgPath, x_min, y_min, x_max, y_max):

	im = Image.open(imgPath)
	im.crop((x_min, y_min, x_max, y_max)).show()

#Definitions for taxonomy. Taken from http://www.msnucleus.org/watersheds/mission/plankton.pdf and number in order.
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

#ask for a starting row so that you don't need to start from the top each time.
startingRow = input("what row would you like to start with?  ")

#When doContinue is set to false, the program will terminate.
doContinue = True 

#counter + startingRow will always be the current row.
counter = 0

while doContinue:
	curRow = startingRow + counter

	#Checking to make sure at least 1 field in the taxonomy section is blank, otherwise the row is skipped.
	if str(ScumWorkingData[curRow][13]) == "" or str(ScumWorkingData[curRow][14]) == "" or str(ScumWorkingData[curRow][15]) == "" or str(ScumWorkingData[curRow][16]) == "":

		#shows inmage to user.
		display(ScumWorkingData[curRow][17],int(ScumWorkingData[curRow][8]),int(ScumWorkingData[curRow][10]),int(ScumWorkingData[curRow][9]),int(ScumWorkingData[curRow][11]))

		#askes if user recognises image. if not, the next image is shown
		doesRecognize = raw_input("do you recognize this object? (y/n) ")


		if doesRecognize != "n":

			#asks for an idenification from the PDF file, otherwise goes to manual input.
			databaseNumber = input("Can you identify the entry on the key? (1-?, or n)")
			if databaseNumber != "n":
				identity = identify(databaseNumber)
				#update ScumWorkingData with the retunred values from hte identity function.
				ScumWorkingData[curRow][13] = identity[0]
				ScumWorkingData[curRow][14] = identity[1]
				ScumWorkingData[curRow][15] = identity[2]
				ScumWorkingData[curRow][16] = identity[3]
				

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

		#makes sure user wants to continue.			
		if str(raw_input('continue? (y/n)  ')) == 'n':
			doContinue = False

	counter = counter + 1

	#Writes updated ScumWorkingData to new CSV.
	wr = csv.writer(open('ScumScanOutput.csv','wb'))
	wr.writerows(ScumWorkingData)
print "Thank you! You saw ", counter, " rows!"
