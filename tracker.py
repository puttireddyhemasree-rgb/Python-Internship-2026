total_spent = 0.0
print("=== EXPENSE TRACKER ===")
print("Enter expenses one by one. Type 'done' to finish.")
while True:
    user_input = input("Enter expense amount: ")
    if user_input.lower() == 'done':
        break
    try:
        expense = float(user_input)
        if expense < 0:
            print("Expense cannot be negative. Enter positive amount.")
            continue    
        total_spent = total_spent + expense
        print(f"Added: {expense}")
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")
print("---------------------------")
print(f"TOTAL SPENT: {total_spent}")
print("---------------------------")
