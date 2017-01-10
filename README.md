# Description

Example Flask application with:
    - SQLAlchemy + PostgreSQL model layer
    - stateless JWT authentcation
    - REST API in view layer

Used as a teaching tool last year.

# Installation

See [INSTALL.md](INSTALL.md)

# Running

## Starting dev server

~~~
source .venv/bin/activate
python manage.py runserver
~~~

## Application operations in `production` mode.

- production mode looks for config file in following locations:
    - /etc/$(APPLICATION_NAME).conf
    - ~/$(APPLICATION_NAME).conf

- all operations available from `manage.py` are still available, but require
  stating `production` mode explicitly:

- note that it is still highly recommended to have all dependencies in virtual
  environment

~~~
source .venv/bin/activate
python manage.py --environment production runserver
~~~

For cron tasks, make sure application is started from its virtual environment:

~~~
4 2 * * * /home/app_user/app_name/.venv/bin/python /home/app_user/app_name/manage.py -e production my_fancy_task
~~~

## Dependencies maintenance

Add/remove packages from `requirements.in` and then:

~~~
source .venv/bin/activate
pip-compile requirements.in
pip install -r requirements.txt
~~~

## Running tests

~~~
source .venv/bin/activate
py.test
~~~

or, for spec output:

~~~
source .venv/bin/activate
py.test --spec
~~~

## Seeding database with fake development data

~~~
source .venv/bin/activate
python manage.py db seed
~~~

## Application shell

~~~
python manage.py shell
user = factories.UserFactory()
category = models.Category.query.first()
movies = category.movies()
# ...
~~~

## Application routes

~~~
source .venv/bin/activate
python manage.py routes
~~~

## Logging in and making requests
