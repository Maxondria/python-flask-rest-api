import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='Price is required!!'
                        )

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item, 200
        return {'message': f'An item with name {name} does not exist'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        if Item.find_by_name(name):
            return {'message': f'An item with name {name} exists already'}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        try:
            Item.insert(item)
        except:
            return {'message': 'An error occured while inserting an item.'}, 500

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = Item.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {'message': 'An error occured while inserting an item.'}, 500
        else:
            try:
                Item.update(updated_item)
            except:
                return {'message': 'An error occured while updating an item.'}, 500
        return updated_item


class ItemList(Resource):
    def get(self):
        return {'items': items}
