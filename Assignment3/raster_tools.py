import arcpy
from arcpy.sa import *

# reprojects input raster to output geodatabase
# inputs: to/from projection, interpolation method (optional, default: bilinear)
# returns path to the new raster
def project_raster(raster, output_geodatabase, to_projection, from_projection, interpolation_method = 'BILINEAR'):
  output_path = output_geodatabase + '/' + raster
  arcpy.ProjectRaster_management(raster, output_path, to_projection, interpolation_method,"#","#","#",from_projection)
  return output_path

# hillshades input DEM raster, or any raster, but you probably won't like the results on something that's not elevation
# inputs: output geodatabase location
# returns path to new raster
def hillshade_raster(raster, output_geodatabase):
  arcpy.CheckOutExtension('Spatial')
  output_path = output_geodatabase + '/' + raster.replace(output_geodatabase, '') + '_hs'
  arcpy.gp.HillShade_sa(raster, output_path, "315", "45", "NO_SHADOWS", "1")
  return output_path

