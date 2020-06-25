#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------



import ogr
import pandas as pd

#Getting the shapefile
datasource = ogr.Open('.../countries.shp')
layer = datasource.GetLayerByIndex(0)

#Visualizing the number of features in it
print("Number of Features : {}".format(layer.GetFeatureCount()))

#creating a list for the fields in the attribute table
schema = []
ldefn = layer.GetLayerDefn()
for n in range(ldefn.GetFieldCount()):
    fdefn = ldefn.GetFieldDefn(n)
    schema.append(fdefn.name)
print (schema)

#indexing the list as a pandas series
series = pd.Series(schema)

#OGR needs us to reset in order to start reading from the top
layer.ResetReading()

#creating a panda series with the  names of the countries in the shapefile
#number 17 is the index of the field "NAME"that countains the countries' names
for feature in layer:
    countries = pd.Series(feature.GetFieldAsString(17))
    print (countries)

