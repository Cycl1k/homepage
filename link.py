import json

def links(file):
    file_json = open (file)
    data_json = json.load(file_json)
    sorted_dict = dict(sorted(data_json.items()))
    return sorted_dict