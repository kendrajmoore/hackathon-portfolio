import os

from dotenv import load_dotenv
from flask import Flask, render_template

from helper import proj_data, proj_json, prof_json, prof_data

load_dotenv()
app = Flask(__name__)

url = os.getenv("URL")
projects_base_url = url + "/projects/"
profiles_base_url = url + "/profiles/"

projects = proj_json()
profiles = prof_json()


@app.route('/')
def index():
    return render_template('index.html', profiles=profiles, projects=projects, title="Team Kenargi's portfolio",
                           url=url)


@app.route('/projects/<name>')
def get_project(name):
    item = proj_data(name)
    return render_template('project.html', item=item, title=name, url=projects_base_url + name)


@app.route('/profiles/<name>')
def get_profile(name):
    item = prof_data(name)
    title = name + "'s Profile"
    return render_template('profile.html', item=item, title=title, url=profiles_base_url + name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page not found"), 404
