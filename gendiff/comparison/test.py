dict1 = {"hello": "world", "is": True, "nested": {"count": 55}, "rr": "rr"}

dict2 = {"hello": "wor", "is": True, "nested": {"count": 5}, "ff": "ff"}

def key_state_define(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    rez = {}
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            rez[key] = key_state_define(value1, value2)
        elif key not in dict1:
            key_mod = f'+ {key}'
            val_mod = dict2[key]
            rez[key_mod] = val_mod
        elif key not in dict2:
            key_mod = f'- {key}'
            val_mod = dict1[key]
            rez[key_mod] = val_mod
        elif dict1[key] == dict2[key]:
            key_mod = f'  {key}'
            val_mod = dict1[key]
            rez[key_mod] = val_mod
        elif dict1[key] != dict2[key]:
            key_mod1 = f'- {key}'
            val_mod1 = dict1[key]
            rez[key_mod1] = val_mod1
            key_mod2 = f'+ {key}'
            val_mod2 = dict1[key]
            rez[key_mod2] = val_mod2
    return rez

print(key_state_define(dict1, dict2))