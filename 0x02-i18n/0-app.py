#!/usr/bin/env python3
"""
serving a simple page
"""
from flask import Flask, render_template

app = Flask('__main__')


@app.route("/")
def index() -> str:
    """
    return the index page
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
