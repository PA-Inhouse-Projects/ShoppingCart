import os
import json


def write_file(file_path, file_data):
    check_path_exist(file_path)
    with open(file_path, 'w') as JSON_FILE:
        json.dump(file_data, JSON_FILE)


def check_path_exist(file_path):
    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
