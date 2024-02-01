"""

Sources:
https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
"""

from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)


# This route is specifically for the index.html file
@app.route('/')
def index():
    return render_template('index.html')


# This route is specifically for the mathOne.html file
@app.route('/math_one')
def mathOne():
    return render_template('mathOne.html')


# This route is specifically for the mathTwo.html file
@app.route('/math_two')
def mathTwo():
    return render_template('mathTwo.html')


# This route is specifically for the mathThree.html file
@app.route('/math_three')
def mathThree():
    return render_template('mathThree.html')


# This route is specifically for serving static files (like images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), filename)


if __name__ == '__main__':
    app.run(debug=True)
