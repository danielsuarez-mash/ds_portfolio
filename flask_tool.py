from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

people = {
    'name': 'Daniel',
    'age': 24,
    'address': 'Solihull'
}

ghub = "https://github.com/amateurish-coder"


# Making a home page
@app.route("/")
def home():
    return render_template('index.html', people=people, ghub=ghub)


# Whatever I type after /home/{....} will be captured by the python function as an input
@app.route('/<name>')
def user(name):
    return f'Hello {name}, please type in a valid directory'


# Return user to home page if they type /admin
@app.route('/admin')
def admin():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
