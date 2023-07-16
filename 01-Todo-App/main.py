user_prompt = "Enter a Todo: "

todos = []

while True:
    user_action = input("Choose add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                print(index + 1, '-', item)
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
