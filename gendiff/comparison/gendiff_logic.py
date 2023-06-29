from gendiff.comparison.file_parser import json_open
from gendiff.comparison.file_parser import yaml_open
from gendiff.comparison.stylish import stringify

# define the keys states
def key_state_define(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    keys = sorted(keys)
    
    rez = {}
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            key_mod = f'  {key}'
            rez[key_mod] = key_state_define(value1, value2)
        elif key not in dict1:
            key_mod = f'+ {key}'
            val_mod = dict2[key]
            rez[key_mod] = val_mod
        elif key not in dict2:
            key_mod = f'- {key}'
            val_mod = dict1[key]
            rez[key_mod] = val_mod
        elif dict1[key] == dict2[key]:
            key_mod = f'  {key}'
            val_mod = dict1[key]
            rez[key_mod] = val_mod
        elif dict1[key] != dict2[key]:
            key_mod1 = f'- {key}'
            val_mod1 = dict1[key]
            rez[key_mod1] = val_mod1
            key_mod2 = f'+ {key}'
            val_mod2 = dict2[key]
            rez[key_mod2] = val_mod2
    return rez

# read files as dictionaries and define their keys states
def generate_diff(path1, path2):
    if '.json' in path1:
        open_file1 = json_open(path1)
    if '.json' in path2:
        open_file2 = json_open(path2)
    if '.yaml' or '.yml' in path1:
        open_file1 = yaml_open(path1)
    if '.yaml' or '.yml' in path2:
        open_file2 = yaml_open(path2)
    dict1 = dict(sorted(open_file1.items()))
    dict2 = dict(sorted(open_file2.items()))  
    internal_dict = key_state_define(dict1, dict2)
    string_represent = stringify(internal_dict)
    print(string_represent)
    return string_represent
