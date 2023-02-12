from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

people = {
    'name': 'Daniel Suarez-Mash',
    'age': 24,
    'address': 'Solihull'
}

ghub = "https://github.com/amateurish-coder"


# Making a home page
@app.route("/")
def home():
    return render_template('index.html', people=people, ghub=ghub)


# About page
@app.route("/about-me")
def about_me():
    return render_template('about-me.html', people=people, ghub=ghub)


# About page
@app.route("/ds-projects")
def ds_projects():
    return render_template('ds-projects.html', people=people, ghub=ghub)


# Whatever I type after /home/{....} will be captured by the python function as an input
@app.route('/<name>')
def user(name):
    return f'Hello {name}, please type in a valid directory'


# Return user to home page if they type /admin
@app.route('/admin')
def admin():
    return redirect(url_for('home'))


# send static files from directory
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)
