import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "products.json"

def load_products():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_products(products):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


products = load_products()

def all_products():
    return products

def get_product(key):
    for product in products:
        if key in (product["product_name"], product["barcode"]):
            return product
    return None

def add_product(barcode, name, quantity, brand, category, inventory):
    product = {
        "barcode": barcode,
        "product_name": name,
        "quantity": quantity,
        "brands": brand,
        "category": category,
        "inventory": inventory,
    }
    products.append(product)
    save_products(products)
    return product

def update_product(key, change, update):
    product = get_product(key)
    if product is None:
        return None

    product[change] = update
    save_products(products)
    return product

def delete_product(key):
    product = get_product(key)
    if product is None:
        return None

    products.remove(product)
    save_products(products)
    return product