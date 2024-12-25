import uuid
from flask import Flask , request
from db import items,stores

app = Flask(__name__)

"""

If you will restart your application
then data from the list will be lost
because it is not persisted unlike the database

"""
@app.get('/get_stores')
def get_all_stores():
    if stores:
        return stores
    return {'message': 'No Stores Registered'},404

@app.get('/get_items')
def get_all_items():
    if items:
        return items
    return {'message': 'No Items Registered'},404

@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {'message': 'Store not found'},404
    
@app.get('/item/<string:item_id>')
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {'message': 'Item not found'},404

@app.post('/store')
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, 'id': store_id}
    stores[store_id] = store
    return store,201

@app.post('/item')
def create_item(name):
    item_data = request.get_json()
    item_id = uuid.uuid4().hex
    if item_data["store_id"] not in stores:
        return {'message': 'Store not found'},404
    item = {**item_data, 'id': item_id}
    items[item_id] = item
    return item,201
    
"""   
/*
@app.get('/store/<string:name>')
def get_store_by_name(name):
    for store in stores:
        if store['name']==name:
            return store
    return {'message': 'Store not found'},404

@app.get('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if store['name']==name:
            return store['items']
    return {'message': 'Store not found'},404

*/

"""