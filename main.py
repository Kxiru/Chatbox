from flask import Flask, render_template, request, redirect, session
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
    if request.method == 'POST':
        database.add_new_user(request.form['email'], request.form['username'], request.form['password'])
        return redirect('/')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if(database.login_user(request.form['username'], request.form['password'])):
            return redirect('/')
        else:
            return render_template('login.html')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
