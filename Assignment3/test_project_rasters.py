import raster_tools
import arcpy


source_workspace = 'D:/Downloads/assignment-3-rasters/smaller2'#arcpy.GetParameterAsText(0)
output_geodatabase = 'C:/Users/jroebuck/Projects/GEOG-590/Assignment3/Output.gdb'#arcpy.GetParameterAsText(1)

arcpy.env.workspace = source_workspace
for raster in arcpy.ListRasters():
  projected_raster = raster_tools.project_raster(raster, output_geodatabase,
	"PROJCS['North_America_Lambert_Conformal_Conic',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-96.0],PARAMETER['Standard_Parallel_1',20.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Latitude_Of_Origin',40.0],UNIT['Meter',1.0]]",
	"GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
  )
  print 'Reprojected raster as', projected_raster
  hillshaded_raster = raster_tools.hillshade_raster(projected_raster, output_geodatabase)
  print 'Hillshaded raster as', hillshaded_raster