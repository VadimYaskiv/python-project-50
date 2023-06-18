from gendiff.comparison.gendiff_logic import generate_diff


def test_generate_diff():
    with_links_path = 'gendiff/tests/fixtures/rezult.txt'
    with open(with_links_path, 'r') as f:
        rezult = f.read()
        
        assert generate_diff(
            'gendiff/json_files/file1.json',
            'gendiff/json_files/file2.json'
        ) == rezult

        assert generate_diff(
            'gendiff/yaml_files/file1.yaml',
            'gendiff/yaml_files/file2.yaml'
        ) == rezult
