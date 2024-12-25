from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'Chair',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store')
def get_store():
    return {'stores': stores}