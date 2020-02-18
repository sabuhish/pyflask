FROM tiangolo/uwsgi-nginx-flask

# ENV FLASK_APP run.py

WORKDIR /app


COPY . /app

RUN pip install -r requirements.txt

