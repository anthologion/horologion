#!/usr/bin/python
import os, sys
from flask import Flask
import pypandoc as pandoc
from generate_hour import generate_service
app = Flask(__name__)

SCRIPT_DIR=os.path.dirname(os.path.abspath(sys.argv[0]))
if __name__ is not "__main__":
    SCRIPT_DIR = os.path.dirname(__file__)

@app.route("/")
def midnight_service():
    markdown = generate_service("oc", "eastern", "en-us", "hmbm", "midnight")
    return pandoc.convert_text(markdown, 'html5', format='md', extra_args=['-s'])

if __name__ == "__main__":
    app.run(debug=True)

