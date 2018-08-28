
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


2018-08-27

=====
- [x] create a file called portfolio.py .
- [x] create a Portfolio class with the following attributes: id, name, date_created, date_updated
- [x] Define each attribute of your class with the appropriate data type and any further restrictions or definitions that
each attribute should carry with it into the database table.
- [x] Define two class methods on your Portfolio class:
    - [x] one() : Retrieve a single instance from the database by the primary key for that record
    - [x] new() : Create a single new instance of the Portfolio class
- [x] Create a file called stock.py in the models/ directory.
- [x] Create a Stock class with the following attributes, mirror the data that you will retrieve from your 3rd party API:
id, symbol, companyName, exchange, industry, website, description, CEO, issueType, sector,
date_created, date_updated
- [x] Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
- [x] Define three class methods on your Stock class:
    - [x] one() : Retrieve a single instance from the database by the primary key for that record
    - [x] new() : Create a single new instance of the Stock class
    - [x] destroy() : Remove a single instance from the database by the primary key for that record
- [x] Create a file called schemas.py for model serializers in the models/ directory.
- [x] You will define two Marshmallow schemas in this file, 1.) PortfolioSchema and 2.) StockSchema.
- [x] Each of these will simply define the model they require for serialization (we’ll further define these later in the
course…)
- [x] In the views/portfolio.py file, define the following View Class Controllers:
    - [x] PortfolioAPIView - Controller interactions with the Portfolio model/schema
    - [x] StockAPIView - Controller interactions with the Stock model/schema
    - [x] CompanyAPIView - 3rd-party API interactions for requesting company data for the portfolio
- [x] The requests library and a free API from IEX TRADING, which does not require the use of an API key at this point.
- [x] We are specifically interested in the Company Info and the Time Series info, both of which are
accessible via an API call using a companies Stock Symbol.
- [] Using your model class methods, formulate an appropriate serialized response for each available endpoint /
method that we configured in our last lab for this application. You may want to refer back to the LAB.md
specification for each of those endpoints to review the functionality required.


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


