from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

try:
    db = PostgresqlDatabase(
        database="piskarobota",
        user="postgres",
        password="postgres",
        host='5.23.55.230',
        port=5432)

except:
    db = PostgresqlExtDatabase(
        database='piskarobota',
        user='postgres',
        password="postgres",
        host='5.23.55.230', 
        port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class Users(Model):

    

    
    pass