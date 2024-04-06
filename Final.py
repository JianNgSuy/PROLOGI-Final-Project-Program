# Enhanced security and anti-fraud protection
userCredentials = {
    "Miguel": "password",
    "Andrei": "123456",
    "Abad": "iloveyou"
}

# Login input and validation
def loginAccess():
    access = 'N'
    while (str(access)).upper() != 'Y':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in userCredentials and userCredentials[username] == password:
            access = 'Y'
        else:
            print("\nInvalid username or password. Please try again.")
            access = 'N'

    return access, username

# Menu items
menuItems = {
    1: {"code": '01', "name": "Intel i3", "price": 150, "stock": 7},
    2: {"code": '02', "name": "Intel i5", "price": 250, "stock": 5},
    3: {"code": '03', "name": "Intel i7", "price": 350, "stock": 3},
    4: {"code": '04', "name": "AMD Ryzen 3", "price": 150, "stock": 7},
    5: {"code": '05', "name": "AMD Ryzen 5", "price": 250, "stock": 5},
    6: {"code": '06', "name": "AMD Ryzen 7", "price": 350, "stock": 3},
    7: {"code": '07', "name": "Nvidia RTX 4060", "price": 400, "stock": 15},
    8: {"code": '08', "name": "Nvidia RTX 4070", "price": 550, "stock": 13},
    9: {"code": '09', "name": "Nvidia RTX 4080", "price": 700, "stock": 10},
    10: {"code": '10', "name": "AMD MoBo", "price": 200, "stock": 10},
    11: {"code": '11', "name": "Intel MoBo", "price": 200, "stock": 10},
    12: {"code": '12', "name": "16gb RAM stick", "price": 80, "stock": 30},
    13: {"code": '13', "name": "32gb RAM stick", "price": 150, "stock": 16},
    14: {"code": '14', "name": "Power Supply", "price": 120, "stock": 30},
    15: {"code": '15', "name": "500gb SSD  ", "price": 100, "stock": 30},
    16: {"code": '16', "name": "1tb SSD    ", "price": 190, "stock": 20},
    17: {"code": '17', "name": "500gb HDD  ", "price": 50, "stock": 50},
    18: {"code": '18', "name": "1tb HDD    ", "price": 80, "stock": 40},
    19: {"code": '19', "name": "Gaming Case", "price": 100, "stock": 15},
    20: {"code": '20', "name": "Office Case", "price": 40, "stock": 15},
}

# Function to display menu items
def displayMenu():
    print("\nMenu Items:")
    print("Code\tName\t\t\tPrice\tStock")
    for item in menuItems.values():
        print(f"{item['code']}\t{item['name']}\t\t${item['price']}\t{item['stock']}")

# Function to take orders
def takeOrder():
    order = {}
    while True:
        code = input("Enter item code (0 to finish order): ")
        if code == '':
            print("No input provided. Please enter an item code.")
            continue
        elif code == '0':
            break
        elif int(code) not in menuItems:
            print("Invalid item code. Please try again.")
            continue

        quantity = input("Enter quantity: ")
        if quantity == '':
            print("No input provided. Please enter a quantity.")
            continue
        quantity = int(quantity)  # Convert quantity to integer
        if quantity > menuItems[int(code)]['stock'] or quantity < 0:
            print("Insufficient stock. Please enter a valid quantity.")
            continue
        order[int(code)] = quantity
        menuItems[int(code)]['stock'] -= quantity  # Subtract quantity from stock
    return order

# Function to print receipt
def printReceipt(order):
    totalPrice = 0
    print("\nReceipt:")
    print("Code\tName\t\tQuantity\tPrice")      
    for code, quantity in order.items():
        item = menuItems[code]
        subtotal = item['price'] * quantity
        totalPrice += subtotal
        print(f"{item['code']}\t{item['name']}\t{quantity}\t\t{subtotal}")
    print(f"\nTotal Price: ${totalPrice}")

    # Discount option
    discountChoice = input("\nAre you eligible for a discount? (Y/N): ")
    if discountChoice.upper() == 'Y':
        discountAmount = totalPrice * 0.1  # 10% discount
        totalPrice -= discountAmount
        print(f"Discount Applied: ${discountAmount}")
        print(f"Discounted Price: ${totalPrice}")
    elif discountChoice.upper() == 'N':
        print(f"Total Price: ${totalPrice * 1.0}")
    else:
        print("Invalid Input. Please try again.")
            
    # Cash payment
    while True:
        cashPayment = input("\nEnter cash amount: $")
        try:
            cashPayment = float(cashPayment)
            break  # Break out of the loop if input is valid
        except ValueError:
            print("Invalid Input. Please enter a valid cash amount.")
    
    # Change calculation and validation
    change = cashPayment - totalPrice
    while change < 0:
        print("Insufficient Amount")
        cashPayment = float(input("\nEnter cash amount: $"))
        change = cashPayment - totalPrice
        
    print(f"Change: ${change:.2f}")

# Shows Options
def menuOptions():
    print("\nOptions:")
    print("1. Take Order")
    print("2. Show Menu")
    print("3. Exit")
    choice = input("\nEnter your choice: ")
    return choice

# Main function
def main():
    # Login
    print("Welcome to C0MPUT3R Parts 4 Sale!")
    access, username = loginAccess()
    
    if str(access).upper() == 'Y':
        print(f"\nAre you ready to shop {username}!")
        displayMenu()
        while True:
            choice = menuOptions()
            if choice == '1':
                order = takeOrder() # Takes Order
                if order:
                    printReceipt(order) # AFter taking order it prints receipt
            elif choice == '2':
                displayMenu() # Redisplays the Menu
                continue
            elif choice == '3':
                print(f"Thank you for shopping with us {username}!. Please Come Again!") # Exits the Programs
                break
            else:
                print("Invalid choice. Please try again.") # Default, Reprompts the User


main()
