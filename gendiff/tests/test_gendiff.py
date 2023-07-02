from gendiff.comparison.gendiff_logic import generate_diff


def test_generate_diff():
    links_path_flat = 'gendiff/tests/fixtures/rezult_float.txt'
    with open(links_path_flat, 'r') as f:
        rezult = f.read()
        
        #assert generate_diff('gendiff/json_files/file1_flat.json','gendiff/json_files/file2_flat.json'
        #) == rezult

        #assert generate_diff('gendiff/yaml_files/file1_flat.yaml','gendiff/yaml_files/file2_flat.yaml'
        #) == rezult
    links_path = 'gendiff/tests/fixtures/rezult.txt'
    with open(links_path, 'r') as f:
        rezult = f.read()

        assert generate_diff(
            'gendiff/json_files/file1.json',
            'gendiff/json_files/file2.json'
        ) == rezult
