import os

from dotenv import load_dotenv
from flask import Flask, render_template, json, current_app as app
from helper import read_file
load_dotenv()
app = Flask(__name__)




@app.route('/')
@app.route('/index')
def index():

    img_1 = './static/img/friends.jpg'
    img_2 = "./static/img/Gigi_Hui.png"
    img_3 = "./static/img/friends.jpg"
    project_file = os.path.join(app.static_folder, 'data', 'project.json')
    projects = read_file(project_file) 
    profile_file = os.path.join(app.static_folder, 'data', 'profile.json')
    profiles = read_file(profile_file)
    return render_template('index.html', profiles=profiles, projects=projects, title="Team Kenargi's portfolio", url=os.getenv("URL"),
    img_1=img_1, img_2=img_2, img_3=img_3)



@app.route('/project/<name>')
def get_project(name):
    project_file = os.path.join(app.static_folder, 'data', 'project.json')
    projects = read_file(project_file)       
    for project in projects:
        if project['name'] == name:
            item = project
    return render_template('project.html', projects=projects, item=item, url=os.getenv("URL"))


@app.route('/profile/<name>')
def get_profile(name):
    profile_file = os.path.join(app.static_folder, 'data', 'profile.json')
    profiles = read_file(profile_file)
    for profile in profiles:
        if profile['name'] == name:
            item = profile
    return render_template('profile.html', profiles=profiles, item=item, title='Profile', url=os.getenv("URL"))

  
@app.errorhandler(404)
def page_not_found(e):
    source_img="./static/img/404.png"
    return render_template('404.html', img=source_img, title="Page not found"), 404
    

