FROM python:3.6

RUN apt-get update && apt-get install -y vim sqlite3

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN mkdir -p webconsole/migrations/versions && python manage.py migrate

EXPOSE 8000

SHELL ["/bin/bash", "-c"]

CMD ["python", "manage.py", "runserver"]
