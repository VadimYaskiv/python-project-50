import os
import json
import yaml


def get_data(file_path):
    data = open(file_path)
    return data


def get_extent(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension


def parse(data, extens):
    if extens == '.json':
        return json.load(data)
    elif extens == '.yaml' or extens == '.yml':
        return yaml.safe_load(data)
