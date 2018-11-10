"""
This is the file that 'runs' the server.

Here we will import flask, which is a bunch of code
someone else wrote due to the common code between most
web backends.
"""

import os
from flask import Flask, send_file, render_template

# Create an object that controls the server
app = Flask(__name__)


"""
When there is nothing after the website domain, this function is called
and returns the string 'Hello World!'.
"""
@app.route("/")
def home():
    # Make a list of files in the dropbox
    files = []
    for file in os.listdir("dropbox"):
        files.append(file)
    return render_template("home.html", links=files)


"""
This is called when the url looks like: website.com/dropbox/[insert something here].

This opens a file in the 'dropbox' folder and sends the file 
contents back to the client.
"""
@app.route("/dropbox/<fpath>")
def public(fpath):
    path_to_file = "dropbox/" + fpath # Put together a path to the file requested
    return send_file(path_to_file)


"""
If the client requests anything after the first slash and does not match
with another route, then this function is called.
"""
@app.route("/<fpath>")
def another_route(fpath):
    # Put together a string that says 'You wanted this path: [insert the path requested here]'
    response = "You wanted this path: " + fpath
    return response # Send the response string back to the client