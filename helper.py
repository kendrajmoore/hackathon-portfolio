import json


def read_file(file):
    lists = []
    with open(file) as p:
        data = json.load(p)
        for i in data['lists']:
            lists.append(i)
    return lists


def proj_json():
    project_file = './project.json'
    projects = read_file(project_file)
    return projects

def proj_data(name):
    projects = proj_json()
    for project in projects:
        if project['name'] == name:
            item = project
    return item

def prof_json():
    profile_file = './profile.json'
    profiles = read_file(profile_file)
    return profiles

def prof_data(name):
    profiles = prof_json()
    for profile in profiles:
        if profile['name'] == name:
            item = profiles
    return item
