def main():
    tasks = []
    print("Welcome to the To-Do List App!")
    print("Commands: add <task>, list, remove <number>, exit")
    while True:
        command = input("Enter command: ").strip()
        if command.lower() == "exit":
            print("Goodbye!")
            break
        elif command.lower().startswith("add "):
            task = command[4:].strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("No task specified. Usage: add <task>")
        elif command.lower() == "list":
            if not tasks:
                print("No tasks in your to-do list.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
        elif command.lower().startswith("remove "):
            num_part = command[7:].strip()
            if num_part.isdigit():
                idx = int(num_part)
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("Please specify a valid task number to remove. Usage: remove <number>")
        else:
            print("Unknown command. Please use: add <task>, list, remove <number>, exit")

if __name__ == "__main__":
    main()
