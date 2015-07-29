# ScumScan

Max Caplow & Caleb Zakarin

The data collected in ScumScan.csv

columns

    id = unique identifier for each observation
    siteID = 
	1: 6300 Lake Balboa Hiking Trail, Lake Balboa, CA 91406, USA (34.1786177,-118.4977081)
	2:  4101-4127 Laurel Canyon Boulevard, Studio City, CA 91604, USA (34.1457431,-118.3960976)
	3: 4030-4074 Colfax Avenue, Studio City, CA 91604, USA (34.1423249,-118.387336)
	4: 48 Riverside Drive, Los Angeles, CA 90027, USA (34.1562449,-118.294331)
	5: Los Angeles River Bike Path, Glendale, CA 91201, USA (34.1558848,-118.2882568)
	6: Los Angeles River Bike Path, Los Angeles, CA 90039, USA (34.1215869,-118.2706885)
	7: Los Angeles River Greenway Trail, Los Angeles, CA 90039, USA (34.1080075,-118.2540206)
	8: 1721 North Broadway, Los Angeles, CA 90031, USA (34.0719847,-118.2248829)
   
  -measurement Type = sus1 and sus2 for suspended solids of type 1 and 2, col3 for colonial organism (listed as type 3 on the viles)
  sus# and col# are followed by the letter (a, b, or c) denoting which repeated version of the sample was tested. 
ex. sus1a, sus1b, sus1c, sus2a, ect...
    1: storageType = e or f (ethanol or formalin)
    2: year = YYYY
    3: month = MM
    4: day = DD
    5: magnification = 10x, 20x, 40x
    6: x_min= the minimum x-value of the selected area
    7: x_max = the maximum x-value of the selected area
    8: y_min= the minimum y-value of the selected area
    9: y_max= the maximum y-value of the selected area
    10: n = number of objects in the selected area (usually 1)
    11: order =
    12: phylum =
    13: genus = [NA is acceptable]
    14: spp = [NA is acceptable]
    15: url = /AlgaeFoley/YY_MM_DD_site#/measurementType/site#_storageType_sampleIteration_DD_MM_YYYY/magnification/##.bmp
    16: idNum = 0-18 (O: no id)

site# = single integer 1-8 denoting which site the sample was taken from.
storageType = ?f? for formalin, ?e? for ethanal.
*sampleIteration= the measurementType number (1,2, or 3) followed by the letter denoting which repeated iteration of the sample it is (a, b, or c).



Completed:

-Site 1, 17, Jul, 2014, sus1a
	(10x
	20x
	40x),
-Site 2, 17, Jul, 2014, sus1a
	(10x
	20x
	40x),
-Site 2, 17, Jul, 2014, sus1b
	10x
	20x
	40x
-Site 2, 17, Jul, 2014, sus1c
	10x
	20x
	40x
-Site 6, 17, Jul, 2014, sus1a
	10x
	20x
	40x
-Site 6, 17, Jul, 2014, sus1b
	10x
	20x
	40x
-Site 6, 17, Jul, 2014, sus1c
	10x
	20x
	40x
-Site 6, 17, Jul, 2014, sus2a
	10x
	20x
	40x
-Site 6, 17, Jul, 2014, sus2b
	10x
	20x
	40x
-Site 6, 17, Jul, 2014, sus2c
	10x
	20x
	40x



to re-scan: 2_f_2a_17_jul_2014

