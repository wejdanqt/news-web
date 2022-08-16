# Introduction

The goal of this project is to view latest news and mark your favorites articles

## Features
- View Latest news 
- Add or remove your favorite articles from favorite list

## Technologies
- [Python 3.9.6](https://www.python.org/downloads/release/python-396/)
- [Django 4.1](https://docs.djangoproject.com/en/4.1/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)


## Getting Started
First clone the repository from Github and switch to the new directory:
```sh
$ git clone https://github.com/wejdanqt/news-web.git
$ cd {{ project_name }}
```
Create your virtualenv
```sh
$ virtualenv venv
```
Activate the virtualenv for your project.
```sh
$ source venv/bin/active
```

Install project dependencies:

```sh
$ pip install -r requirements.txt
```
You can now run the development server:
```sh
$ python3 manage.py runserver
```
**_NOTE:_**  The database is already loded by external API https://newsapi.org/ to `db.sqlite3` in case the database is empty please follow the following commands to reload it:

```sh
python3 manage.py makemigrations main
python3 manage.py makemigrations accounts
python3 manage.py migrate
python3 manage.py get_articles_command
python3 manage.py runserver
```