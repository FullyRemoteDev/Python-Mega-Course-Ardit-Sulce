while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1} - {item}")

        case 'edit':
            edit_item_index = int(input("Enter the number of the todo to edit: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ") + '\n'
            todos[edit_item_index - 1] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            completed_item_index = int(input("Enter the number of the completed todo: ")) - 1

            with open('todos.txt', 'r') as file:
                file.readlines()

            todo_to_remove = todos[completed_item_index].strip('\n')
            todos.pop(completed_item_index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"\nTodo '{todo_to_remove}' was removed from the list\n"
            print(message)

        case 'exit':
            break

        case _:
            print("Hey, you entered an unknown command")

print("Bye!")
