from gendiff.comparison.file_parser import json_open
from gendiff.comparison.file_parser import yaml_open
from gendiff.formatters.stylish import stringify_s
from gendiff.formatters.plain import stringify_p
from gendiff.formatters.json import stringify_j


# define the keys states
def key_state_define(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    keys = sorted(keys)
    rez = {}
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            rez[key] = key_state_define(value1, value2)
        elif key not in dict1:
            key_dict = {}
            key_dict['status'] = 'added'
            key_dict['second_val'] = value2
            rez[key] = key_dict
        elif key not in dict2:
            key_dict = {}
            key_dict['status'] = 'deleted'
            key_dict['first_val'] = value1
            rez[key] = key_dict
        elif dict1[key] == dict2[key]:
            key_dict = {}
            key_dict['status'] = 'unchanged'
            key_dict['first_val'] = value1
            rez[key] = key_dict
        elif dict1[key] != dict2[key]:
            key_dict = {}
            key_dict['status'] = 'changed'
            key_dict['first_val'] = value1
            key_dict['second_val'] = value2
            rez[key] = key_dict
    return rez


# read files as dictionaries,
# call the function to create an internal dictionary 
# with the identified parameters of the keys,
# call the formatter
def generate_diff(path1, path2, format):
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
    if format == 'stylish':
        string_represent = stringify_s(internal_dict)        
    elif format == 'plain':
        string_represent = stringify_p(internal_dict)
    elif format == 'json':
        string_represent = stringify_j(internal_dict)
    return string_represent
