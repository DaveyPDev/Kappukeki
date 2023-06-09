"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = 'https://images.unsplash.com/photo-1612203985729-70726954388c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGN1cGNha2VzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60'

class Cupcake(db.Model):
    """ Cupcake Info """

    __tablename__ = 'cupcakes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def dict_cupcake(self):
        """ Serialize info """

        return {
            'id': self.id,
            'flavor': self.flavor,
            'rating': self.rating,
            'size' : self.size,
            'image': self.image
        }
    
def connect_db(app):
    """ Connect to Database """

    db.app = app
    db.init_app(app)