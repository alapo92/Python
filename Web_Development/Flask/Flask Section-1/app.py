from flask import Flask, jsonify, request, render_template

app = Flask(__name__)  # python variable that gives a file a unique name

stores = [{
    'name': 'My Wonderful Store',
    'items': [{'name': 'my item', 'price': 15.99}]
}]


# POST - used to receive data
# GET - used to send data back only
@app.route('/')  # 'http://www.google.com/' last slash indicates home page
def home():
    return render_template('index.html')


# POST /store data: {name:}
@app.route('/store', methods=['POST'])  # only accessible via post request
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # iterate over stores,
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

    #  if the store name matches return that one
    #  if it doesnt match, return an error message


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})  # convert list to dict to convert to JSON file


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')  # 'http://127.0.0.1:5000/store/some_name/item'
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        return jsonify({'message': 'item not found'})


app.run(port=5000)

#   going to a page always sends a GET
