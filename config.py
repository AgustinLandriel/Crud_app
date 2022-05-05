from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
database = os.environ["MYSQL_DATABASE"]
host = os.environ["MYSQL_HOST"]
key = os.environ["SECRET_KEY"]
conexionDatabase = f"mysql://{user}:{password}@{host}/{database}"
# mysql://Usuario:password@host/database
