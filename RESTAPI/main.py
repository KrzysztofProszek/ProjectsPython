from fastapi import Request,FastAPI

app = FastAPI()
@app.get("/user")
def read_root():
    return {"Hello": "World"}


# GET parsing
@app.get("/user/{user_id}")
def get_user(user_id: int):
    # parsujemy request i na jego podstawie zwracamy zasób
    return {"user_id": user_id}

@app.get('/ping')
def ping():
    return {'Ping':'Pong'}


# POST

import json


@app.post("/user")
async def get_body(request: Request):
    # Parsujemy request i na jego podstawie wykonujemy edycje zasobu
    parsed_json = json.loads(await request.body())
    username = parsed_json['username']
    password = parsed_json['password']
    return parsed_json


# PUT
@app.put("/user/{user_id}")
def modify_item(user_id: int):
    # Parsujemy request i na jego podstawie wykonujemy edycje zasobu

    return {'status': 'edited'}


# PUT z edycją użytkownika:

# @app.put("/user/{id}")
# async def get_body(request: Request,id : int):

#     #Parsujemy request i na jego podstawie wykonujemy edycje zasobu
#     parsed_json = json.loads(await request.body())
#     username = parsed_json['username']
#     db.update().values(users.columns.name=username).where(users.columns.id=id)
#     return request.json()

# DELETE
@app.delete("/user/{user_id}")
def delete_item(user_id: int):
    # usuwamy zasób

    return {'action_status': 'deleted'}

#GET parsing
@app.get("/user/{user_id}/location/")
def get_location(user_id: int):
    locations = ["50.049683 N, 19.944544 E","32.049683 N, 11.944544 E","26.049683 N, 8.944544 E"]
    #Pobieramy sub zasób danego użytkownika na podstawie jego id i nazwy zasobu
    user_location = locations[user_id]
    return {"location": user_location }

@app.post("/texts")
async def add_text(request: Request):
    # Parsujemy request i na jego podstawie wykonujemy edycje zasobu
    parsed_json = json.loads(await request.body())
    addText = parsed_json['addText']
    addText = 'dodano ' + str(addText)
    return addText


@app.put("/number")
async def return_num(request: Request):
    parsed_json = json.loads(await request.body())
    number = parsed_json['number']
    amount = 10
    return {'number': number + int(amount)}