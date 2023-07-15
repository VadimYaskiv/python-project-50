def signer(val):
    rez_list = ''
    if val['status'] == 'added':
        val_loc = val['second_val']
        rez_list = (f"was added with value: {val_loc}")
    elif val['status'] == 'deleted':
        rez_list = (f'was removed')
    elif val['status'] == 'changed':
        val_loc1 = val['first_val'] 
        val_loc2 = val['second_val']
        rez_list = (f'was updated. From {val_loc1} to {val_loc2}')
    return rez_list

def stringify_p(value):
    def iter_(current_value, path):
        lines = []
        for key, val in current_value.items():
            if 'status' in val:
                lin = signer(val)
                lines.append(f"Property {'.'.join(path)}.{key} {lin}")
            else:
                path.append(key)
                lines.append(f"{iter_(val, path)}")
        return '\n'.join(lines)
    return iter_(value, [])
