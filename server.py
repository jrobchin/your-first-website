"""
This is the file that 'runs' the server.

Here we will import flask, which is a bunch of code
someone else wrote due to the common code between most
web backends.

We also import os which is used to make interacting with the
operating system easier.
"""

import os
from flask import Flask, send_file, render_template, Response, jsonify, request
import billboard

# Keep track of how many visits we've had since the site has been running
visits = 0
comment_list = []

# Create an object that controls the server
app = Flask(__name__)

"""
This is called when the url looks like: website.com/dropbox/[insert something here].

This opens a file in the 'dropbox' folder and sends the file 
contents back to the client.
"""
@app.route("/dropbox/<fpath>")
def dropbox(fpath):
    path_to_file = "myfiles/" + fpath # Put together a path to the file requested
    return send_file(path_to_file)

"""
This is our comments endpoint.

If we get a "GET" request, we return the comments template with the comment list.

If we get a "POST" request, we add the comment to the comments list 
and then return the comments template with the comment list.
"""
@app.route("/comments", methods=('GET', 'POST'))
def comments():
    global comment_list
    if request.method == 'POST':
        comment = {}
        comment['name'] = request.form['name']
        comment['body'] = request.form['body']
        comment['date'] = request.form['date']
        comment_list.append(comment)
    return render_template("comments.html", comments=comment_list)

"""
When there is nothing after the website domain, this function is called
and returns the string 'Hello World!'.
"""
@app.route("/")
def home():
    global visits
    visits = visits + 1
    return render_template("index.html", visits=visits)

"""
If the client requests anything after the first slash and does not match
with another route, then this function is called.
"""
@app.route("/<fpath>")
def another_route(fpath):
    # Put together a string that says 'You wanted this path: [insert the path requested here]'
    response = "You wanted this path: " + fpath
    return response # Send the response string back to the client