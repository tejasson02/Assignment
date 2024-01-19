class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def delete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f'Task "{task}" deleted.')
                break
        else:
            print(f'Task "{task}" not found.')

    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f'Task "{task}" marked as completed.')
                break
        else:
            print(f'Task "{task}" not found.')

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, t in enumerate(self.tasks, start=1):
                status = "Completed" if t["completed"] else "Not Completed"
                print(f"{index}. {t['task']} - {status}")
        else:
            print("No tasks in the list.")


# Main program
todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. Delete Task\n3. Mark Task as Completed\n4. Show Tasks\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        todo_list.add_task(task_name)
    elif choice == "2":
        task_name = input("Enter task name to delete: ")
        todo_list.delete_task(task_name)
    elif choice == "3":
        task_name = input("Enter task name to mark as completed: ")
        todo_list.mark_completed(task_name)
    elif choice == "4":
        todo_list.show_tasks()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
