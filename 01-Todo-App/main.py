while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1} - {item}")
        case 'edit':
            edit_item_index = int(input("Enter the number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[edit_item_index - 1] = new_todo
        case 'complete':
            completed_item_index = int(input("Enter the number of the completed todo: "))
            todos.pop(completed_item_index - 1)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")
