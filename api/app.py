from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config['DATABASE_URI'] = Config.DATABASE_URI
