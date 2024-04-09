# Python Todo List

This is a simple command-line Todo List application written in Python. It's a great project for beginners to get started with Python programming.

## Features

The application has the following features:

- Add a task to the todo list
- View all tasks in the todo list
- Remove a task from the todo list
- Exit the application

## Code Explanation

The code is organized into several functions, each performing a specific task:

- `add_task(todo_list)`: This function asks the user for a task (a string), appends it to the `todo_list`, and prints a confirmation message.

- `view_tasks(todo_list)`: This function checks if the `todo_list` is empty. If it is, it prints a message. Otherwise, it prints all the tasks in the `todo_list`.

- `remove_task(todo_list)`: This function checks if the `todo_list` is empty. If it is, it prints a message. Otherwise, it asks the user for a task to remove, removes it from the `todo_list` if it exists, and prints a confirmation message.

The `while(True)` loop continuously asks the user for a command and calls the appropriate function based on the command. The loop breaks and the program exits when the user enters 'exit'.

## Running the Code Locally

To run this code on your local machine, follow these steps:

1. Make sure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).

2. Save the code in a file named `todo_list.py`.

3. Open a terminal/command prompt.

4. Navigate to the directory where you saved `todo_list.py`.

5. Run the command `python todo_list.py`.

You should now see the prompt "Enter a command (add, view, remove, exit): " and you can start using the application!
