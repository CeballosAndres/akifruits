# AkiFruits
An approach to Akinator.

## Set environment

### Create virtual environment

`python3 -m venv env`

### Activate virtual environment

**On macOS**

`source env/bin/activate`

**On Windows** 

cmd `env\Scripts\activate.bat`

PowerShell `venv\Scripts\Activate.ps1`

### Install dependencies 

`pip install -r requirements.txt`

### Install MongoDB

**On macOS**

`brew install mongodb-community`

## Run

### Local

`python wsgi.py`

`gunicorn wsgi:app`

### Heroku

[HerokuApp](https://akifruits.herokuapp.com/)