# Сайт для мониторинга состояния серверов БСКБ Нефтехимавтоматика

## Подготовка к запуску

```
* Поставить виртуальное окружение: python -m venv env

* Запустить его: source env/Scripts/activate

* Скачать библиотеки: pip install -r requirements.txt

* Применить миграции к бд:
*   1. python manage.py migrate servers
*   2. python manage.py migrate users
*   3. python manage.py migrate

* Если не будет css стилей, то: python manage.py collectstatic
```

## Запуск celery

```
* Для начала необходимо поставить redis сервер либо через docker, либо качать именно redis-server.exe
* В IDE (PyCharm или VSCode) открываем 2 вкладки терминала и пишем туда команды из файла commands.txt
```

## Запуск
```
* python manage.py runserver
* Можно создать админа: python manage.py createsuperuser
```
