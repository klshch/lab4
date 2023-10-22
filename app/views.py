#!/usr/bin/python3

from flask import redirect, render_template, url_for, make_response, request, session
from app import app

import os
from datetime import datetime

from data import skills
import json

def get_system_info():
    os_info = os.uname()
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return os_info, user_agent, current_time

json_file_path = os.path.join(os.path.dirname(__file__), 'static', 'json', 'users.json')
with open(json_file_path, 'r') as users_file:
    users = json.load(users_file)


@app.route('/')
def home():
    os_info, user_agent, current_time = get_system_info()
    return render_template('home.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/page1')
def page1():
    os_info, user_agent, current_time = get_system_info()
    return render_template('page1.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/page2')
def page2():
    os_info, user_agent, current_time = get_system_info()
    return render_template('page2.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/page3')
@app.route('/page3/<int:idx>')
def page3(idx=None):
    os_info, user_agent, current_time = get_system_info()
    if idx is not None:
        if 0 <= idx < len(skills):
            skill = skills[idx]
            return render_template('page3.html', skill=skill, os_info=os_info, user_agent=user_agent, current_time=current_time)
        else:
            total_skills = len(skills)
            return render_template('page3.html', skills=skills, total_skills=total_skills, os_info=os_info, user_agent=user_agent, current_time=current_time)
    else:
        total_skills = len(skills)
        return render_template('page3.html', skills=skills, total_skills=total_skills, os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/form', methods=["GET", "POST"])
def form():
    os_info, user_agent, current_time = get_system_info()

    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        if name in users and users[name] == password:
            session["username"] = name
            return redirect(url_for("info"))
    return render_template('form.html', os_info=os_info, user_agent=user_agent, current_time=current_time)
