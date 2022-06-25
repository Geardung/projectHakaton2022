
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

try:
    db = PostgresqlDatabase(
        database="piskarobota",
        user="postgres",
        password="postgres",
        host='localhost',
        port=5432)

except:
    db = PostgresqlExtDatabase(
        database='piskarobota',
        user='postgres',
        password="postgres",
        host='localhost', 
        port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class Controllers(BaseModel):
    
    id = IntegerField(unique=True)
    
    is_online = BooleanField(default=False)

    
class Roles(BaseModel):
    
    id = IntegerField(unique=True)
    
    label = TextField()
    
class Groups(BaseModel):
    
    id = IntegerField(unique=True)
    
    label = TextField()
    
class Users(BaseModel):

    id = IntegerField(unique=True)
    
    fio = TextField(null=False)
    
    phone = TextField(null=False)
    
    password_hash = TextField(null=False)
    
    role_id = ForeignKeyField(Roles)
    
    group_id = ForeignKeyField(Groups)

class Ver_SMS(BaseModel):
    
    id = IntegerField(unique=True)
    
    code = TextField()
    
    for_phone = TextField()
    
class Rukovoditeli(BaseModel):
    
    id = IntegerField(unique=True)
    
    user_id = ForeignKeyField(Users)
    
    group_id = ForeignKeyField(Groups)
    
class Codes(BaseModel):
    
    id = IntegerField(unique=True)
    
    code = TextField()
    
    expires_on = TextField(null=True)
    
    created_on = TextField(null=True)
    
    enter_user_id = ForeignKeyField(Users)

class Prohodi(BaseModel):
    
    id = IntegerField(unique=True)
    
    controller_id = ForeignKeyField(Controllers)
    
    when_ts = IntegerField()
    
    code_id = ForeignKeyField(Codes)
    
    who_id = ForeignKeyField(Users)
    
class Cabinets(BaseModel):
    
    id = IntegerField(unique=True)
    
    codename = TextField()
    
    label = TextField()
    
    floor = IntegerField()
    
    otvetstv_id = ForeignKeyField(Users)
    

class Events (BaseModel):
    
    id = IntegerField(unique=True)
    
    label = TextField()
    
    type = TextField()
    
    cabinet_id = ForeignKeyField(Cabinets)
    
    organisator_id = ForeignKeyField(Users)
    
class Invitations (BaseModel):
    
    id = IntegerField(unique=True)
    
    event_id = ForeignKeyField(Events)
    
    person_id = ForeignKeyField(Users)
    
class Chats (BaseModel):
    
    id = IntegerField(unique=True)
    
    label = TextField()
    
class Messages (BaseModel):
    
    id = IntegerField(unique=True)
    
    owner_id = ForeignKeyField(Users)
    
    content = TextField()
    
    chat_id = ForeignKeyField(Chats)
    
class Chats_access (BaseModel):
    
    id = IntegerField(unique=True)
    
    chat_id = ForeignKeyField(Chats)
    
    user_id = ForeignKeyField(Users)
    
class Goods (BaseModel):
    
    id = IntegerField(unique=True)
    
    label = TextField()
    
    cost = IntegerField()

