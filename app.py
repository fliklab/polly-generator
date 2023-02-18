import os
import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    html_files = []
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if re.search('\.html$', filename):
                html_files.append(filename)
    return render_template('index.html', html_files=html_files)

@app.route('/<html_file>')
def serve_html(html_file):
    return render_template(html_file)

if __name__ == '__main__':
    app.run()