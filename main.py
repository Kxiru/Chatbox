from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def index():
    database.test_add()
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
