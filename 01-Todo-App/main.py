# from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append('\n' + todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1} - {item}")

    elif user_action.startswith('edit'):
        try:
            edit_item_index = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ") + '\n'
            todos[edit_item_index - 1] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_item_index = int(user_action[9:]) - 1

            todos = functions.get_todos()

            todo_to_remove = todos[completed_item_index].strip('\n')
            todos.pop(completed_item_index)

            functions.write_todos(todos)

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
