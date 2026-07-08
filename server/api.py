from flask import Flask, jsonify
import json

products = []
with open("data/products.json", "r") as f:
    products = json.load(f)

app = Flask(__name__)
from services import products

@app.route("/")
def home():
    return jsonify({
        "all_products" : "/products",
        "single_product" : "/product/(product name/ barcode)",
    })

#GET
@app.route("/products", methods=["GET"])
def all_products():
    return jsonify(products)


#GET_SINGLE
@app.route("/product/<str:key>", methods=["GET"])
def get_product(key):
        for product in products:
            if product['product_name'] or product['barcode'] == key:
                return product

#POST
@app.route("/product", methods=["POST"])
def add_product(barcode, name, quantity, brand, category, inventory):
    products.append({
        "barcode": barcode,
        "product_name": name,
        "quantity": quantity,
        "brands" : brand,
        "category" : category,
        "inventory": inventory,
        }
    )
    return products


# PATCH
@app.route("/products/<str:key>", methods=["PATCH"])
def update_product(key, change, update):
        for product in products:
            if product['product_name'] or product['barcode'] == key:
                print(product)
                product[change] = update
                return product

#DELETE
@app.route("/products/<str:key>", methods=["DELETE"])
def delete_product(key):
        for product in products:
            if product['product_name'] or product['barcode'] == key:
                products.pop(product)
                return products

if __name__ == "__main__":
    app.run(debug=True)
