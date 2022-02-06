import main
import certifi
import flask
from flask_pymongo import PyMongo

mongodb_client = PyMongo(main.app, uri="mongodb+srv://sustainagram:sus1@sustainagram.eueen.mongodb.net/Sustainagram?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = mongodb_client.db


def add_new_user(email, usern, passw):
    db.users.insert_one({'email': email, 'username': usern, 'password': passw})
    print("This ran")
    return flask.jsonify(message="success!")

def login_user(usern, passw):
    if(db.users.find({"username": usern, "password": passw})):
        print("user exists!")
        main.curuser = usern
        return True
    else:
        print("User does not exist")
        return False

def get_all_posts():
    return db.posts.find()

def newPost(subject, desc):
    db.posts.insert_one({'subject': subject, 'description': desc})
    print("This ran")
    return flask.jsonify(message="success!")
