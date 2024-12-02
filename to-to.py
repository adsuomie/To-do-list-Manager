class Task:
    def __init__(self, id, name, done=False):
        self.id = id
        self.name = name
        self.done = done

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'done': self.done
        }

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            return [Task(**task) for task in tasks]
    return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump([task.to_dict() for task in tasks], file)

def add_task(tasks):
    id = len(tasks) + 1
    name = input("Enter task name: ")
    tasks.append(Task(id, name))
    save_tasks(tasks)

def view_tasks(tasks):
    for task in tasks:
        status = "Done" if task.done else "Not Done"
        print(f"{task.id}. {task.name} [{status}]")

def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task.id == task_id:
            task.name = input("Enter new task name: ")
            save_tasks(tasks)
            return
    print("Task not found!")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return
    print("Task not found!")

def mark_task_done(tasks):
    task_id = int(input("Enter task ID to mark as done: "))
    for task in tasks:
        if task.id == task_id:
            task.done = True
            save_tasks(tasks)
            return
    print("Task not found!")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_done(tasks)
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

