#add the idNum field to a CSV
import os
from PIL import Image
import csv

def identify(idTup):
	if idTup == ("null","Chlorophyceae","null","Green algae (with flagella, small)"):
		outp = 1
	elif idTup == ("null","Chlorophyceae","null","Green algae (with flagella)"):
		outp = 2
	elif idTup == ("null","Chlorophyceae","null","Green algae (no flagella)"):
		outp = 3
	elif idTup == ("null","Gamophyceae","null","Filamentous green algae"):
		outp = 4
	elif idTup == ("null","Gamophyceae","null","Desmids"):
		outp = 5
	elif idTup == ("null","Bacillariophyceae","null","Diatoms"):
		outp = 6
	elif idTup == ("null","Zoomastigophora","null","Flagellates"):
		outp = 7
	elif idTup == ("Amoebina","Sacrodina","null","Amoeba"):
		outp = 8
	elif idTup == ("Testacea","Sacrodina","null","Shelled Amoeba"):
		outp = 9
	elif idTup == ("Heliozoea","Sacrodina","null","Heliozoans"):
		outp = 10
	elif idTup == ("Peritrichida","Ciliophora","null","Ciliates Peritrich"):
		outp = 11
	elif idTup == ("Eridogenida","Ciliophora","null","Ciliates Suctoria"):
		outp = 12
	elif idTup == ("Oliogohymenophorea","Ciliophora","null","Ciliates Paramecium"):
		outp = 13
	elif idTup == ("Heterotrichea","Ciliophora","null","Ciliates Stentor"):
		outp = 14
	elif idTup == ("Prostomatea","Ciliophora","null","Ciliates Coleps"):
		outp = 15
	elif idTup == ("null","null","null","Blue-green algae (cyanobacteria)"):
		outp = 16
	elif idTup == ("null","Euglenida","null","Euglenoids"):
		outp = 17
	elif idTup == ("null","Dinoflagellate","null","Dinoflagellates"):
		outp = 18
	elif idTup == ("null","Rotifer","null","Rotifers"):
		outp = 19
	elif idTup == ("null","Cnidaria","null","Hydra"):
		outp = 20
	elif idTup == ("null","Platyhelminthes","null","Flatworms"):
		outp = 21
	else:
		outp = 0
	return outp

r = csv.reader(open("ScumScan.csv", 'rU'))
wr = csv.writer(open('ScumScanAdded.csv','wb'))
wr.writerow(("","siteID","measurementType","storageType","year","month","day","magnification","x_min","x_max","y_min","y_max","n","order","phylum","genus","spp","url"))

for row in r:
	#tup = (row[13],row[14],row[15],row[15])
	#print tup
	tup = ("Heterotrichea","Ciliophora","null","Ciliates Stentor")
	#print tup
	#print (row[13],row[14],row[15],row[15])
	rowAdd = row.append(identify((row[13],row[14],row[15],row[16])))
	
	wr.writerow(row)
