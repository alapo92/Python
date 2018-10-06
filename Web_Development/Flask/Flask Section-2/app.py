from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Peter'  # if in real life use hide key
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,  # price is a required field
                        help='This field cannot be left blank'
                        )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items),
                    None)  # next returns the first item found by the filter
        # !! NEXT can break a programme if there are no more items unless u pass the none argument
        #   for item in items:
        #       if item['name'] == name:
        #       return item  # no need to jsonify with restful
        return {'item': item}, 200 if item else 404
        # 200 being most popular http status code (success)
        # 200 if item is not None else 404 (is not None can be shortened to if exists=(if name))

    def post(self, name):
        #   data = request.get_json(silent=True)     no error - returns none
        #   data = request.get_json(force=True) instead of get json we can use a parser
        #   force true - no need for a content type header, dangerous because without it,
        #   if the header is not set correctly - do nothing,
        #   with it u dont look at the header therefore u always process the text even if its incorrect
        #
        #   Error first approach !!
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': 'an item with name "{}" already exists.'.format(name)}, 400  # 400 is bad request

        # data = request.get_json()
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # http status code 'created'

    def delete(self, name):
        global items    # to define that the variable is from the outer scope
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    # @jwt_required() - if u wanna authorise it
    def put(self, name):
        #   data = request.get_json()
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')  # http://127.00.1:5000/item/Chair
api.add_resource(ItemList, '/items')
if __name__ == "__main__":
    app.run(port=5000, debug=True)
