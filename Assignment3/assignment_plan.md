# Assignment 3 Process Plan

1. Successfully run raster reprojection using ArcToolbox.
2. Successfully run hillshade process using ArcToolbox.
3. Export successful scripts as python snippets.
4. Test scripts again using python shell.
5. Extract out parameters as variables in order to accept them into generic methods.
6. Transform working code for each process into separate method.
7. Extract method into its own helper class.
8. Create a tester class as main method.  Hardcode test values into test class.
9. Update hardcoded values to use `argv`. Profit. :)

# Assignment 3 Pseudo-code

```py
in raster_tools.py:

import arcpy + ?

# projects a raster dataset
# inputs: source raster, an output geodatabase, to projection of your choice in arcgis stringy format, from raster source projection (could probably be retrieved programmatically), and interpolation method (with default value)
# returns output path of exported (reprojected) raster
def project_raster(raster, output geodatabase, to projection, from projection, interpolation method = 'BILINEAR')
  output_path = output_geodatabase + / + raster
  project raster (raster, output path, to_projection, interpolation_method,none,none,none,from projection)
  return output path

# takes a DEM raster and creates copy with hillshade pattern
# inputs: source raster
# requires: ArcGIS Spatial Analyst extension
# returns output path of exported raster
def hillshade_raster(raster, output geodatabase):
  checkout spatial analyst extension
  output path = output geodatabase + / + raster + _hs
  spatial analyst hillshade (raster, output path, 315, 45, False / No Shadows, 1)
  return output path


in test_project_rasters.py:

import raster tools ^^
import arcpy + ?

source workspace = parameter 0 # 'D:/Downloads/assignment-3-rasters/smaller2'
output geodatabase = parameter 1 # 'C:/Users/jroebuck/Projects/GEOG-590/Assignment3/Output.gdb'

arcpy.env.workspace = source workspace
for each raster in list rasters
projected raster = 
  raster_tools.project_raster(raster, output geodatabase,Lambert,NAD 83)
  print 'Reprojected raster as', projected raster
  hillshaded raster = raster_tools.hillshade_raster(projected raster, output geodatabase)
  print 'Hillshaded raster as', hillshaded raster
```


# Diary
- Export from toolbox... check.
- Pretty much followed the pseudo code... which is updated to reflect the final project
- The trickiest part of this assignment was figuring out how arcpy handled paths for each method: is it the full or relative.
- Running it several times was tricky because if the destination existed it bombed.  So, I could have wrote code to clear it out for me, but was either too lazy or not sufficiently lazy.