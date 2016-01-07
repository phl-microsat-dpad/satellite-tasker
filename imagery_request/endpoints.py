from flask_restful import Resource, reqparse
from imagery_request import db, models

parser = reqparse.RequestParser()
parser.add_argument('fname', type=str)
parser.add_argument('lname', type=str)
parser.add_argument('institution', type=str)
parser.add_argument('address', type=str)
parser.add_argument('zip', type=str)
parser.add_argument('email', type=str)
parser.add_argument('phone', type=str)
parser.add_argument('fax', type=str)
parser.add_argument('area-of-interest', type=str)
parser.add_argument('field-of-application', type=str)
parser.add_argument('area-of-study', type=str)
parser.add_argument('affiliation', type=str)
parser.add_argument('message', type=str)


class Orders(Resource):
    def post(self):
        args = parser.parse_args()

        new_order = models.Order(
            firstname=args.get('fname'),
            lastname=args.get('lname'),
            institution=args.get('institution'),
            address=args.get('address'),
            zip_code=args.get('zip'),
            email=args.get('email'),
            phone=args.get('phone'),
            fax=args.get('fax'),
            area_of_interest=args.get('area-of-interest'),
            field_of_application=args.get('field-of-application'),
            area_of_study=args.get('area-of-study'),
            affiliation=args.get('affiliation'),
            message=args.get('message'))

        db.session.add(new_order)
        db.session.commit()

        return new_order.serialize, 201

    def get(self):
        items = models.Order.query.all()
        return [item.serialize for item in items]
