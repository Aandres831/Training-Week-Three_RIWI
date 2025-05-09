
def menu():
    #decision = 0
    print("-------------------------------------------- 💻 MENU 💻 -------------------------------------------------------")
    print(" Welcome to the inventory system of RIWI.")
    print("✅ 1.Add Product \n" \
    "🔎 2. Search Product \n" \
    "🔁 3. Update Price \n" \
    "❌ 4. Delete Product \n" \
    "💲 5. Total Value Of Inventory \n" \
    "🚫 0. Exit")
    print("----------------------------------------------------------------------------------------------------------")


inventario = []

#------------------------------------------------------------------------------------------------------------------
# 📦 Function to add a new product to the inventory
# ✅ Takes user input for product name, price, and quantity
# 🔄 Stores the product as a dictionary in the global `inventario` list
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


# 🔎 Function to search for a product in the inventory
# 🚀 Iterates through the inventory and compares names in lowercase
# ❌ Displays an error message if the product is not found
def search_product():
    try:
        print("     Search Product")
        name = input("Enter the name of the product to consult: ").lower()
        for producto in inventario:
            if producto["name"].lower() == name:
                print(f"Prodcut: {producto['name']}")
                print(f"price: {producto['price']}")
                print(f"Quantity: {producto['quantity']}")
                return

        print("Product not found.")
    except ValueError:
        print("Enter a value name to search. ")



# 🔁 Function to update the price of an existing product
# 🎯 Searches for the product by name and modifies its price
# ❌ Displays an error message if the product is not found
def update_product():
    try:
        print("     Update Price ")
        name_product = input("Enter the product name: ").lower()
        new_price = float(input("Enter the new product price: "))
        for act in inventario:
            if act["name"] == name_product:
                act["price"] = new_price
                print(f"Price updated, the new price of {name_product} is {new_price} ")
            else:
                print(f"We can't update the price, We can't found your product {act["name"]}, please try again. ")
    except ValueError:
        print("Enter a value name to update. ")


# ❌ Function to delete a product from the inventory
# 🔎 Searches for a matching product name and removes it
# 🛑 Requires user confirmation before deleting
def delete_product():
    try:
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
    except ValueError:
        print("Enter a value name to delete. ")


# 💲 Function to calculate the total value of inventory
# 🔄 Multiplies price and quantity for each product, then sums the total
# ❌ Displays an error message if calculation fails
def calculate_total_value():
    try:
        total_inventory = sum (map (lambda product: product.get("price", 0) * product.get("quantity", 1), inventario))
        print(f"Total inventory value is: {total_inventory}")
    except ValueError:
        print("Right now we can't show you the total value of inventory, please try again later. ")
    

# 🚪 Function to exit the program gracefully
# 🛑 Prints a farewell message before terminating the loop
def exit_program():
    try:
        print("Exit The Program")
        print("See you soon!")
    except ValueError:
        print("We can't exit, try again. ")

# options = {
#     1: add_product,
#     2: search_product,
#     3: update_product,
#     4: delete_product,
#     5: calculate_total_value,
#     0: exit_program
# }


while True:
    menu()  # 📜 Display the menu options
    
    try:
        decision = int(input("🕒 Enter a menu option: "))  # ⌨️ Get user input for action selection

        # 🔀 Decision branching based on user input
        if decision == 1:
            add_product()  # ➕ Add a new product
        elif decision == 2:
            search_product()  # 🔍 Search for a product
        elif decision == 3:
            update_product()  # 🔁 Update product price
        elif decision == 4:
            delete_product()  # ❌ Delete a product
        elif decision == 5:
            calculate_total_value()  # 💲 Calculate total inventory value
        elif decision == 0:
            exit_program()  # 🚪 Exit the program
            break  # 🔄 End the loop
        else:
            print("Invalid option. Please try again , Enter a valid menu option.")  # ⚠️ Error message for invalid input
            
    except ValueError:
        print("Enter a valid menu option: ")  # 🚫 Catch input errors (non-numeric)
