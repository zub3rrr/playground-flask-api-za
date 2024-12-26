from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


"""

import uuid
from flask import Flask , request 
from flask_smorest import abort
from db import items,stores

app = Flask(__name__)

"""
"""
If you will restart your application
then data from the list will be lost
because it is not persisted unlike the database

"""
"""
@app.get('/get_stores')
def get_all_stores():
    if stores:
        return stores
    abort(404,message='No Stores Registered')
    # return {'message': 'No Stores Registered'},404

@app.get('/get_items')
def get_all_items():
    if items:
        return items
    abort(404,message='No Items Registered')
    # return {'message': 'No Items Registered'},404

@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message=f'No Store Found for id = {store_id}')

    
@app.get('/item/<string:item_id>')
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message='No Items Found')

        # return {'message': 'Item not found'},404

@app.delete('/item/<string:item_id>')
def delete_item(item_id):
    try:
        del items[item_id]
        return {'message': 'Item deleted'}
    except KeyError:
        abort(404,message='No Item Found')

@app.post('/store')
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    if ("name" not in store_data):
        abort(400,message='Missing Required Fields')
    for store in stores.values():
        if store["name"]==store_data["name"]:
            abort(400,message='Store Already Exists')
    store = {**store_data, 'id': store_id}
    stores[store_id] = store
    return store,201

@app.delete('/store/<string:store_id>')
def delete_store(store_id):
    try:
        del stores[store_id]
        return {'message': 'Store deleted'}
    except KeyError:
        abort(404,message='No Store Found')

@app.post('/item')
def create_item():
    item_data = request.get_json()
    item_id = uuid.uuid4().hex
    if ("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
        abort(400,message='Missing Required Fields')
    
    for item in items.values():
        if (item["name"]==item_data["name"] and item["store_id"]==item_data["store_id"]):
            abort(400,message='Item Already Exists')
    if item_data["store_id"] not in stores:
        abort(404,message='No Items Found')
    item = {**item_data, 'id': item_id}
    items[item_id] = item
    return item,201

@app.put('/item/<string:item_id>')
def update_item(item_id):
    item_data = request.get_json()
    if item_id not in items:
        abort(404,message='No Items Found')
    try:
        item = items[item_id]
        item.update(item_data)
        return item
    except KeyError:
        abort(404,message='No Items Found')
"""   

"""
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