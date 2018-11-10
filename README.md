# Your first website!

## Setup

1. Install python3, pip, and virtualenv.
2. Create a Python 3 virtual environment (called 'venv') for this server.
    
    ```
    $ virtualenv venv --python=python3
    ```
3. Install the required packages.

    ```
    $ pip install -r requirements.txt
    ```
4. Give the run-script permissions to run.

    ```
    $ chmod a+x run-server
    ```
5. Run the server.

    ```
    $ ./run-server
    ```
    OR

    ```
    $ bash run-server
    ```

---

## Important files and folders

#### [requirements.txt](https://github.com/jrobchin/your-first-website/blob/master/run-server)
Contains the Python packages needed to run this server.

#### [run-server](https://github.com/jrobchin/your-first-website/blob/master/run-server)
Sets variables needed to run the server and runs the server itself.

- **FLASK_ENV** - usually _production_ or _development_ to describe what mode to run the server in
- **FLASK_APP** - the file that holds the flask app
- **flask run** - runs flask

#### [server.py](https://github.com/jrobchin/your-first-website/blob/master/server.py)
Holds the server code. Contains the logic for routing the server to certain functions.

#### [dropbox/](https://github.com/jrobchin/your-first-website/blob/master/dropbox)
Contains files for our _dropbox_.

#### [static/](https://github.com/jrobchin/your-first-website/blob/master/static)
Generally contains files for styling, JavaScript, or images that will not change.

#### [templates/](https://github.com/jrobchin/your-first-website/blob/master/templates)
Contains html that can change dynamically.

Ex. In our case, if you add files to the _dropbox_ folder, you will see more links listed under dropbox files on the homepage.
