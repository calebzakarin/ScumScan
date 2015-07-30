
# coding: utf-8

# In[1]:

import os
from PIL import Image, ImageDraw
import csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'pylab inline')
get_ipython().magic(u'matplotlib inline')


# In[2]:

#ScumFullDF is a dataframe of the ScumScan csv file (from the identification script)
ScumFullDF = pd.DataFrame.from_csv("ScumScan.csv",header=0, index_col=0)
ScumFullDF


# The following block creates a new set of images where each object is highlighted in a grey box and referenced in a new CSV file (ScumDataOutput.csv).  If one image contains multiple objects of the same species, these are condensed into one image with each similar species highlighted.  
# 
# sppTypes is a unique list of the species typed by idNum
# immages is a unique list of the immages.
# 
# The main body loops through each image, creating a new dataframe (low_df) with only the rows that reference that particular image.  Then we attempt to pull out a dataframe of the observations which pertain to each of the species types (similarObjecsDF).  If the similarObjecsDF has at least one item, we draw a box around each observation, and export the resulting image to an "images" folder. Then each of these new images are included in a new CSV file along with the corresponding meta data (site location, date, taxonomy, ect...) 

# In[43]:

sppTypes = sorted(pd.unique(ScumFullDF.idNum.ravel()))
immages = pd.unique(ScumFullDF.url.ravel())

wr = csv.writer(open('ScumScanOutput.csv','wb'))
wr.writerow(("","siteID","measurementType","storageType","year","month","day","magnification","n","order","phylum","genus","spp","url","idNum"))
wrI = 0

print sppTypes

for image in immages:
    #DF of rows pertaining to the image
    low_df = ScumFullDF.loc[ScumFullDF.url == image]
        
    i  = 1 #skip = 0 no ID.
    while i < len(sppTypes):
        #Rows where the spp type (idNum) is a match
        similarObjecsDF = low_df.loc[low_df.idNum == sppTypes[i]]
            
        #If there are any matches, run this:
        if len(similarObjecsDF) > 0:
            im = Image.open( low_df.iloc[0]['url'])
            draw = ImageDraw.Draw(im)
                
            #Draw a box for each match    
            for row_index, row in similarObjecsDF.iterrows():
                draw.rectangle([int(row['x_min']),int(row['y_min']),int(row['x_max']),int(row['y_max'])], outline = "grey")
            #saveing
            imgPath = '_'.join((''.join((os.getcwd(),"/images/",str(low_df.iloc[0]['siteID']))), low_df.iloc[0]['measurementType'], str(low_df.iloc[0]['year']), str(low_df.iloc[0]['month']), str(low_df.iloc[0]['day']), low_df.iloc[0]['magnification'], str(i), image[-6:]))
            im.save(imgPath)
            writeingRow = (str(wrI),similarObjecsDF.iloc[0]['siteID'],similarObjecsDF.iloc[0]['measurementType'],similarObjecsDF.iloc[0]['storageType'],similarObjecsDF.iloc[0]['year'],similarObjecsDF.iloc[0]['month'],similarObjecsDF.iloc[0]['day'],similarObjecsDF.iloc[0]['magnification'],len(similarObjecsDF),similarObjecsDF.iloc[0]['order'],similarObjecsDF.iloc[0]['phylum'],similarObjecsDF.iloc[0]['genus'],similarObjecsDF.iloc[0]['spp'],imgPath,i)
            wr.writerow(writeingRow)
            wrI = wrI + 1
        i = i + 1


# In[ ]:



