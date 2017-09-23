"""Main runner of the application. Gathers together all required things and launch server."""

import config

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
app = Flask(__name__)

controller = config.DEFAULT_CONTROLLER()
validate_url = config.DEFAULT_VALIDATOR


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<shorten_url>')
def redirection(shorten_url):
    full_url = controller.fetch(shorten_url)
    return redirect(full_url)


@app.route('/shorten', methods=['POST'])
def shorten():
    full_url = request.form['full_url']
    if not validate_url(full_url):
        return render_template('index.html', warnings='Please, use valid URL for shortening')
    short_url = controller.make(full_url)
    return render_template('index.html', short_url=short_url)


if __name__ == '__main__':
    app.run(debug=True)
