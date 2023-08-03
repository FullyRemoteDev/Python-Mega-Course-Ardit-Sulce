while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append('\n' + todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1} - {item}")

    elif 'edit' in user_action:
        edit_item_index = int(user_action[5:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ") + '\n'
        todos[edit_item_index - 1] = new_todo

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        completed_item_index = int(user_action[9:]) - 1

        with open('todos.txt', 'r') as file:
            file.readlines()

        todo_to_remove = todos[completed_item_index].strip('\n')
        todos.pop(completed_item_index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"\nTodo '{todo_to_remove}' was removed from the list\n"
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("The command is not correct.")

print("Bye!")
