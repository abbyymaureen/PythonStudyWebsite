"""

Sources:
https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
"""

from flask import Flask, url_for, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('../website/html/index.html')


with app.test_request_context():
    print(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
