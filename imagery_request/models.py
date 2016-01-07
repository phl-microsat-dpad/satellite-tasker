from imagery_request import db
from sqlalchemy import Column


class Order(db.Model):
    __tablename__ = 'order'

    order_id = Column(db.Integer, primary_key=True)
    firstname = Column(db.String)
    lastname = Column(db.String)
    institution = Column(db.String)
    address = Column(db.String)
    zip_code = Column(db.String)
    email = Column(db.String)
    phone = Column(db.String)
    fax = Column(db.String)
    area_of_interest = Column(db.String)
    field_of_application = Column(db.String)
    area_of_study = Column(db.String)
    affiliation = Column(db.String)
    message = Column(db.String)

    def __repr__(self):
        return "<Order(order_id='%s' email='%s')>" % (
            self.order_id, self.email)

    @property
    def serialize(self):
        return {
            'order_id': self.order_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'institution': self.institution,
            'address': self.address,
            'zip_code': self.zip_code,
            'email': self.email,
            'phone': self.phone,
            'fax': self.fax,
            'area_of_interest': self.area_of_interest,
            'field_of_application': self.field_of_application,
            'area_of_study': self.area_of_study,
            'affiliation': self.affiliation,
            'message': self.message
        }
