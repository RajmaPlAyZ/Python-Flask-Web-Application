
from flask import Flask, render_template, request
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    title = 'SlamBook'
    heading = 'Slam Book'
    message = 'This is a simple Flask app using Jinja2 templates & DevOps'
    return render_template('index.html', title=title, heading=heading, message=message)


@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    # Process the form data as needed

    return render_template('result.html', first_name=first_name, last_name=last_name, email=email)


def run():
    app.run(host="0.0.0.0", port=8001)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
