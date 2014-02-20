import arcpy
from arcpy.sa import *

def project_raster(raster, output_geodatabase, to_projection, from_projection, interpolation_method = 'BILINEAR'):
  output_path = output_geodatabase + '/' + raster
  arcpy.ProjectRaster_management(raster, output_path, to_projection, interpolation_method,"#","#","#",from_projection)
  return output_path

def hillshade_raster(raster, output_geodatabase):
  arcpy.CheckOutExtension('Spatial')
  output_path = output_geodatabase + '/' + raster.replace(output_geodatabase, '') + '_hs'
  arcpy.gp.HillShade_sa(raster, output_path, "315", "45", "NO_SHADOWS", "1")
  return output_path

