from flask import Flask,jsonify
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.dbconf import db
from utils.config import  Config
from flask_migrate import Migrate
from model.models import Contact
from app.serializer import Contact
from pprint import pprint
from celery.schedules import crontab
from app.celery_example import  make_celery

from app import  app, celery


@app.route("/")
def root():
   

    return jsonify({"result": "Flask app is working perfectly"})



@app.route("/celery")
def my_celery_test():
    add_together.delay(2,4)

    return jsonify({"result": True})


@app.route("/ping")
def my_test():
    from redis import Redis

    redis_host = 'redis'
    r = Redis(redis_host, socket_connect_timeout=1) # short timeout for the test

    r.ping() 

    print('connected to redis "{}"'.format(redis_host)) 

    return jsonify({"result": r.ping()})



@celery.task(name="celery_example.add_together")
def add_together(a, b):
    return a + b


@celery.task(name="celery_example.some_test")
def some_test():
    return "test succesfflly"


  