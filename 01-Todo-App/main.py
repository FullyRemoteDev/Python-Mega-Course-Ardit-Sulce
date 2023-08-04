while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append('\n' + todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1} - {item}")

    elif user_action.startswith('edit'):
        try:
            edit_item_index = int(user_action[5:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ") + '\n'
            todos[edit_item_index - 1] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_item_index = int(user_action[9:]) - 1

            with open('todos.txt', 'r') as file:
                file.readlines()

            todo_to_remove = todos[completed_item_index].strip('\n')
            todos.pop(completed_item_index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"\nThe Todo '{todo_to_remove.title()}' was removed from the list\n"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("The command is not correct.")

print("Bye!")
