def compare_dict(dict1, dict2):
    result = []
    dict1 = dict(sorted(dict1.items()))
    dict2 = dict(sorted(dict2.items()))
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
