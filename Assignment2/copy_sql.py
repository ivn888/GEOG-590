# ExtactFeaturesByLocationAndAttribute.py
# Description: Extract features to a new feature class based on a Location and an attribute query
# Requirements: Python and the Python win32all extension
# Author: ESRI
# Data 1/1/2004
# modified from the above 10/1/2004 by percy
#updated to ArcMap10 January 2012

# Create the Geoprocessor
import arcpy

# fake-out argv for testing
# argv = ['c:/temp/percy/San_Diego/majorrds.shp','c:/temp/percy/', 'bigrds.shp', "\"CLASS\" = '1' or \"CLASS\" = '2'", True]
# source feature class, destination workspace, destination feature class, where clause, overwrite output?

arcpy.env.overwriteOutput = argv[4]

# Put in error trapping in case an error occurs when running tool
try:
    # copy just the features that have class 1
    arcpy.FeatureClassToFeatureClass_conversion(argv[0], argv[1], argv[2], argv[3])
except:
    # If an error occured print the message to the screen
    print arcpy.GetMessages()
