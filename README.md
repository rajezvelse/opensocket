# opensocket

Sanic - SocketIO startup kit.

![banner](./screenshot.png)

## Getting started
Clone the repo, followup the steps:

1. Configure database and server host settings in  ```webconsole/main/settings.py```

1. ``` pip install -r requirements``` - Installs required python packages

1. ```python manage.py migrate``` - Updates database schema

1. To start server run ```python manage.py runserver```

Open http://localhost:8000 to view webconsole


Note:
You may need to install ```mysql/sqlite3``` server depends on database that you are using.

## Getting started with docker
Pull docker image
```
docker pull rajez/opensocket:beta
```

Run
```
docker run -dti -p 8000:8000 --name opensocket rajez/opensocket:beta
```

Open http://localhost:8000 to view webconsole

## Workup

You may modify socket authentication in  ```socketplay/connection/authentication.py```

Define websocket event in directory ```socketplay/events```

Define namespaces in directory  ```socketplay/namespaces```

Define rooms in directory  ```socketplay/rooms```
  
## Sources
[sanic](https://sanic.readthedocs.io/en/latest/)

[python-socketio](https://python-socketio.readthedocs.io/en/latest/)

## References

[python-sokcetio](https://github.com/miguelgrinberg/python-socketio) - Example implementations of python-socketio for various deployment methods

[sanic-starter](https://github.com/seanpar203/sanic-starter) - sanic starter with [alembic](https://alembic.sqlalchemy.org/en/latest/) migration
