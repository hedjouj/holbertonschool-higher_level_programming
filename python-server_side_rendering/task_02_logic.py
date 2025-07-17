from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        return render_template('items.html', items=data['items'])
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template('items.html', items=[])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
