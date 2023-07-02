dict1 = {"hello": "world", "is": True, "nested": {"count": 55}, "rr": "rr", "bobr": {"hhh": 55}}

dict2 = {"hello": "wor", "is": True, "nested": {"count": 5}, "ff": "ff"}

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


print(key_state_define(dict1, dict2))

import itertools

def stringify(value, replacer='.', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - 2)
        bracket_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')            
        result = itertools.chain("{", lines, [bracket_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)

print(stringify(data))