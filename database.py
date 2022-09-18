from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg2
import os

password = os.environ['PASSWORD']
user = os.environ['USERNAME1']
database = 'pizza_delivery'
hostname = 'localhost'
port_id = 5432

engine = create_engine('postgresql://user:password@localhost/pizza_delivery',
    echo = True
)

Base = declarative_base()

Session = sessionmaker()