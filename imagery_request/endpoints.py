from flask_restful import Resource, reqparse
from imagery_request import db, models

parser = reqparse.RequestParser()
parser.add_argument('fname', type=str)
parser.add_argument('lname', type=str)
parser.add_argument('email', type=str)


class Orders(Resource):
    def post(self):
        args = parser.parse_args()

        new_order = models.Order(
                firstname=args['fname'],
                lastname=args['lname'],
                email=args['email'])

        db.session.add(new_order)
        db.session.commit()

        return {
            'fname': args['fname'],
            'lname': args['lname'],
            'email': args['email']
        }, 201

    def get(self):
        items = models.Order.query.all()
        return [item.serialize for item in items]
