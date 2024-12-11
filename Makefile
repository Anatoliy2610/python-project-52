PORT ?= 8000

install:
	poetry install

run:
	poetry run python manage.py runserver

start:
	poetry run gunicorn --workers=5 --bind=0.0.0.0:$(PORT) task_manager.wsgi

build:
	./build.sh

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

flake8:
	poetry run flake8 task_manager

isort:
	poetry run isort task_manager
