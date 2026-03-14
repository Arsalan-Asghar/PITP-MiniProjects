# Week 2 - Mini Project 1 - Inventory Management System:

import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

def add_product(inventory):
    name = input("Enter product name: ")
    if name in inventory:
        print("Product already exists. Use update option.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"quantity": quantity, "price": price}
        save_inventory(inventory)
        print("Product added successfully!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nInventory List:")
        for name, details in inventory.items():
            print(f"{name} | Quantity: {details['quantity']} | Price: ${details['price']:.2f}")

def inventory_manager():
    inventory = load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

inventory_manager()
