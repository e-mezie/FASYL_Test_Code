from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)
app.config['SECRET_KEY'] = 'cfe396b1a27c2914da6b7e45dee37180'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy (app)

from main import routes