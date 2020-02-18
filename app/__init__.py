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
# "amqp://myuser:mypassword@localhost:5672/myvhost"

app.config['BROKER_URL']="amqp://guest:guest@rabbitmq:5672"
app.config['CELERY_RESULT_BACKEND']="redis://redis:6379/0"


celery= make_celery(app)



from app import  my_app
