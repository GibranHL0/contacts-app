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
    phone = db.Column(db.String(20), nullable=True)

    def __init__(self, name, last_name, company, phone, email):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.phone = phone
        self.email = email
    
    @property
    def serialize(self):
        return {
            'email' : self.email,
            'name': self.name,
            'last_name': self.last_name,
            'company': self.company,
            'phone': self.phone
        }
    
    @property
    def getEmail(self):
        return self.email

db.create_all()
db.session.commit()

@app.route('/contacts', methods=['POST', 'GET', 'DELETE', 'PUT'])
def contacts():
    # Post the information received to the database
    if request.method == 'POST':
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
    
    # GET all the contacts in the database
    elif request.method == 'GET':
        contacts_data = Contacts.query.all()
        
        if not contacts_data:
            response = make_response(jsonify([]), 200)
        else:
            contacts_list = [contact.serialize for contact in contacts_data]
            response = make_response(jsonify(contacts_list), 200)
        
        response.headers['Content-Type'] = "application/json"

        return response
    
    # DELETE a specific contact
    elif request.method == 'DELETE':
        email = request.get_json().get('email')

        Contacts.query.filter(Contacts.email == email).delete()

        db.session.commit()

        response = make_response(
            jsonify(
                {
                    'msg': f'{email} deleted'
                }
            ),200
        )

        response.headers['Content-Type'] = "application/json"

        return response
    
    # Modify by PUT a specific contact
    elif request.method == 'PUT':
        info = request.get_json()
        name = info.get("name")
        last_name = info.get("last_name")
        company = info.get("company")
        phone = info.get("phone")
        email = info.get("email")

        contact = Contacts.query.get(email)
        contact.name = name
        contact.last_name = last_name
        contact.company = company
        contact.phone = phone
        contact.email = email

        db.session.commit()

        response = make_response(
            jsonify(
                {
                    'msg': f'{email} modified'
                }
            ),200
        )

        response.headers['Content-Type'] = "application/json"

        return response


@app.route('/emails', methods=['GET'])
def emails():
    contacts_data = Contacts.query.all()

    if not contacts_data:
        response = make_response(jsonify([]), 200)
    else:
        emails_list = [contact.getEmail for contact in contacts_data]
        response = make_response(jsonify(emails_list), 200)
    
    response.headers['Content-Type'] = "application/json"

    return response

if __name__ == '__main__':
    app.run(debug=True)