#!/usr/bin/python3
def display_tasks(tasks):
    """
    Displays the current tasks in the to-do list.

    Args:
        tasks (list): List of tasks to be displayed.
    """
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, new_task):
    """
    Adds a new task to the to-do list.

    Args:
        tasks (list): List of tasks.
        new_task (str): New task to be added.
    """
    tasks.append(new_task)
    print(f"Task '{new_task}' added to the list.")

def remove_task(tasks, task_index):
    """
    Removes a task from the to-do list.

    Args:
        tasks (list): List of tasks.
        task_index (int): Index of the task to be removed.
    """
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index.")

def main():
    """
    Main function to run the to-do list application.
    """
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
