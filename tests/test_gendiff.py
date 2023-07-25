from gendiff.comparison.gendiff_logic import generate_diff


def test_generate_diff():
    links_path = 'tests/fixtures/result_stylish.txt'
    with open(links_path, 'r') as f:
        result = f.read()

        assert generate_diff(
            'tests/fixtures/json_files/file1.json',
            'tests/fixtures/json_files/file2.json', 'stylish'
        ) == result

        assert generate_diff(
            'tests/fixtures/yaml_files/file1.yaml',
            'tests/fixtures/yaml_files/file2.yaml', 'stylish'
        ) == result

    links_path = 'tests/fixtures/result_plain.txt'
    with open(links_path, 'r') as f:
        result = f.read()

        assert generate_diff(
            'tests/fixtures/json_files/file1.json',
            'tests/fixtures/json_files/file2.json', 'plain'
        ) == result

        assert generate_diff(
            'tests/fixtures/yaml_files/file1.yaml',
            'tests/fixtures/yaml_files/file2.yaml', 'plain'
        ) == result

    links_path = 'tests/fixtures/result_json.txt'
    with open(links_path, 'r') as f:
        result = f.read()

        assert generate_diff(
            'tests/fixtures/json_files/file1.json',
            'tests/fixtures/json_files/file2.json', 'json'
        ) == result

        assert generate_diff(
            'tests/fixtures/yaml_files/file1.yaml',
            'tests/fixtures/yaml_files/file2.yaml', 'json'
        ) == result
