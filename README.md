
---

## 📁 4. Expense Tracker (CSV) — `README.md`

```markdown
# 💸 Expense Tracker CLI

Track your daily or monthly expenses with this CLI app that stores records in a CSV file.

---

## ✨ Features
- Add expenses with date, category, and amount
- View all expenses
- Data saved persistently in `expenses.csv`

---

## ✅ Prerequisites
- Python 3.x

---

## ▶️ How to Run
1. Save the file as `expense_tracker.py`
2. Run it:
```bash
python expense_tracker.py

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
