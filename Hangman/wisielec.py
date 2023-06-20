from fastapi import Request, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import sqlalchemy as db
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Obiekty bazy danych SQLAlchemy
engine = db.create_engine('sqlite:///wisielec.db', connect_args={"check_same_thread": False})
connection = engine.connect()
metadata = db.MetaData()
categories = db.Table('Categories', metadata,
                      db.Column('id', db.Integer(), primary_key=True, autoincrement=True),
                      db.Column('name', db.String(60), nullable=False),
                      db.Column('description', db.String(100), nullable=False)
                      )
words = db.Table('Words', metadata,
                 db.Column('id', db.Integer(), primary_key=True, autoincrement=True),
                 db.Column('category_id', db.Integer(), nullable=False),
                 db.Column('word', db.String(60), nullable=False)
                 )
metadata.create_all(engine)
print("Klucze tabeli:", categories.columns.keys(), '\n')
print("Klucze tabeli words:", words.columns.keys(), '\n')


# endpoint do pobierania wszystkich kategorii
@app.get('/categories')
def get_categories():
    try:
        query = db.select(categories)
        result = connection.execute(query).fetchall()
        if result == []:
            return {"status": "failed", "info": "No such categories"}
        return result
    except Exception as error:
        print(error)
        return {"status": "failed", "info": str(error)}


# endpoint do pobierania kategorii o danym id
@app.get('/categories/{id_category}')
def get_category(id_category: int):
    try:
        query = db.select(categories).where(categories.columns.id == id_category)
        result = connection.execute(query).fetchall()
        if result == []:
            return {"status": "failed", "info": "No such categories"}
        return result[0]
    except Exception as error:
        print(error)
        return {"status": "failed", "info": str(error)}


# endpoint do dowania kategorii
@app.post('/categories')
async def add_category(request: Request):
    try:
        parsed_jason = json.loads(await request.body())
        name = parsed_jason['name']
        description = parsed_jason['description']
        query = db.insert(categories).values(name=name, description=description)
        connection.execute(query)
        print(name, description)
        return {'status': 'done'}
    except Exception as error:
        print(error)
        return {"status": "failed"}


# endpoint do odawania hasła
@app.post('/words')
async def add_words(request: Request):
    try:
        parsed_jason = json.loads(await request.body())
        category_id = parsed_jason['category_id']
        name = parsed_jason['name']
        query = db.select(categories).where(categories.columns.id == category_id)
        result = connection.execute(query).fetchall()
        if result == []:
            return {"status": "failed", "info": "No such categories"}

        query = db.insert(words).values(category_id=category_id, word=name)
        connection.execute(query)

        print(category_id, name)
        return {'status': 'done'}
    except Exception as error:

        print(error)
        return {"status": "failed"}


# Endpoint do randomowego hasła
@app.get("/words/random")
def get_random():
    try:
        query = db.select(words).order_by(db.func.random())
        word = connection.execute(query).fetchone()
        print(word)
        query1 = db.select(categories).where(categories.columns.id == word['category_id'])
        category = connection.execute(query1).fetchone()
        result = {'id': word[0], 'category': {'name':category[1], 'description':category[2]}, 'name': word[2] }
        return result
    except Exception as error:

        print(error)
        return {"status": "failed"}