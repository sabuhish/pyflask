

### Simple containerized Flask application  ships with rabbitmq, redis, celery, postgress and flower 



### Usage

```python

python3 -m venv .venv

pip install -r requirements.txt

export FLASK_APP=run.py     

export FLASK_ENV=development

flask run or python run.py

```
### For the first migration


```sh

    flask db init

    flask db migrate

    flask db upgrade

if changes made on model:

    flask upgrade
```


### Docker commands to run app

```bash
docker-compose up --build -d

without detach mode:

docker-compose up --build 


open browser 
type:

localhost:8080

```


