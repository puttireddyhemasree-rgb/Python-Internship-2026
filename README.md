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
## **Project 2: Expense Tracker**

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
## Project 3: Random Password Generator

### **Goal**
Write a tool that asks the user for a password length and generates a random, complex password using letters and numbers using pure Python logic.

### **Key Skills Demonstrated**
- **Importing Modules**: Using `import random` and `import string` from Python's built-in libraries
- **String Manipulation**: Combining `string.ascii_letters + string.digits` to create character pool
- **Loops/Comprehension**: Using generator expression with `for i in range(length)` to build password
- **Built-in Functions**: `random.choice()` for random selection and `''.join()` to convert list to string

### **Features**
1. **Take Length Input** → User enters desired password length
2. **Generate Password** → Creates non-predictable password using letters and numbers
3. **Display Output** → Shows the generated secure password

### **How to Run**
```bash
password_generator.py
```
### **Sample Output**
```
Enter password length: 8
Generated Password: mK9pQ2tR
```
### **Status:** completed
------------
## Project 4: General Knowledge Quiz

### Goal
Create an interactive quiz program that asks 3 questions, tracks the user's score, and handles messy user input using pure Python logic.

### Key Skills Demonstrated
- **Control Flow**: Using `if-else` statements to check if answers are correct.
- **State Management**: Using a `score` variable that updates after each correct answer.
- **Input Sanitization**: Using `.strip()` and `.lower()` to handle spaces and case differences in user input.
- **User Input/Output**: Using `input()` to get answers and `print()` to give feedback.

### Features
1. **Ask Questions** → Presents 3 general knowledge questions to the user.
2. **Check Answers** → Compares user input against correct answers, ignoring case and extra spaces.
3. **Track Score** → Adds +1 to score for every correct answer.
4. **Display Result** → Shows the final score out of 3 at the end.

### How to Run
```bash
 quiz.py
```
### **Sample Output**
```
Question 1: What is the capital of France?
Your answer: paris 
Correct! +1 point

Question 2: Which planet is known as the Red Planet?
Your answer: mars
Correct! +1 point

Question 3: How many days are there in a leap year?
Your answer: 366
Correct! +1 point

-------------------------
Quiz Complete! Your final score is: 3/3
-------------------------
```
### **Status:** completed
