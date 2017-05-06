__author__ = 'Yu'
import sqlite3
from flask import Flask, request, render_template, session, \
    redirect, url_for, abort, flash
#configurateion
DATABASE = r'.\DB\flaskr.db'
DEBUG = True
SECRET_KEY = "development key"
USERNAME = "admin"
PASSWORD = "changeme"

#create our little application
app = Flask(__name__)
"""
import configuration
"""
app.config.from_object(__name__)
#app.config.from_envvar("SETTING", silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()
