import main
import certifi
import flask
from flask_pymongo import PyMongo

mongodb_client = PyMongo(main.app, uri="mongodb+srv://sustainagram:sus1@sustainagram.eueen.mongodb.net/Sustainagram?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = mongodb_client.db


def test_add():
    posts = db.posts.find()
    users = db.users.find()
    print([post for post in posts])
    print([user for user in users])
    print("This ran")
    # db.users.insert_one({'username': 'test1', 'password': 'pass1'})
    return flask.jsonify(message="success!")

def add_new_user(email, usern, passw):
    db.users.insert_one({'email': email, 'username': usern, 'password': passw})
    print("This ran")
    return flask.jsonify(message="success!")

def login_user(usern, passw):
    if(db.users.find({"username": usern, "password": passw})):
        print("user exists!")
        return True
    else:
        print("User does not exist")
        return False
