from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table

import hashlib
import secrets

def scramble(password: str):
    """ hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


#  instantiate a blueprint for each collection
bp = Blueprint('users', __name__, url_prefix = '/users')

@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())

@bp.route('', methods=['POST'])
def create():
    # request body must contain : name and password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    # username must be at least 3 chars long | password must be at least 8 chars long
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    # construct new user
    user = User(
        username = request.json['username'],
        password = scramble(request.json['password']) # scramble pw before storing it in db
    )
    db.session.add(user)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(user.serialize())

@bp.route('<int:id>', methods=['DELETE'])
def delte(id: int):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)  # prepare DELETE statment
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)


@bp.route('<int:id>', methods = ['PATCH', 'PUT'])
def update(id: int):
    """ update username, password, or both"""
    # check to see if user exists
    user = User.query.get_or_404(id)
    # request must contain username and password
    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)
    
    if 'username' in request.json:
        # username must have a length of 3 or more chars 
        if len(request.json['username']) < 3:
            return abort(400)
        else:
            # update username
            user.username = request.json['username']

    if 'password' in request.json:
        # password must by at least 8 characters
        if len(request.json['password']) < 8:
            return abort(400)
        else:
            # update password
            user.password = scramble(request.json['password'])

    try:
        db.session.commit()
        return jsonify(user.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liking_users(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)


    
