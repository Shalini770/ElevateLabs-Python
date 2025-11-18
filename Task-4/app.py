from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user list
users = []
next_id = 1  # Auto-incrementing user ID


# -------------------------------------
# CREATE USER (POST)
# -------------------------------------
@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.json

    new_user = {
        "id": next_id,
        "name": data.get("name"),
        "email": data.get("email")
    }

    users.append(new_user)
    next_id += 1

    return jsonify({"message": "User created", "user": new_user}), 201


# -------------------------------------
# GET ALL USERS (GET)
# -------------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# -------------------------------------
# GET SINGLE USER (GET)
# -------------------------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# -------------------------------------
# UPDATE USER (PUT)
# -------------------------------------
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    return jsonify({"message": "User updated", "user": user}), 200


# -------------------------------------
# DELETE USER (DELETE)
# -------------------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200


# -------------------------------------
# MAIN
# -------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
