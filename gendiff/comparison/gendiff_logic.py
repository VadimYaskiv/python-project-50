from gendiff.comparison.parser import get_data
from gendiff.comparison.parser import get_extent
from gendiff.comparison.parser import parse
from gendiff.formatters.stylish import stringify_s
from gendiff.formatters.plain import stringify_p
from gendiff.formatters.json import stringify_j


# define the keys states
def key_state_define(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    rez = {}
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            rez[key] = key_state_define(value1, value2)
        elif key not in dict1:
            rez[key] = {'status': 'added',
                        'second_val': dict2[key]}
        elif key not in dict2:
            rez[key] = {'status': 'deleted',
                        'first_val': dict1[key]}
        elif dict1[key] == dict2[key]:
            rez[key] = {'status': 'unchanged',
                        'first_val': dict1[key]}
        elif dict1[key] != dict2[key]:
            rez[key] = {'status': 'changed',
                        'first_val': dict1[key],
                        'second_val': dict2[key]}
    return rez


# read files as dictionaries,
# call the function to create an internal dictionary
# with the identified parameters of the keys,
# call the formatter
def generate_diff(path1, path2, format='stylish'):
    data1 = get_data(path1)
    data2 = get_data(path2)
    exten1 = get_extent(path1)
    exten2 = get_extent(path2)
    file1 = parse(data1, exten1)
    file2 = parse(data2, exten2)

    dict1 = dict(sorted(file1.items()))
    dict2 = dict(sorted(file2.items()))
    internal_dict = key_state_define(dict1, dict2)
    if format == 'stylish':
        string_represent = stringify_s(internal_dict)
    elif format == 'plain':
        string_represent = stringify_p(internal_dict)
    elif format == 'json':
        string_represent = stringify_j(internal_dict)
    return string_represent
