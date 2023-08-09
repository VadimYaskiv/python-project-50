import itertools


# unpack dictionaries that are in 'first_val' and 'second_val'
# and don't have 'status' because 'status' is defined
# for the dictionary at the level above
# (which has the keys 'first_val' and 'second_val')
def unpack(val, depth):
    rez = []
    deep_indent_size = depth + 4
    deep_indent = ' ' * deep_indent_size
    bracket_indent = ' ' * depth
    if isinstance(val, dict):
        for key, val in val.items():
            rez.append(
                f'{deep_indent}{key}: '
                f'{unpack(val, deep_indent_size)}'
            )
            result = itertools.chain("{", rez, [bracket_indent + "}"])
    else:
        if val is True or val is False:
            val = str(val).lower()
            rez.append(val)
        elif val is None:
            val = 'null'
            rez.append(val)
        else:
            rez.append(f'{val}')
        result = itertools.chain(rez)
    return '\n'.join(result)


# define the signs for keys according to the 'status'
def signer(key, val, depth):
    rez_list = ''
    deep_indent_size = depth
    deep_indent = ' ' * (deep_indent_size - 2)
    if val['status'] == 'added':
        val_loc = unpack(val['second_val'], deep_indent_size)
        rez_list = (f'{deep_indent}+ {key}: {val_loc}')
    elif val['status'] == 'deleted':
        val_loc = unpack(val['first_val'], deep_indent_size)
        rez_list = (f'{deep_indent}- {key}: {val_loc}')
    elif val['status'] == 'unchanged':
        val_loc = unpack(val['first_val'], deep_indent_size)
        rez_list = (f'{deep_indent}  {key}: {val_loc}')
    elif val['status'] == 'changed':
        val_loc1 = unpack(val['first_val'], deep_indent_size)
        val_loc2 = unpack(val['second_val'], deep_indent_size)
        rez_list = (f'{deep_indent}- {key}: '
                    f'{val_loc1}\n{deep_indent}+ {key}: {val_loc2}')
    return rez_list


# recursively unpack internal dictionary (with parameters of keys)
# and call еру function to define the signs
def stringify_s(value, replacer=' '):
    def iter_(current_value, depth):
        lines = []
        deep_indent_size = depth + 4
        first_indent = replacer * deep_indent_size
        bracket_indent = replacer * depth
        for key, val in current_value.items():
            if 'status' in val:
                lin = signer(key, val, deep_indent_size)
                lines.append(f'{lin}')
            else:
                lines.append(f'{first_indent}{key}: '
                             f'{iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [bracket_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
