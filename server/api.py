from flask import Flask, jsonify, request

app = Flask(__name__)

#GET
@app.route("/inventory", methods=["GET"])
def all_products():
    pass


#GET_SINGLE
@app.route("/inventory/<int:id>", methods=["GET"])
def get_product():
    pass


#POST
@app.route("/inventory", methods=["POST"])
def add_product():
    pass


#PATCH
@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_product():
    pass


#DELETE
@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_product():
    pass

if __name__ == "__main__":
    app.run(debug=True)
