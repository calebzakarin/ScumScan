
# coding: utf-8

# This is based on the python flickr api: http://stuvel.eu/media/flickrapi-docs/documentation/
# 

# In[59]:

import flickrapi
import os
import fileinput
import xml
import csv


api_key = '' #removed for security
api_secret = '' #removed for security

flickr = flickrapi.FlickrAPI(api_key, api_secret)
flickr.authenticate_via_browser(perms='write')


# flickr user id for the MCScumScan account (just for future reference): '134053962@N08'
# 
# we use 'r' as the CSV reader for the ScumScanOutput.csv file produced by the FIndingSimilarObjects script.
# 
# The 'for' loop goes through each row of this file. We use the flickr.upload command with the location of the image file (row[13]). This will also produce an XML variable containing the photo id. We save this as 'flickrID'.
# 
# Next we append the row with this flickr id, and save it to a new CSV file, 'ScumScanFlickr.csv'.
# 
# In order to save the flickrIDs as the script runs, so that if uploading fails we don't have to start over, we use a list variable, 'listdata', to store the data from the CSV, and then the writerows command with 'listdata' as input.

# In[74]:

r = csv.reader(open("ScumScanOutput.csv", 'rU'))

listdata = [['','siteID','measurementType','storageType','year','month','day','magnification','n','order','phylum','genus','spp','url','idNum','flickrID']]

#r2 = csv.reader(open('ScumScanFlickr.csv','rU'))
#listdata = [l for l in r2]

#if the program hangs on uploading, uncomment the above lines and comment our the 'listdata = [l for l in r2]'. 
#then change 0 in 'if i > 0:' for the index of the image to start with.
i = 0
for row in r:
    if i > 0:
        flickrID = flickr.upload(row[13])
        row.append(str(flickrID[0].text))
        print row
        listdata.append(row)
        wr = csv.writer(open('ScumScanFlickr.csv','wb'))
        wr.writerows(listdata)
    i = i + 1


# In[ ]:



