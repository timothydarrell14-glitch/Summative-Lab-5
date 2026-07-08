from flask import Flask, jsonify, request

app = Flask(__name__)

from modules.product import (
    add_product as create_product,
    all_products,
    delete_product as remove_product,
    get_product,
    update_product as change_product,
)

@app.route("/")
def home():
    return jsonify({
        "all_products" : "/products",
        "single_product" : "/product/(product name/ barcode)",
    })

#GET
@app.route("/products", methods=["GET"])
def products():
    return jsonify(all_products)


#GET_SINGLE
@app.route("/product/<string:key>", methods=["GET"])
def single_product(key):
    product = get_product(key)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

#POST
@app.route("/product", methods=["POST"])
def add_product():
    data = request.get_json() or {}
    required_fields = ["barcode", "product_name", "quantity", "brands", "category", "inventory"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": "Missing fields", "fields": missing_fields}), 400

    product = create_product(
        data["barcode"],
        data["product_name"],
        data["quantity"],
        data["brands"],
        data["category"],
        data["inventory"],
    )
    return jsonify(product), 201


# PATCH
@app.route("/products/<string:key>", methods=["PATCH"])
def update_product(key):
    data = request.get_json() or {}
    change = data.get("field")
    update = data.get("value")

    if change is None or update is None:
        return jsonify({"error": "Request must include 'field' and 'value'"}), 400

    product = change_product(key, change, update)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

#DELETE
@app.route("/products/<string:key>", methods=["DELETE"])
def delete_product(key):
    product = remove_product(key)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"deleted": product})

if __name__ == "__main__":
    app.run(debug=True)
