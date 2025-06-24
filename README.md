## Late Show API
a flask REST API to manage late-night show guests, episodes, and appearance with authentication, PostgresSQL, and JWT protection.

## setup Instructions
1. Clone the Repository
git clone git@github.com:youngpuffy/late-show-api-challenge.git

cd late-show-api-challenge

2. Install PostgresSQL
sudo -i -u postgres
psql -U postgres -d late_show_db
sudo -i -u postgres
3. Create the Database
-access PostgresSQL via terminal or pgAdmin and run
    CREATE DATABASE late_show_db;

4. Set up python Environment and install dependencies
for virtual environment management use pipenv:
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell

5. configure Environment Variables
to set your database URL in server/config.py:
DATABASE_URL=postgresql://levi:1234@localhost:5432/late_show_db

## RUNNING THE PROJECT
1. Initialize and migrate the database
run the following commands in your shell:
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade

2. seed the database
PYTHONPATH=. python server/seed.py

3. Run the flask app
 flask run

## AUTHENTICATION FLOW
 Register User
POST/REGISTER
{
  "username": "levi",
  "password": "123"
}
 login user
 POST/ LOGIN
 {
  "username": "levi",
  "password": "123"
}

##  API Routes
Route	            Method	 Auth Required?	         Description
/register	        POST	   No	                   Register a new user
/login	            POST	   No	                   Login and get JWT token
/episodes	        GET 	   No	                   List all episodes
/episodes/<int:id>	GET	       No	                   Get episode details + appearances
/episodes/<int:id>	DELETE	   No                    	Delete episode and its appearances
/guests	            GET	       No                       	List all guests
/appearances	    POST	   Yes	                    Create a new appearance

## sample requests
GET/episodes
http://127.0.0.1:5000/episodes

[
  {
    "date": "2025-23-01",
    "id": 1,
    "number": 1
  },
  {
    "date": "2025-24-01",
    "id": 2,
    "number": 2
  }
]
GET/guests
http://127.0.0.1:5000/guests
[
  {
    "id": 1,
    "name": "levi ",
    "occupation": "alive"
  },
  {
    "id": 2,
    "name": "muturi",
    "occupation": "programmer"
  }
]