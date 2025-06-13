#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}  # <-- Move users outside the app context

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
