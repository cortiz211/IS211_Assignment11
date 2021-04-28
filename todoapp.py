from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

todo_list = [
    ("Buy batteries", "a@gmail.com", "High"),
    ("Get vaccine", "b@gmail.com", "High"),
    ("Sleep early", "a@gmail.com", "Low"),
]


@app.route('/')
def display_list():
    # display
    return render_template('todo.html', todo_list=todo_list)


@app.route('/submit', methods=["POST"])
def submit():
    global todo_list

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    todo_list.append((task, email, priority))
    return redirect(url_for('display_list'))


@app.route('/clear')
def clear():
    global todo_list
    todo_list = []
    return redirect(url_for('display_list'))


if __name__ == '__main__':
    app.run(debug=True)
