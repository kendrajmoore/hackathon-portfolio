import json

def read_file(file):
    lists = []
    with open(file) as p:
        data = json.load(p)
        for i in data['lists']:
            lists.append(i)
    return lists

