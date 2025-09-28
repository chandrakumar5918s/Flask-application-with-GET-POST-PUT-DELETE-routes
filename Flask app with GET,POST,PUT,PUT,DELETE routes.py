from flask import Flask, request, jsonify
app=Flask(__name__)
users={}    # In-memory database

@app.route('/users',methods=['GET'])
def get_users():     # Get all users
    return jsonify(users),200

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):    # Get user ID
    if user_id in users:
        return jsonify ({user_id:users[user_id]}),200
    return jsonify ({"error":"User not found"}),404

@app.route('/users',methods=['POST'])
def sdd_user():     # Add new user
    data=request.get_json()
    user_id=data.get("id")
    name=data.get("name")

    if not user_id or not name:
        return jsonify ({"error":"Missing 'id' of 'name'"}),400

    users[user_id]=name
    return jsonify({"message":"User added","users":users}),201

@app.route('/users/<int:user_id>',methods=["PUT"])
def update_user(user_id):      # update user
    if user_id not in users:
        return jsonify({"error":"User not found"}),404

    data=request.get_json()
    name=data.get("name")
    if not name:
        return jsonify ({"error":"Missing 'name'"}),400

    user[user_id]=name
    return jsonify ({"message":"User updated","users":users}),200

@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):       # Delete user
    if user_id not in users:
        return jsonify ({"error":"User not found"}),404

    del users[user_id]
    return jsonify ({"message":"User deleted","users":users}),200
if __name__=='__main__':
    app.run(debug=True)
