from flask import Blueprint, request, jsonify
from models.user import User
from services.db import db
dbRouter = Blueprint("db", __name__)

@dbRouter.route("/create", methods=["POST"])
def create():
    body = request.get_json()
    user = User(username=body.get("username"), email=body.get("email"), password=body.get("password"))
    db.session.add(user)
    db.session.commit()
    return "User added successfully"


@dbRouter.route("/read")
def read():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@dbRouter.route("/update", methods=["PUT"])
def update():
    body = request.get_json()
    if(not body.get("id")): return "Id is required"
    user = User.query.get(body.get("id"))
    if user is None:
        return "User not found", 404
    # user = User.query.filter_by(username='john_doe').first()
    if(body.get("email")): user.email = body.get("email")
    if(body.get("username")): user.username = body.get("username")
    db.session.commit()
    return "User updated successfully"

@dbRouter.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    if(not id): return "Id is required"
    user = User.query.get(id)
    if user is None:
        return "User not found", 404
    db.session.delete(user)
    db.session.commit()
    return "User deleted successfully"

