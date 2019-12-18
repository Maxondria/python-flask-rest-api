from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Wonderland store',
        'items': [
            {
                'name': 'Item name',
                'price': 15.09
            }
        ]
    }
]


def find_store(name):
    found_store = [store for store in stores if store['name'] == name]
    if(len(found_store) == 0):
        return False
    return found_store[0]


@app.route('/')
def home():
    return "Hello World!!"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    found_store = find_store(name)
    if(found_store == False):
        return jsonify({'message': 'store not found'})
    return jsonify(found_store)


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    found_store = find_store(name)
    if(found_store == False):
        return jsonify({'message': 'store not found'})
    request_data = request.get_json()
    new_item = {'name': request_data['name'],
                'price': request_data['price']}
    found_store['items'].append(new_item)
    return jsonify(new_item)


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    found_store = find_store(name)
    if(found_store == False):
        return jsonify({'message': 'store not found'})
    return jsonify({'items': found_store['items']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
