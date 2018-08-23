
# Stock Portfolio

==========

RESTful API application that consumes data from a 3rd party API and provides users with the ability to create stock
portfolios. The basic functionality of the application, introduces data science, visualizations, and machine learning
into the application to analyze and make basic predictions based on historical data!


## API

Using python scripting language, pyramid restful framework


## Changelog


2018-08-22

=====

- [x] Create your Pyramid scaffold using the cookiecutter template for a SQLAlchemy scaffold
- [x] Navigate into the new project directory and create a new git repository: git init
- [x] Create a new repository on GitHub called stocks_api, and connect your repos using git remote add origin <url-to-your-repo.git> from within the project directory
- [x] Create a well named branch for today’s work in your stocks_api repository
- [x] Configure the root of your repository with the following files and directories. Thoughtfully name and organize any additional configuration or module files.
- [x] README.md - Containing good documentation for how to setup, install, and run your application
- [x] .editorconfig - Contains a standard Editor Configuration for your application (use our class standard)
- [x] .gitignore - Contains a robust Git Ignore file for all relevant Python related materials
- [x] tests/ - Contains unit tests for your application
- [x] Install the requests package using pipenv, which will enable as easy to use API for making HTTP requests to your 3rd party API


- [x] Disable the unnecessary functionality of your scaffold, by commenting out the include() statements in your __init__.py:main() function
; we will not be using Jinja2 templating (Delete that line) or Models for the time being
- [x] Delete the templates/ directory
- [x] Remove the contents of default.py and notfound.py
- [x] Ensure that your application can accept requests to the following routes, and returns the appropriate response:
- [x] GET / - the base API route -> Status code: 200 OK


Getting Started
---------------

- Change directory into your newly created project.

    cd stocks_api

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Configure the database.

    env/bin/initialize_stocks_api_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini


