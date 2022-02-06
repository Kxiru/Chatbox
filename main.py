from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if request.method == 'POST':


    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
