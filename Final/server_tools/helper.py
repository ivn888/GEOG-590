import os
import copy
import json

def get_all_files(root, ext=None):
    result = []
    for (new_path, dirs, files) in os.walk(root):
        result += [ os.path.abspath(os.path.join(new_path, f)) for f in files if ext is None or os.path.splitext(f)[1] == ext]
    return result

def obj_to_deep_dict(obj, classkey=None):
    if isinstance(obj, dict):
        for k in obj.keys():
            obj[k] = obj_to_deep_dict(obj[k], classkey)
        return obj
    elif hasattr(obj, "__iter__"):
        return [obj_to_deep_dict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, obj_to_deep_dict(value, classkey)) 
            for key, value in obj.__dict__.iteritems() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj
    
def obj_to_json(obj):
    return json.dumps(obj_to_deep_dict(obj))