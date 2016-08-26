#!/usr/bin/python
from flask import Flask
import pypandoc as pandoc
from generate_hour import generate_service
app = Flask(__name__)

@app.route("/")
def midnight_service():
    markdown = generate_service("oc", "eastern", "en-us", "hmbm", "midnight")
    return pandoc.convert_text(markdown, 'html5', format='md', extra_args=['-s'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=False)

