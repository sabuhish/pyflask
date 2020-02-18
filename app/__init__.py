from flask import  Flask
from app.celery_example import  make_celery
from celery.schedules import crontab
from utils.dbconf import db
from utils.config import  Config
from flask_migrate import Migrate
app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

celery= make_celery(app)



from app import  my_app
