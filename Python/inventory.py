inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s)")

def view_inventory():
    for item,quantity in inventory.items():
        print(f"{item}: {quantity}")

def update(item, quantity):
    if item in inventory:
        inventory[item] = quantity
    else:
        print("Item not found.")

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            add_item(item, quantity)
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            item = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            update(item, quantity)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    manage_inventory()
