import sys, os
basedir = os.path.abspath(os.path.dirname(__file__))



DB_HOST = os.getenv("localhost")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_PORT = os.getenv("DB_PORT", 5432)


class Config(object):
    # SQLALCHEMY_DATABASE_URI = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI =  'postgres:///test_db' #lor local testing
    # SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 'lite.db')
    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {"encoding" : "utf-8-sig"}
    BROKER_URL = "amqp://guest:guest@rabbitmq:5672"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"

