#  Python-Internship-2026 | DecodeLabs 

**Intern:** Putti Reddy Hemasree | **Batch:** 2026  
**Role:** Junior Python Developer @ DecodeLabs

## Project 1: To-Do List App

### **Goal**
Build a program where users can add tasks to a list and view them using pure Python logic.

### **Key Skills Demonstrated**
- **Data Management**: Storing multiple items in a single variable
- **Python Lists**: Using `append()` for O(1) operations  
- **Loops**: `for` loop with `range(len())` to print all tasks

### **Features**
1. **Add Task** → `tasks.append(new_task)`
2. **View All Tasks** → Numbered list display with empty check
3. **Exit** → `break` to close the application

### **How to Run**
```bash
todo.py
```
### **Sample Output**
```
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 1
Enter the task: learn python basics
Task added successfully

1. Add Task
2. View Tasks
3. Exit
Enter your choice: 1
Enter the task: submit decode labs project
Task added successfully

1. Add Task
2. View Tasks
3. Exit
Enter your choice: 2

--- Your Tasks ---
1. learn python basics
2. submit decode labs project

1. Add Task
2. View Tasks
3. Exit
Enter your choice: 3
Exiting program
```
### **Status:** completed
-----------------
## ** Project 2: Expense Tracker**

### **Goal**
Build a program where users can enter expense amounts and the program adds them up to display the Total Spent using pure Python logic.

### **Key Skills Demonstrated**
- **Data Accumulation**: Storing and updating a running total using an accumulator variable
- **Math Operations**: Using `total = total + new_expense` for continuous addition
- **Loops**: `while True` loop for continuous data entry until user types 'done'
- **Error Handling**: `try-except` block to handle invalid non-numeric inputs

### **Features**
1. **Add Expense** → Takes numeric input and adds to total
2. **Input Validation** → Rejects negative numbers and non-numeric text
3. **Running Total** → Displays updated total after each entry
4. **Exit** → Type `done` to break loop and show final total

### **How to Run**
```bash
tracker.py
```
### **Sample Output**
```
Enter expense amount: 100
Added: 100.0
Enter expense amount: 50
Added: 50.0
Enter expense amount: done
TOTAL SPENT: 150.0
```
### **Status:** completed
-------------
