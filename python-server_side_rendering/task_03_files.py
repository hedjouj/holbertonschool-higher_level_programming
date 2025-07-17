from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_file(filename):
    products = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            products = read_json_file('products.json')
        else:
            products = read_csv_file('products.csv')

        if product_id:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")

        return render_template('product_display.html', products=products)

    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")
    except Exception as e:
        return render_template('product_display.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
