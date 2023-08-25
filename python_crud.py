from flask import Flask, jsonify, request
import uuid
import json

app = Flask(__name__)

# USER List
users = []

# Default Route
@app.route("/")
def service_status():
    return jsonify({"Health": True})

# Create User
@app.route("/user", methods=['POST'])
def create_user():
    user = request.get_json()
    user["_id"] = uuid.uuid4()
    users.append(user)
    return jsonify(user), 201

# Read Users
@app.route("/user", methods=["GET"])
def get_users():
    return jsonify(users), 200

# Read User by Id
@app.route("/user/<id>", methods=["GET"])
def get_user_byId(id):
    for u in users:
        if(str(u.get("_id")) == id):
            return jsonify(u), 200
    return jsonify({}), 404 

# Read User by Email
@app.route("/user/<email>", methods=["GET"])
def get_user_byEmail(email):
    for u in users:
        if(str(u.get("email")) == email):
            return jsonify(u), 200
    return jsonify({}), 404

# Update User
@app.route("/user", methods=["PUT"])
def update_user():
    user = request.get_json()
    update_id = str(user['_id'])

    for idx, u in enumerate(users):
        user_id = str(u.get("_id"))
        if(user_id == update_id):
            print("User found")
            users[idx] = user
            return jsonify(user), 200
    return jsonify({}), 404

# Delete User
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    for idx, u in enumerate(users):
        if(str(u.get("_id")) == id):
            users.pop(idx)
            return jsonify(users), 204
    return jsonify({}), 404
