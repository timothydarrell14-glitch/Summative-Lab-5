## IMPORT DATA ##

## LOAD DATA ##
def load_data():
    pass
## SAVE DATA ##
def save_data():
    pass


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
            print("6. Save data")
            print("7. Load data")
            print("8. Exit")
            print()
            print()

            choice = input("Enter a number----").strip()         
            
            if choice == "1":
                load_data()

                # ADD #
            if choice == "2":
                save_data()

                # SEARCH #
            if choice == "3":
                pass

                # UPDATE #
            if choice == "4":
                save_data()

                # DELETE #
            if choice == "5":
                save_data()

            if choice == "6":
                save_data()

            if choice == "7":
                load_data()

            if choice == "8":
                save_data()
                break


    finally:
        pass

# cli_run()


