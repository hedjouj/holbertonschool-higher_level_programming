#!/usr/bin/env python3
from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def data():
    users = load_users()
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    users = load_users()
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    users = load_users()
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
    save_users(users)

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
