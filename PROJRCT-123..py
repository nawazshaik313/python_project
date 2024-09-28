import datetime

hardware_inventory = {
    "Mouse": 10,
    "Keyboard": 8,
    "Monitor": 5
}

check_in_out_logs = {}

maintenance_schedule = {
    "Mouse": datetime.date(2024, 10, 15),
    "Keyboard": datetime.date(2024, 11, 5),
    "Monitor": datetime.date(2024, 9, 30)
}

def add_hardware():
    hardware_type = input("Enter hardware name: ")
    quantity = int(input(f"Enter quantity of {hardware_type}: "))
    if hardware_type in hardware_inventory:
        print(f"{hardware_type} already exists. Use update option to modify the quantity.")
    else:
        hardware_inventory[hardware_type] = quantity
        print(f"{hardware_type} added with quantity {quantity}.")

def update_hardware():
    hardware_type = input("Enter hardware name to update: ")
    if hardware_type in hardware_inventory:
        quantity = int(input(f"Enter new quantity for {hardware_type}: "))
        hardware_inventory[hardware_type] = quantity
        print(f"{hardware_type} updated to quantity {quantity}.")
    else:
        print(f"{hardware_type} not found in inventory.")

def delete_hardware():
    hardware_type = input("Enter hardware name to delete: ")
    if hardware_type in hardware_inventory:
        del hardware_inventory[hardware_type]
        print(f"{hardware_type} deleted from inventory.")
    else:
        print(f"{hardware_type} not found in inventory.")

def view_inventory():
    if hardware_inventory:
        print("\nHardware Inventory:")
        for hardware, quantity in hardware_inventory.items():
            print(f"{hardware}: {quantity} units")
    else:
        print("Inventory is empty.")

def check_availability(hardware_type):
    if hardware_inventory.get(hardware_type, 0) > 0:
        print(f"{hardware_type} is available. Quantity: {hardware_inventory[hardware_type]}")
    else:
        print(f"{hardware_type} is not available.")

def check_out(hardware_type, user, quantity):
    if hardware_inventory.get(hardware_type, 0) >= quantity:
        hardware_inventory[hardware_type] -= quantity
        check_in_out_logs[hardware_type] = {"user": user, "checkout_date": datetime.datetime.now(), "quantity": quantity}
        print(f"{quantity} unit(s) of {hardware_type} checked out by {user}.")
    else:
        print(f"Not enough {hardware_type} available for checkout. Available quantity: {hardware_inventory.get(hardware_type, 0)}.")

def check_in(hardware_type, user, quantity):
    hardware_inventory[hardware_type] += quantity
    check_in_out_logs[hardware_type] = {"user": user, "checkin_date": datetime.datetime.now(), "quantity": quantity}
    print(f"{quantity} unit(s) of {hardware_type} checked in by {user}.")

def alert_maintenance_due(hardware_type):
    today = datetime.date.today()
    maintenance_date = maintenance_schedule.get(hardware_type)
    if maintenance_date and today >= maintenance_date:
        print(f"Alert: {hardware_type} requires maintenance (scheduled for {maintenance_date}).")
    else:
        print(f"{hardware_type} does not require maintenance yet.")

def sell_hardware():
    hardware_type = input("Enter hardware name to sell: ")
    if hardware_type in hardware_inventory:
        sell_quantity = int(input(f"Enter number of {hardware_type} units to sell: "))
        if hardware_inventory[hardware_type] >= sell_quantity:
            hardware_inventory[hardware_type] -= sell_quantity
            print(f"{sell_quantity} unit(s) of {hardware_type} sold.")
        else:
            print(f"Insufficient stock of {hardware_type}. Available quantity: {hardware_inventory[hardware_type]}.")
    else:
        print(f"{hardware_type} not found in inventory.")


def main():
    while True:
        print("\nOptions:")
        print("1. Add Hardware")
        print("2. Update Hardware")
        print("3. Delete Hardware")
        print("4. View Inventory")
        print("5. Sell Hardware")
        print("6. Check Out Hardware")
        print("7. Check In Hardware")
        print("8. Check Maintenance Due")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_hardware()
        elif choice == '2':
            update_hardware()
        elif choice == '3':
            delete_hardware()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            sell_hardware()
        elif choice == '6':
            hardware_type = input("Enter hardware to check out: ")
            user = input("Enter user name: ")
            quantity = int(input(f"Enter quantity of {hardware_type} to check out: "))
            check_out(hardware_type, user, quantity)
        elif choice == '7':
            hardware_type = input("Enter hardware to check in: ")
            user = input("Enter user name: ")
            quantity = int(input(f"Enter quantity of {hardware_type} to check in: "))
            check_in(hardware_type, user, quantity)
        elif choice == '8':
            hardware_type = input("Enter hardware to check maintenance: ")
            alert_maintenance_due(hardware_type)
        elif choice == '9': 
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
