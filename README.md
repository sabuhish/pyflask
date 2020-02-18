



python3 -m venv .venv



pip install -r requirements.txt


export FLASK_APP=run.py     

export FLASK_ENV=development


flask run


for first migration

flask db init

flask db migrate

flask db upgrade


if changes made on model:

flask upgrade




docker-compose up --build -d

without detach mode:

docker-compose up --build 


open browser 
type:

localhost:8080



