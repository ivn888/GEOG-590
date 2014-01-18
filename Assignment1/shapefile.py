# 2014-01 Jason Roebuck
# Product of work for GEOG 590 @ Portland State University
# May be used for whatever!
# github.com/jtroe/GEOG-590 - Fork me on github!
import arcpy
import os

shapefile = r'states_21basic\states.shp'

def main():
    for shp in AllShapefiles():
        shpDesc = arcpy.Describe(shp)
        print shpDesc.name, 'is a' ,shpDesc.shapeType
        if len(shpDesc.fields) > 6:
            print shpDesc.name,'has',str(len(shpDesc.fields)),'fields:'
            for f in shpDesc.fields:
                print f.name
        if shpDesc.shapeType == 'Polygon':
            print
            print 'Life is', shpDesc.featureType

def AllShapefiles():
    result = []
    thisDir = os.path.dirname(os.path.abspath(__file__))
    for (new_path, dirs, files) in os.walk(thisDir):
        for f in files:
            if os.path.splitext(f)[1] == '.shp':
                shapefile = os.path.join(new_path, f)
                result.append(shapefile)
    return result



if __name__ == "__main__":
    main()