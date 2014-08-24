from views import app, db
from flask.ext.restful import Resource, Api, reqparse, fields, marshal_with, marshal
from models import Item

api = Api(app)

################
#### apis   ####
################

items_fields = {
    'item_id' : fields.Integer,
    'name' : fields.String,
    'item_details' : fields.String,
    'posted_date' : fields.String,
}

class ItemsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_id', type = int, required = False, location = 'json') #help = 'No Task ID provided',
        self.reqparse.add_argument('name', type = str, default = "", location = 'json')
        self.reqparse.add_argument('item_details', type = str, default = "", location = 'json')
        self.reqparse.add_argument('posted_date', type = str, default = "", location = 'json')
        super(ItemsAPI, self).__init__()

    @marshal_with(items_fields)
    def get(self):
        results = db.session.query(Item).all()
        return results

    @marshal_with(items_fields)
    def post(self):
        import datetime
        parsed_args = self.reqparse.parse_args()
        # return parsed_args # return parsed_args returns a json of the object for example
        new_item = Item(
                parsed_args['name'],
                parsed_args['item_details'],
                datetime.datetime.utcnow(),
            )
        db.session.add(new_item)
        db.session.commit()
        print parsed_args
        return { 'message': 'success' }, 201 # curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Read a book", "item_details":"A whole lot of item details"}' http://localhost:5000/api/v1.0/items/

#require:
# error messaging
# lots of test-driven development
# can't for the life of me work out why tests aren't working

class ItemAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_id', type = int, required = False, location = 'json') #help = 'No Task ID provided',
        self.reqparse.add_argument('name', type = str, default = "", location = 'json')
        self.reqparse.add_argument('item_details', type = str, default = "", location = 'json')
        self.reqparse.add_argument('posted_date', type = str, default = "", location = 'json')
        super(ItemAPI, self).__init__()

    @marshal_with(items_fields)
    def get(self, item_id):
        result = db.session.query(Item).filter_by(item_id=item_id).first()
        return result # curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1.0/items/5

    #@marshal_with(items_fields)
    def put(self, item_id):
        parsed_args = self.reqparse.parse_args()
        db.session.query(Item).filter_by(item_id=item_id).update({
            "name":parsed_args['name'], 
            "item_details":parsed_args['item_details']
            })
        db.session.commit()
        return { 'message': 'success' }, 201 # curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"Read a book", "item_details":"A whole lot of item details"}' http://localhost:5000/api/v1.0/items/5

    #@marshal_with(items_fields)
    def delete(self, item_id):
        db.session.query(Item).filter_by(item_id=item_id).delete()
        db.session.commit()
        return { 'message': 'success' }, 201 # curl -i -H "Content-Type: application/json" -X DELETE -d '{"name":"Read a book", "item_details":"A whole lot of item details"}' http://localhost:5000/api/v1.0/items/5

# Why Marshal With?
# Then apply the marshal_with decorator to an HTTP method on a Resource class.  
# The return value of that method will be transformed to the data structure passed
# to marshal_with.  Another advantage of this approach is that you can return 
# Python class instances instead of dictionaries.
# Therefore, don't really need to apply it to anything other than get methods


api.add_resource(ItemsAPI, '/api/v1.0/items/', endpoint='Itemsapi') #curl -i http://localhost:5000/api/v1.0/items
api.add_resource(ItemAPI, '/api/v1.0/items/<int:item_id>')


