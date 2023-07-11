import os
import json


def write_file(file_path, file_data):
    check_path_exist(file_path)
    with open(file_path, 'w') as json_file:
        json.dump(file_data, json_file)


def check_path_exist(file_path):
    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def parse_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

