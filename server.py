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
When there is nothing after the website domain, this function is called
and returns the string 'Hello World!'.
"""
@app.route("/")
def home():
    global visits
    visits = visits + 1
    return render_template("index.html", visits=visits)

"""
Here we get data from the billboard top rnb and hip-hop songs and
look for all songs that have Drake as an artist.
"""
@app.route("/billboard-hits")
def billboard_hits():
    n_songs = int(request.args.get('songs', 100)) # Look at the query parameters for how many songs to return

    songs = [] # The list of songs we'll be using in the template

    chart = billboard.ChartData('r-b-hip-hop-songs') # Get chart data
    counter = 0
    for song in chart:
        if counter >= n_songs: # Check if we have enough songs yet
            break # If we do, break out of the loop
        elif 'Drake' in song.artist: 
            # If the word 'Drake' can be found in the artist string, add the song to the song list
            songs.append(song)
            counter = counter + 1 # Add one to the counter for each song added

    return render_template("billboard.html", songs=songs)

"""
If the client requests anything after the first slash and does not match
with another route, then this function is called.
"""
@app.route("/<fpath>")
def another_route(fpath):
    # Put together a string that says 'You wanted this path: [insert the path requested here]'
    response = "You wanted this path: " + fpath
    return response # Send the response string back to the client