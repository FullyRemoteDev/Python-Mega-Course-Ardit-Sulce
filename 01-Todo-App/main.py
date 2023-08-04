def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local


while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append('\n' + todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1} - {item}")

    elif user_action.startswith('edit'):
        try:
            edit_item_index = int(user_action[5:])

            todos = get_todos()

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

            todos = get_todos()

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
