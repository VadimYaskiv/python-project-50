def unpack(value=''):
    if isinstance(value, dict):
        return '[complex value]'
    elif value not in ['false', 'true', 'null'] and isinstance(value, str):
        return f"'{value}'"
    else:
        return f"{value}"


# form the lines of the final file depending on the type
# if type is nested than recursively unpack values of internal dictionary
def stringify_p(internal_dict, path=""):
    result = []
    for key, val in internal_dict.items():
        param = f"{path}{key}"

        if val['type'] == 'added':
            result.append(f"Property '{param}' "
                          f"was added with value: {unpack(val['value'])}"
                          )

        if val['type'] == 'deleted':
            result.append(f"Property '{param}' was removed")

        if val['type'] == 'nested':
            new_value = stringify_p(val['value'], f"{param}.")
            result.append(f"{new_value}")

        if val['type'] == 'changed':
            result.append(
                f"Property '{param}' was updated. "
                f"From {unpack(val['first_val'])} to "
                f"{unpack(val['second_val'])}")

    res = "\n".join(result)

    return res
