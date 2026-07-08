from modules.product import (
    add_product,
    all_products,
    delete_product,
    get_product,
    products,
    save_products,
    update_product,
)


def save_data():
    save_products(products)


def show_product(product):
    if product is None:
        print("Product not found.")
        return

    for key, value in product.items():
        print(f"{key}: {value}")

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
                for product in all_products():
                    show_product(product)
                    print()

                # ADD #
            elif choice == "2":
                barcode = input("Enter the barcode of the product-----").strip()
                name = input("Enter the name of the product-----").strip()
                quantity = input("Enter the quantity of the product-----").strip()
                brand = input("Enter the brands of the product----").strip()
                category = input("Enter the category of the product").strip()
                inventory = int(input("Enter the current stock of the product"))
                product = add_product(barcode, name, quantity, brand, category, inventory)
                print("Product added:")
                show_product(product)
                
                # SEARCH #
            elif choice == "3":
                key = input("Please enter barcode or name of the product---").strip()
                show_product(get_product(key))

                # UPDATE #
            elif choice == "4":
                key = input("Please enter barcode or name of the product---").strip()
                change = input("Please enter what you would like to change about the product---").strip()
                update = input("Please enter change to be implemented----").strip()
                product = update_product(key, change, update)
                print("Product updated:")
                show_product(product)

                # DELETE #
            elif choice == "5":
                key = input("Please enter the name or barcode of the product to delete").strip()
                product = delete_product(key)
                if product is None:
                    print("Product not found.")
                else:
                    print("Product deleted.")

            elif choice == "6":
                key = input("Please enter name or barcode of the product----").strip()
                print(f"https://world.openfoodfacts.org/api/v3/product/{key}")

            elif choice == "7":
                save_data()
                print("Data saved.")

            elif choice == "8":
                save_data()
                break

            else:
                print("Please enter a number from 1 to 8.")


    finally:
        save_data()
