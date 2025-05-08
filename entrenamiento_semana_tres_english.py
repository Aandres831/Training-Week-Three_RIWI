
def menu():
    #decision = 0
    print("-------------------------------------------- MENU -------------------------------------------------------")
    print("Welcome to the inventory system of RIWI.")
    print("1. Add Product \n" \
    "2. Search Product \n" \
    "3. Update Price \n" \
    "4. Delete Product \n" \
    "5. Total Value Of Inventory \n" \
    "0. Exit")
    print("----------------------------------------------------------------------------------------------------------")


inventario = []

#------------------------------------------------------------------------------------------------------------------
def add_product():
    while True:       
        try:
            name = input("Enter the product name: ").strip().lower()
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the quantity of the product: "))
            product = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            inventario.append(product)  
            break
        except ValueError:
            print("Invalid Enter, try again.")
    print(f"Product {name} added succesfully, price: {price} and quantity is {quantity}")


def search_product():
    print("     Search Product")
    name = input("Enter the name of the product to consult: ").lower()
    for producto in inventario:
        if producto["name"].lower() == name:
            print(f"Prodcut: {producto['name']}")
            print(f"price: {producto['price']}")
            print(f"Quantity: {producto['quantity']}")
            return

    print("Product not found.")


def update_product():
    print("     Update Price ")
    name_product = input("Enter the product name: ").lower()
    new_price = float(input("Enter the new product price: "))
    for act in inventario:
        if act["name"] == name_product:
            act["price"] = new_price
            print(f"Price updated, the new price of {name_product} is {new_price} ")
        else:
            print(f"We can't update the price, We can't found your product {act["name"]}, please try again. ")


def delete_product():
    print("     Delete Product ")
    delete_product = input("Enter the product to delete: ").lower()
    for delet in inventario:
        if delet["name"] == delete_product:
            delet_decision = input("Are you sure? Press S/N -> ").lower()
            if delet_decision == "s":
                inventario.remove(delet)
                print("Delete Complete")
                return
            elif delet_decision == "n":
                print("Deleted Cancelled ")
                return
            else:
                print("Enter a S/N decision")
                return
        else:
            print(f"We can't found your product  ")


def calculate_total_value():
    total_inventory = sum (map (lambda product: product.get("price", 0) * product.get("quantity", 1), inventario))
    print(f"Total inventory value is: {total_inventory}")
    

def exit_program():
    print("Exit The Program")
    print("See you soon!")

# options = {
#     1: add_product,
#     2: search_product,
#     3: update_product,
#     4: delete_product,
#     5: calculate_total_value,
#     0: exit_program
# }


while True:
    menu()
    try:
        decision = int(input("Enter a menu option: "))

        if decision == 1:
            add_product()
        elif decision == 2:
            search_product()
        elif decision == 3:
            update_product()
        elif decision == 4:
            delete_product()
        elif decision == 5:
            calculate_total_value()
        elif decision == 0:
            exit_program()
            break
        else:
            print("Invalid option. Please try again , Enter a valid menu option.")
            
    except ValueError:
        print("Enter a valid menu option: ")