import arcpy
import json
import os
import os.path
import urllib
from helper import get_all_files
from helper import obj_to_json

class map_service:
	def __init__(self):
		file_path = None
		service_path = None
		layers = []
	
	@classmethod
	def from_path_info(map_doc, path, root_path):
		result = map_doc()
		result.file_path = path
		result.service_path = _path_to_url(path, root_path)
		result.layers = _get_layer_infos(path)
		return result
		
	def to_json(self):
		return obj_to_json(self)

class map_layer:
	def __init__(self):
		index = None
		name = None
		feature_class = None
	
	@classmethod
	def group_layer(index, name):
		result = map_layer()
		result.index = index
		result.name = name
		return result

	def __str__(self):
		return str(name)
	
	def to_json(self):
		return obj_to_json(self)

def _path_to_url(path, root_path):
	no_ext = os.path.splitext(path)[0]
	rel_path = os.path.relpath(no_ext, root_path)
	return urllib.pathname2url(rel_path)

def _get_layer_infos(mxd_path):
	layer_infos = { }
	map_doc = arcpy.mapping.MapDocument(mxd_path)
	print mxd_path
	for i, layer in enumerate(arcpy.mapping.ListLayers(map_doc)):
		if layer.supports('dataSource'):
			if layer.isGroupLayer: # annotation
				for j, anno_layer in enumerate(layer):
					anno_idx = i + j + 1
					layer_infos[anno_idx] = _get_layer_info(anno_layer, anno_idx)
			else: # feature or raster layer
				layer_infos[i] = _get_layer_info(layer, i)
		else: # group layer
			layer_infos[i] = layer.name
	return layer_infos

def _get_layer_info(layer, index):
	layer_info = map_layer()
	layer_info.index = index
	layer_info.name = layer.name
	layer_info.feature_class = os.path.basename(layer.dataSource)
	return layer_info

if __name__ == '__main__':
	rt_path = sys.argv[-1]
	#rt_path = 'C:/users/jroebuck/projects/agdc/gis/mapservices'
	map_services = [ map_service.from_path_info(mxd, rt_path) for mxd in get_all_files(rt_path, '.mxd') ]
	map_services_json = obj_to_json(map_services)
	with open('map_services.json','w') as txt_out:
		txt_out.write(map_services_json)