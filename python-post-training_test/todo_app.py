#!/usr/bin/python3

import psycopg2

# Database connection parameters
DB_NAME = "todoDB"
DB_USER = "dtgamer"
DB_PASSWORD = "drf64gh&-57fg32yh"
DB_HOST = "localhost"  
DB_PORT = "5432"  

def create_table():
    """Create the tasks table if it doesn't exist"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            task_name TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        );
    '''
    
    cursor.execute(create_table_query)
    conn.commit()
    
    cursor.close()
    conn.close()

def add_task(task_name):
    """Add a new task to the tasks table"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    
    add_task_query = '''
        INSERT INTO tasks (task_name, completed) VALUES (%s, %s);
    '''
    
    cursor.execute(add_task_query, (task_name, False))
    conn.commit()
    
    cursor.close()
    conn.close()

def list_tasks():
    """List all tasks from the tasks table"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    
    list_tasks_query = '''
        SELECT * FROM tasks;
    '''
    
    cursor.execute(list_tasks_query)
    tasks = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return tasks

def remove_task(task_id):
    """Remove a task from the tasks table"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()

    remove_task_query = '''
        DELETE FROM tasks WHERE id = %s;
    '''

    cursor.execute(remove_task_query, (task_id,))
    conn.commit()

    cursor.close()
    conn.close()

def main():
    create_table()

    while True:
        print("\n-- To-Do List --")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
            print("Task added!")
        elif choice == "2":
            tasks = list_tasks()
            if tasks:
                print("\n-- Tasks --")
                for task in tasks:
                    task_id, task_name, completed = task
                    status = "Done" if completed else "Not Done"
                    print(f"{task_id}. {task_name} - {status}")
            else:
                print("No tasks found.")
        elif choice == "3":
            tasks = list_tasks()
            if tasks:
                print("\n-- Tasks --")
                for task in tasks:
                    task_id, task_name, completed = task
                    status = "Done" if completed else "Not Done"
                    print(f"{task_id}. {task_name} - {status}")

                sub_choice = input("Enter task ID to remove or press Enter to go back: ")
                if sub_choice.isdigit():
                    task_id = int(sub_choice)
                    if any(task[0] == task_id for task in tasks):
                        confirmation = input("Are you sure you want to remove this task? (y/n): ")
                        if confirmation.lower() == "y":
                            remove_task(task_id)
                            print("Task removed!")
                        else:
                            print("Task removal canceled.")
                    else:
                        print("Invalid task ID. Please enter a valid task ID.")
                else:
                    print("Invalid input. Please enter a valid task ID.")
            else:
                print("No tasks found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
