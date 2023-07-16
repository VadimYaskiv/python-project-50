dict_ = {'common': {'follow': {'status': 'added', 'second_val': False}, 'setting1': {'status': 'unchanged', 'first_val': 'Value 1'}, 'setting2': {'status': 'deleted', 'first_val': 200}, 'setting3': {'status': 'changed', 'first_val': True, 'second_val': None}, 'setting4': {'status': 'added', 'second_val': 'blah blah'}, 'setting5': {'status': 'added', 'second_val': {'key5': 'value5'}}, 'setting6': {'doge': {'wow': {'status': 'changed', 'first_val': '', 'second_val': 'so much'}}, 'key': {'status': 'unchanged', 'first_val': 'value'}, 'ops': {'status': 'added', 'second_val': 'vops'}}}, 
'group1': 
    {'baz': 
        {'status': 'changed', 'first_val': 'bas', 'second_val': 'bars'}, 
    'foo': 
        {'status': 'unchanged', 'first_val': 'bar'}, 
    'nest':
        {'status': 'changed', 'first_val': {'key': 'value'}, 'second_val': 'str'}}, 
'group2': 
{'status': 'deleted', 'first_val': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'status': 'added', 'second_val': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}

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

def stringify(value):
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

print(stringify(dict_))


