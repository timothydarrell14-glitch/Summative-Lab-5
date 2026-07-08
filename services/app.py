## IMPORT DATA ##
import json
from pathlib import Path
from services import all_products, add_product, update_product, delete_product, get_product

curr_dir = Path(__file__).parent
parent_dir = curr_dir.parent
data = parent_dir /"data"/"products.json"
# products = []

# ## LOAD DATA ##
# def load_data():
#     global products
#     with open(data, "r") as f:
#         products = f.read()
#         return products

## SAVE DATA ##
def save_data():
    with open(data, "w", encoding="utf-8") as f:
        json.dump(f)

## CLI ##
def cli_run():
    try:
        while True:
            print("======CLI======")
            print()
            print()
            print("1. All Products")
            print("2. Add Product")
            print("3. Search for Product")
            print("4. Update Product")
            print("5. Delete Product")
            print("6. More information about a product")
            print("7. Save data")
            print("8. Exit")
            print()
            print()

            choice = input("Enter a number----").strip()         
            
            if choice == "1":
                all_products()

                # ADD #
            if choice == "2":
                global product
                barcode = input("Enter the barcode of the product-----").strip()
                name = input("Enter the name of the product-----").strip()
                quantity = input("Enter the quantity of the product-----").strip()
                brand = input("Enter the brands of the product----").strip()
                category = input("Enter the category of the product").strip()
                inventory = int(input("Enter the current stock of the product"))
                add_product(barcode, name, quantity, brand, category, inventory)
                
                # SEARCH #
            if choice == "3":
                key = input("Please enter barcode or name of the product---").strip()
                get_product(key)

                # UPDATE #
            if choice == "4":
                key = input("Please enter barcode or name of the product---").strip()
                change = input("Please enter what you would like to change about the product---").strip()
                update = input("Please enter change to be implemented----").strip
                update_product(key, change, update)
                save_data()

                # DELETE #
            if choice == "5":
                key = input("Please enter the name or barcode of the product to delete")
                delete_product(key)
                save_data()

            if choice == "6":
                key = input("Please enter name or barcode of the product----").strip()
                return f"https://world.openfoodfacts.org/api/v3/product/{key}"

            if choice == "7":
                save_data()

            if choice == "8":
                save_data()
                break


    finally:
        save_data()