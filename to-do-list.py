class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append({"description": task_description, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def display_tasks(self):
        for idx, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{idx + 1}. {task['description']} - {status}")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add a task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. Show tasks")
        print("5. Exit")

        choice = input("\nChoose an option: \n\n 1 for Add a task \n  2 for Complete a task \n 3 for Delete a task \n 4 for show Task \n 5 for exit ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            todo_list.add_task(task_description)
        elif choice == '2':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Option Not on the Above , Try Again Please")


if __name__ == "__main__":
    main()
