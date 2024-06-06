tasks = []

def add_task():
    """
    Add a new task to the to-do list.
    """
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")
    
def view_task():
    """
    view the tasks in the to-do list.
    """
    if len(tasks) == 0:
        print("No tasks to view.")
    else:
        print("List of tasks: ")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
def update_task():
    """
    update the task in the to-do list.
    """
    if len(tasks) == 0:
        print("No task to update.")
    else:
        print('tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input('Enter the task number to update:'))
        if 0 < choice <= len(tasks):
            new_task = input('Enter the new task: ')
            tasks[choice-1] = new_task
            print('Task Updated successfully.')
        else:
            print('Invalid task number.')
    
def delete_task():
    """
    Delete a task from the to-do list.
    """
    if len(tasks) == 0:
        print("No tasks to delete. ")
    else:
        print('tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input('Enter the task number to delete:'))
        
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print('Task deleted successfully.')
        else:
            print('Invalid task number.')
            
            
            
def main():
    """
    Run the command-line to do list application.
    """
    while True:
        print('\n==== To-Do-List Application ====')
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Update task")
        print("5. Quit")
        
        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            update_task()
        elif choice == 5:
            print("Thank you for using the to-do-list application.")
            break
        else:
            print("Invalid choice please try again.")
        
    
if __name__ == "__main__":
    main()