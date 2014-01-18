# 2014-01 Jason Roebuck
# Product of work for GEOG 590 @ Portland State University
# May be used for whatever!
# github.com/jtroe/GEOG-590 - Fork me on github!
import arcpy
import os

def main():
    for shp in AllShapefiles():
        shpDesc = arcpy.Describe(shp)
        print shpDesc.name, 'is a' ,shpDesc.shapeType # x.shp is a Polygon/Point/etc.
        if len(shpDesc.fields) > 6:
            print shpDesc.name,'has',str(len(shpDesc.fields)),'fields:' # x.shp has n fields:
            for f in shpDesc.fields: # and they are:
                print f.name 
        if shpDesc.shapeType == 'Polygon':
            print
            print 'Life is', shpDesc.featureType # hopefully this polygon feature class is simple... since that's what I want life to be

# walks the path of this script and subdirectories to get all the shapefiles
def AllShapefiles():
    result = [] # empty list to add shapefile path string to
    thisDir = os.path.dirname(os.path.abspath(__file__))
    for (new_path, dirs, files) in os.walk(thisDir):
        for f in files:
            if os.path.splitext(f)[1] == '.shp': # if it's a shapefile...
                shapefile = os.path.join(new_path, f) # directory + filename
                result.append(shapefile)
    return result


# nerdism
if __name__ == "__main__":
    main()