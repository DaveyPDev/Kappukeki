"""Flask app for Cupcakes"""

from flask import Flask, render_template, jsonify, request
from models import db, connect_db, Cupcake
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'not-so-secret'

connect_db(app)
app.app_context().push() 

@app.route('/')
def root():
    """ Homepage """

    return render_template('base.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """ All Cupcake info """

    cupcakes = [cupcake.dict_cupcake() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """ New Cupcake """

    data = request.json
    
    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None
    )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.dict_cupcake()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>')
def single_cupcake(cupcake_id):
    """ Single Cupcake Info by ID """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.dict_cupcake())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ Update Cupcake Info """

    data = request.json 

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor= data['flavor']
    cupcake.rating= data['rating']
    cupcake.size= data['size']
    cupcake.image= data['image']
    
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.dict_cupcake()))

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Deleted')

