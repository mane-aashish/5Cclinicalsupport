# 5Cclinicalsupport

Clinical Support Module for 5C Network

# Installation

- Navigate to the directory with `requirements.txt` file.
- Run `pip install -r requirements.txt`

While setting up the environment on local, it's always better to use python's virtual environments. Commands to install virtualenv can be found [here](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv).

Steps to activate a virtualenv:
- Navigate to a directory where you want your virtual environment.
- Run `virtualenv <Enter directory name>`.
- From outside this directory, run `source <created directory name>/bin/activate`.
- Then follow the installation steps mentioned above.

# Usage

- Navigate the to the directory with the `manage.py` file.
- Run `python manage.py runserver`. Development server will be set up at localhost:8000
- Go to `localhost:8000/chest/clinic/<scan ID>` to enter clinical observations.
- Go to `localhost:8000/chest/radio/<scan ID>` to enter radiologist findings and compute diagnosis.
- Go to `localhost:8000/chest/diagnosis/<scan ID>` to view the suggested diagnosis.

# Code Description

- `Templates` folder contains the HTML files. 
- `views.py` contains the logic to implementing the decision support. Documentation is provided in the file. 
- `models.py` contains the DB schema. Refer Django migrations to reflect changes to the DB schema.

# Making Changes to DB 

When any change has been made to the DB, the changes need to be manually migrated before running the code. To migrate DB changes:
- Go to directory with `manage.py` file.
- Run `python manage.py makemigrations`.
- Run `python manage.py migrate`.
