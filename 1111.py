from gendiff import generate_diff


diff = generate_diff('gendiff/json_files/file1.json', 'gendiff/json_files/file2.json')
print(diff)