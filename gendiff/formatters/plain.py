def adapt(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def signer(val):
    rez_list = ''
    if val['status'] == 'added':
        val_loc = adapt(val['second_val'])
        rez_list = (f"was added with value: {val_loc}")
    elif val['status'] == 'deleted':
        rez_list = (f'was removed')
    elif val['status'] == 'changed':
        val_loc1 = adapt(val['first_val']) 
        val_loc2 = adapt(val['second_val'])
        rez_list = (f'was updated. From {val_loc1} to {val_loc2}')
    return rez_list

def stringify_p(value):
    def iter_(current_value, path):
        lines = []
        for key, val in current_value.items():
            if val.get('status') == 'unchanged':
                continue
            elif 'status' in val and val.get('status') != 'unchanged':
                lin = signer(val)
                path.append(key)
                lines.append(f"Property '{'.'.join(path)}' {lin}")
                path.pop()
            else:
                path.append(key)
                lines.append(f"{iter_(val, path)}")
                path.pop()
        return '\n'.join(lines)
    return iter_(value, [])
