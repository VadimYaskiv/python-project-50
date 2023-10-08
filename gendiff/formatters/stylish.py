

# unpack dictionaries that are in 'first_val' and 'second_val'
# and don't have 'status' because 'status' is defined
# for the dictionary at the level above
# (which has the keys 'first_val' and 'second_val')



# define the signs for keys according to the 'status'
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


def stylish(dict, replacer='  ', depth=1):
        line = []
        replacer = str(replacer)
        indent = str(replacer * depth)
        for key, val in dict.items():
            if val['status'] == 'nested':
                line.append(indent + replacer + str(key) + ': {' + '\n')
                line.append(stylish(val['value'], replacer, depth + 2))
                line.append(replacer * (depth + 1) + '}' + '\n')
            elif val['status'] == 'changed':
                line.append(indent + '- ' + str(key) + ': ' + 
                            str(unpack(val['first_val'], replacer, depth + 2)) + '\n')
                line.append(indent + '+ ' + str(key) + ': ' + 
                            str(unpack(val['second_val'], replacer, depth + 2)) + '\n')
            else:
                line.append(indent + SIGN[val['status']] + str(key) + ': ' + str(unpack(val['value'], replacer, depth + 2)) + '\n')
        result = ''.join(line)
        return result

# recursively unpack internal dictionary (with parameters of keys)
# and call еру function to define the signs

def stringify_s(internal_dict):
    rez = '{' + '\n' + stylish(internal_dict) + '}'
    return rez

