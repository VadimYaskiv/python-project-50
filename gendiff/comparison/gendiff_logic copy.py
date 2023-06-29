from gendiff.comparison.file_parser import json_open
from gendiff.comparison.file_parser import yaml_open


def generate_diff(path1, path2):
    if '.json' in path1:
        open_file1 = json_open(path1)
    if '.json' in path2:
        open_file2 = json_open(path2)
    if '.yaml' or '.yml' in path1:
        open_file1 = yaml_open(path1)
    if '.yaml' or '.yml' in path2:
        open_file2 = yaml_open(path2)

    result = []
    dict1 = dict(sorted(open_file1.items()))
    dict2 = dict(sorted(open_file2.items()))
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            result.append(f'  {key}: {value}')
        elif key in dict2 and dict2[key] != value:
            result.append(f'- {key}: {value}\n+ {key}: {dict2[key]}')
        elif key not in dict2:
            result.append(f'- {key}: {value}')
    for key, value in dict2.items():
        if key not in dict1:
            result.append(f'+ {key}: {value}')
    result_str = '{\n' + '\n'.join(result) + '\n}'
    return result_str
