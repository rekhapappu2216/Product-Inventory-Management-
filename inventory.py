inventory = {}

while True:
    print("\n--- Product Inventory Management ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product Quantity")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        inventory[name] = qty
        print("Product added successfully!")

    elif choice == "2":
        print("\nAvailable Products:")
        for product, qty in inventory.items():
            print(product, ":", qty)

    elif choice == "3":
        name = input("Enter product name to update: ")
        if name in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[name] = qty
            print("Quantity updated!")
        else:
            print("Product not found")

    elif choice == "4":
        name = input("Enter product name to delete: ")
        if name in inventory:
            del inventory[name]
            print("Product deleted!")
        else:
            print("Product not found")

    elif choice == "5":
        print("Exiting program...")
        break