
#Bank Account Management System
Balance = 10000
Transactions = []

while True:
    print("\n 1. Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Transaction History")
    print("5.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Balance:$",Balance)

    elif choice == '2':

        amount = float(input("Enter amount to deposit :"))

        if amount <=0:
            print("Enter a valid amount")

        elif amount > 0:
            Balance += amount
            Transactions.append({"type": "Deposit", "amount": amount})

            print("Deposit successful. New balance: $", Balance)

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > Balance:
            print("Insufficient balance")
        else:
            Balance -= amount
            Transactions.append({"type": "Withdrawal", "amount": amount})
            print("Withdrawal successful. New balance: $", Balance)

    elif choice == '4':
        for t in Transactions:
            print(t)

    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")



#Library Management System

books = {
    "Python": True,
    "C Programming": True,
    "Data Structures": True,
    "AI Basics": True
}

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Display Unavailable Books")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")

        if book in books:
            if books[book]:
                books[book] = False
                print("Book issued")
            else:
                print("Book unavailable")
        else:
            print("Book not found")

    elif choice == 2:
        book = input("Enter book name: ")

        if book in books and not books[book]:
            days = int(input("Enter late days: "))
            fine = days * 5
            books[book] = True
            print("Book returned")
            print("Fine:", fine)
        else:
            print("Invalid return")

    elif choice == 3:
        for book, available in books.items():
            if not available:
                print(book)

    elif choice == 4:
        break
        
#Electricity  Bill Calculator

def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 200 * 7 + (units - 300) * 10

    fixed_charge = 100

    if units > 500:
        surcharge = bill * 0.10
    else:
        surcharge = 0

    return bill + fixed_charge + surcharge


name = input("Enter consumer name: ")
units = float(input("Enter units consumed: "))

amount = calculate_bill(units)

print("\n----- ELECTRICITY BILL -----")
print("Consumer:", name)
print("Units:", units)
print("Total Bill:", amount)