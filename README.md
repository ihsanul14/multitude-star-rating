# Multitude-Star-Rating

This project goal is to handle rating feedback from user. There are two component of this app which are `feedback` app as the frontend and `server` app as the backend. The `feedback` written in VueJS 2 and the `server` written in Python with FastAPI framework

# Server
The source code layout were separated into 4 group based on separation of concern. Those groups are:
- Framework 
  - This layer is consist of infrastucture of the project such as databases, logger, error, utils function, .etc

- Application 
  - This layer is focusing as presentation layer to the client such as http, gRPC, websocket, .etc. In terms of http all of the handler function will be define in this layer

- Usecase
  - This layer is focusing on business logic of the application like retrieve data, transform it, and manipulating the data output  

- Entity
  - This layer is consist of all data sources of the projects like query to the databases, fetching data from external resources through API, .etc. 


# How to run

## Server
- clone the project and cd to the project
```
git clone https://github.com/ihsanul14/multitude-star-rating.git
cd /path/to/project
```
- setup PostgreSQL, see this documentation (https://www.postgresql.org/download/)
- run the backend service
```
cd server/
python -m venv venv 
```

- activate the `virtual environment`, see this documentation (https://docs.python.org/3/tutorial/venv.html)
- install dependecies
```
python -m pip install -r requirements.txt
```

- generate and migrate the schema to database 
```
alembic init alembic
```
- update the sqlalchemy.url inside `alembic.ini` and models in `alembic/env.py`
```
alembic revision --autogenerate -m "first migration"  
alembic upgrade head
```

- running the application
```
python main.py
```

## Feedback
- run tbe frontend service
```
cd feedback/
npm i
npm run serve
```
- access the application in http://localhost:8081
