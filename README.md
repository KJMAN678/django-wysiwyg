- Silicon Mac 15.3
- uv 0.5.26

- リポジトリ直下に .env ファイルを作成して下記のxxxの部分を更新して入力
```sh
DJANGO_SECRET_KEY='xxx'
DJANGO_SUPERUSER_PASSWORD="xxx"
DJANGO_SUPERUSER_EMAIL="xxx@xxx.com"
DJANGO_SUPERUSER_USERNAME="xxx"
```

http://127.0.0.1:8000/admin/

```sh
# uv で環境構築
$ uv sync --dev

# migrate 実行
$ uv run manage.py migrate
$ uv run manage.py makemigrations

# 下記のsuperuserの情報を更新して入力
$ source .env

# superuser を登録
$ uv run manage.py createsuperuser --no-input

# ローカルサーバー立上げ
$ uv run manage.py runserver
```

```sh
$ uv run manage.py makemigrations
$ uv run ruff check . --fix
$ uv run ruff format .
```
