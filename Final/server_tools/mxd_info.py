#import arcpy
import os
import urllib

class map_doc:
	def __init__(self):
		file_path = None
		service_path = None
		layers = []
	
	@classmethod
	def from_path_info(map_doc, path, root_path):
		result = map_doc()
		result.file_path = path
		result.service_path = _path_to_url(path, root_path)
		return result


class MapLayer:
	def __init__(self):
		index = None
		name = None
		feature_class = None

def mxd_info(root_path):
	return ''

def _get_all_files_with_ext(root, ext):
	result = []
	for (new_path, dirs, files) in os.walk(root):
		result += [ os.path.abspath(os.path.join(new_path, f)) for f in files if os.path.splitext(f)[1] == ext]
	return result

def _path_to_url(path, root_path):
	no_ext = os.path.splitext(path)[0]
	rel_path = os.path.relpath(no_ext, root_path)
	return urllib.pathname2url(rel_path)

rt_path = 'C:/users/jroebuck/projects/agdc/gis/mapservices'
map_docs = [ map_doc.from_path_info(m, rt_path) for m in _get_all_files_with_ext(rt_path, '.mxd') ]