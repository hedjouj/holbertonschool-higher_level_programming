#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs attaché à l'application
app.users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def data():
    return jsonify(list(app.users.keys()))

@app.route('/users/<username>')
def get_user(username):
    user = app.users.get(username)
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

    if username in app.users:
        return jsonify({"error": "Username already exists"}), 400

    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    app.users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run()
