import json
import yaml


def json_open(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def yaml_open(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

