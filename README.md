- Silicon Mac 15.3
- uv 0.5.26

```sh
$ uv sync --dev
$ uv run manage.py runserver
$ uv run manage.py makemigrations
$ uv run manage.py migrate

$ export DJANGO_SUPERUSER_PASSWORD="test4321"
$ export DJANGO_SUPERUSER_EMAIL="test@test.com"
$ export DJANGO_SUPERUSER_USERNAME="admin"
$ uv run manage.py createsuperuser --no-input

$ mkdir wysiwyg/blog
$ uv run django-admin startapp blog blog

$ uv run ruff check . --fix
$ uv run ruff format .
```
