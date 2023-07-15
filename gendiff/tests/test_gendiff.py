from gendiff.comparison.gendiff_logic import generate_diff


def test_generate_diff():
    links_path = 'gendiff/tests/fixtures/rezult_stylish.txt'
    with open(links_path, 'r') as f:
        rezult = f.read()

        assert generate_diff(
            'gendiff/json_files/file1.json',
            'gendiff/json_files/file2.json', 'stylish'
        ) == rezult

        assert generate_diff(
            'gendiff/yaml_files/file1.yaml',
            'gendiff/yaml_files/file2.yaml', 'stylish'
        ) == rezult
        
    links_path = 'gendiff/tests/fixtures/rezult_plain.txt'
    with open(links_path, 'r') as f:
        rezult = f.read()

        assert generate_diff(
            'gendiff/json_files/file1.json',
            'gendiff/json_files/file2.json', 'plain'
        ) == rezult

        assert generate_diff(
            'gendiff/yaml_files/file1.yaml',
            'gendiff/yaml_files/file2.yaml', 'plain'
        ) == rezult
