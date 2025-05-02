import psycopg2
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy

config = dotenv_values(".env")

host = config["DB_HOST"]
database = config["DB_NAME"]
user = config["DB_USER"]
password = config["DB_PWD"]
db_uri = f"postgresql://{user}:{password}@{host}/{database}"

def db_connection():
    print(host, database, user, password)
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("connected to database")
        return connection 
    except Exception as e:
        print("Connection to database failed:", e)
