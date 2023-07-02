


import itertools

def signer(key, val):
    rez_list = ''
    if val['status'] == 'added':
        val_loc = val['second_val']
        rez_list = (f'+ {key}: {val_loc}')
    elif val['status'] == 'deleted':
        val_loc = val['first_val']
        rez_list = (f'- {key}: {val_loc}')
    elif val['status'] == 'unchanged':
        val_loc = val['first_val']
        rez_list = (f'  {key}: {val_loc}')
    elif val['status'] == 'changed':
        val_loc1 = val['first_val']
        val_loc2 = val['second_val']
        rez_list = (f'- {key}: {val_loc1}\n+ {key}: {val_loc2}')
    return rez_list

def stringify(value, replacer='.', spaces_count=4):
    lines = []
    for key, val in value.items():
         if 'status' in val:
             lin = signer(key, val)
             lines.append(lin)
         else:
            vald = stringify(val)
            lines.append(f'{key}: {vald}')
       
    return '\n'.join(lines)

