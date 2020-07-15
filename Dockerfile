FROM python:3.7-alpine

COPY src/app.py /app/src/app.py
COPY src/routes /app/src/routes
COPY src/static /app/src/static
COPY gunicorn.conf.py /app/gunicorn.conf.py 
COPY wsgi.py /app/wsgi.py 

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT gunicorn -c gunicorn.conf.py wsgi:APP
EXPOSE 5000