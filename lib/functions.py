"""Generic functions for MacGiver maze game."""

from os import listdir
from os.path import isfile, join
import json

def load_files(path):
    """Make list of all files in a directory."""              
    files_list = [f for f in listdir(path) if isfile(join(path, f))]
    return files_list

def string_json(path):
    """Read a .json and return a dictionary."""
    with open(path) as json_data:            
        data_dict = json.load(json_data)
        return data_dict

dict_ = {}
def name_inc(name,n, value):
    """Create dictionary with key name increment."""
    dict_[name+str(n)] = value
    return dict_