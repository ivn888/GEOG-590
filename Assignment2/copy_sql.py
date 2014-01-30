# ExtactFeaturesByLocationAndAttribute.py
# Description: Extract features to a new feature class based on a Location and an attribute query
# Requirements: Python and the Python win32all extension
# Author: ESRI
# Data 1/1/2004
# modified from the above 10/1/2004 by percy
#updated to ArcMap10 January 2012
# modified to work on a directory of shapefiles => geodatabase by jtroe 1/30/14
# github.com/jtroe/GEOG-590

# Create the Geoprocessor
import arcpy
import os

# fake-out argv for testing
# argv = ['hydro_data','hydro_data.gdb', '"CFF1" IN (402, 410, 428)', True]
# source workspace, destination workspace, where clause, overwrite output?

scriptPath = os.path.dirname(os.path.realpath(__file__))
outWorkspacePath = os.path.join(scriptPath, argv[1])

arcpy.env.workspace = os.path.join(scriptPath, argv[0])
arcpy.env.overwriteOutput = argv[3]

# Put in error trapping in case an error occurs when running tool
try:
    # create geodatabase if it doesn't exist
    if not os.path.exists(outWorkspacePath):
        arcpy.CreateFileGDB_management(scriptPath, argv[1])

    # copy the features using specified where clause
    for fc in arcpy.ListFeatureClasses():
        outputFcName = os.path.splitext(fc)[0]
        outputFcName = arcpy.ValidateTableName(outputFcName, outWorkspacePath)
        print 'processing', outputFcName
        arcpy.FeatureClassToFeatureClass_conversion(fc, outWorkspacePath, outputFcName, argv[2])

    print 'Success!!'
except:
    # If an error occured print the message to the screen
    print arcpy.GetMessages()
