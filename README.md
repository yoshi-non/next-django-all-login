# Next.js × Django Rest Framework でのログイン

## 仮想環境の作り方
```
python3 -m venv venv
```

## 仮想環境の入り方(powershell)
```
venv/Scripts/Activate.ps1
```

## 必要なモジュールのインストール
```
pip3 install -r requirements.txt
```

## Djangoプロジェクトの作成
```
django-admin startproject mysite .
```

## アプリケーション作成
```
python manage.py startapp <アプリ名>
```

## マイグレーション
```
python manage.py makemigrations
python manage.py migrate
```

## サーバ起動
```
python manage.py runserver
```

## スーパーユーザーの作成
```
python manage.py createsuperuser
```
