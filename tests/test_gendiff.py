import pytest
from gendiff.comparison.gendiff_logic import generate_diff


test_arguments_values = [('tests/fixtures/json_files/file1.json',
                          'tests/fixtures/json_files/file2.json', 'stylish',
                          'tests/fixtures/result_stylish.txt'),
                         ('tests/fixtures/yaml_files/file1.yaml',
                          'tests/fixtures/yaml_files/file2.yaml', 'stylish',
                          'tests/fixtures/result_stylish.txt'),
                         ('tests/fixtures/json_files/file1.json',
                          'tests/fixtures/json_files/file2.json', 'plain',
                          'tests/fixtures/result_plain.txt'),
                         ('tests/fixtures/yaml_files/file1.yaml',
                          'tests/fixtures/yaml_files/file2.yaml', 'plain',
                          'tests/fixtures/result_plain.txt'),
                         ('tests/fixtures/json_files/file1.json',
                          'tests/fixtures/json_files/file2.json', 'json',
                          'tests/fixtures/result_json.txt'),
                         ('tests/fixtures/yaml_files/file1.yaml',
                          'tests/fixtures/yaml_files/file2.yaml', 'json',
                          'tests/fixtures/result_json.txt')]


@pytest.mark.parametrize("filepath_1, filepath_2, format, result_path", test_arguments_values)
def test_generate_diff(filepath_1, filepath_2, format, result_path):
    diff_result = generate_diff(filepath_1, filepath_2, format)
    with open(result_path, 'r') as f:
        exp_result = f.read()

    assert diff_result == exp_result
