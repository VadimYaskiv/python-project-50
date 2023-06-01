import json


def generate_diff(path1, path2):

    with (open(path1, 'r') as file1,
          open(path2, 'r') as file2):
        json1 = json.load(file1)
        json2 = json.load(file2)

    result = []
    dict1 = dict(sorted(json1.items()))
    dict2 = dict(sorted(json2.items()))
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
