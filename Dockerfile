FROM python:3.7-alpine

COPY src/app.py /app/app.py
COPY src/routes /app/routes
COPY src/static /app/static
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT python app.py
EXPOSE 5000