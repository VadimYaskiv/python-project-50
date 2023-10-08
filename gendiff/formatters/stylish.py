# unpack values that ara dictionaries or return value
def unpack(value, replacer, depth):
    if isinstance(value, dict):
        line = ['{']
        for key, val in value.items():
            line.append('\n' + replacer * depth + replacer + str(key)
                        + ': ' + str(unpack(val, replacer, depth + 2)))
        line.append('\n' + str(replacer * (depth - 1)) + '}')
        result = ''.join(line)
        return result
    else:
        return value


SIGN = {
    'unchanged': '  ',
    'added': '+ ',
    'deleted': '- '
}


# recursively unpack internal dictionary (with parameters of keys)
# define the signs (higest level) depending on the type
# and form the lines of the final file
def stylish(dict, replacer='  ', depth=1):
    line = []
    replacer = str(replacer)
    indent = str(replacer * depth)
    for key, val in dict.items():
        if val['type'] == 'nested':
            line.append(indent + replacer + str(key) + ': {' + '\n')
            line.append(stylish(val['value'], replacer, depth + 2))
            line.append(replacer * (depth + 1) + '}' + '\n')
        elif val['type'] == 'changed':
            line.append(indent + '- ' + str(key) + ': ' +
                        str(unpack(val['first_val'], replacer, depth + 2))
                        + '\n')
            line.append(indent + '+ ' + str(key) + ': ' +
                        str(unpack(val['second_val'], replacer, depth + 2))
                        + '\n')
        else:
            line.append(indent + SIGN[val['type']] + str(key)
                        + ': ' + str(unpack(val['value'], replacer, depth + 2))
                        + '\n')
    result = ''.join(line)
    return result


def stringify_s(internal_dict):
    rez = '{' + '\n' + stylish(internal_dict) + '}'
    return rez
