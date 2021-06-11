import json


def read_file(file):
    with open(file) as p:
        data = json.load(p)
        return data["items"]


def load_items(filename):
    items = read_file(filename)
    items_dict = {}
    for item in items:
        name = item["name"]
        items_dict[name] = item
    return items_dict


def load_projects() -> dict:
    return load_items('./project.json')


def load_profiles() -> dict:
    return load_items('./profile.json')
