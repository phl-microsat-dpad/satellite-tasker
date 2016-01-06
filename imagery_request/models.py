from imagery_request import db
from sqlalchemy import Column


class Order(db.Model):
    __tablename__ = 'order'

    order_id = Column(db.Integer, primary_key=True)
    firstname = Column(db.String)
    lastname = Column(db.String)
    email = Column(db.String)

    def __repr__(self):
        return "<Order(order_id='%s' email='%s')>" % (
            self.order_id, self.email)

    @property
    def serialize(self):
        return {
            'order_id': self.order_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email
        }
