# Flask Movies API

<p align="center">
  <img src="https://raw.github.com/marcosvbras/flask-movies/master/images/sparrow.jpg" alt="Custom image"/>
</p>

**Flask Movies** is a Python API project created to taste the powerful of [Flask Framework](http://flask.pocoo.org/). This project also uses [MongoDB](https://www.mongodb.com/) as persistence layer.

## Preparing the environment

### API
This project was developed with **Python version 3.6**, so, for a correct running, it is recommended to install this one.

First, it is required to install all project dependencies. You can use [Pipenv](https://github.com/pypa/pipenv) or [Virtualenv](https://virtualenv.pypa.io/en/stable/). If you are using **Pipenv**, use the following command to install from **Pipfile**:

```bash
$ pipenv install
```

...and active the environment:
```bash
$ pipenv shell
```

However, if you are using **Virtualenv**, you need to activate the environment and install from **requirements.pip** file with the following commands:

```bash
$ source YOUR_ENVIRONMENT_DIRECTORY/bin/activate
$ pip install -r requirements.pip
```

### Database

Install [MongoDB](https://www.mongodb.com/) in your machine and import the data from directory **dump**:

```bash
$ mongorestore dump
```

Be sure **MongoDB** process are running.

## How to run

Export environment variable to tell Flask which file must be loaded and then run Flask:

```bash
$ export FLASK_APP=app.py
$ flask run
* Serving Flask app "app"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

or simply run with:
```bash
$ python app.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Choose what you prefer.

Optionally, you can set debug mode to have more control about your development tests (like automatic code reload):

```bash
$ export FLASK_DEBUG=1
```
Run the API again and enjoy it!
