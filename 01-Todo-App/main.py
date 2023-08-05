def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos('todos.txt')
        todos.append('\n' + todo)

        write_todos("todos.txt", todos)

    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1} - {item}")

    elif user_action.startswith('edit'):
        try:
            edit_item_index = int(user_action[5:])

            todos = get_todos('todos.txt')

            new_todo = input("Enter new todo: ") + '\n'
            todos[edit_item_index - 1] = new_todo

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_item_index = int(user_action[9:]) - 1

            todos = get_todos('todos.txt')

            todo_to_remove = todos[completed_item_index].strip('\n')
            todos.pop(completed_item_index)

            write_todos("todos.txt", todos)

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
