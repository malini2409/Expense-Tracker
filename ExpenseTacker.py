# EXPENSE TRACKER
import csv

def add_expense(date, category, amount):
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added.")

def show_expenses():
    print("\nExpenses:")
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]}")

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Choose: ")

    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Category: ")
        amount = input("Amount: ")
        add_expense(date, category, amount)
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
