from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['DATABASE_URI'] = Config.DATABASE_URI
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class UsersModel(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(),primary_key=True)

@app.route('/')
def hello():
    return 'Hey Gibran!'

if __name__ == '__main__':
    app.run(debug=True)