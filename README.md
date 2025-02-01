- Silicon Mac 15.3
- uv 0.5.26

- リポジトリ直下に .env ファイルを作成して下記のxxxの部分を更新して入力
```sh
DJANGO_SECRET_KEY='xxx'
```

```sh
# uv で環境構築
$ uv sync --dev

# migrate 実行
$ uv run manage.py migrate

# 下記のsuperuserの情報を更新して入力
$ export DJANGO_SUPERUSER_PASSWORD="xxx"
$ export DJANGO_SUPERUSER_EMAIL="xxx@xxx.com"
$ export DJANGO_SUPERUSER_USERNAME="xxx"

# superuser を登録
$ uv run manage.py createsuperuser --no-input

# ローカルサーバー立上げ
$ uv run manage.py runserver
```
