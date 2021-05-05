from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Contacts(db.Model):
    __tablename__ = 'contacts'
    email = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(40), nullable=True)
    phone = db.Column(db.Integer, nullable=True)

    def __init__(self, name, last_name, company, phone, email):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.phone = phone
        self.email = email

@app.route('/contacts', methods= ['POST'])
def hello():
    info = request.get_json()
    name = info.get("name")
    last_name = info.get("last_name")
    company = info.get("company")
    phone = info.get("phone")
    email = info.get("email")

    new_contact = Contacts(name,last_name,company,phone,email)
    db.session.add(new_contact)
    db.session.commit()

    response = make_response(
        jsonify(
            {'data': {
                'email' : email,
                'name': name,
                'last_name': last_name,
                'company': company,
                'phone': phone,
                },
             'msg': 'Information recieved'
            }
        ),
        200
    )
    response.headers['Content-Type'] = "application/json"

    return response

# if __name__ == '__main__':
#     app.run(debug=True)