import functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo:")
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_button = psg.Button('Add')
list_box = psg.Listbox(values=functions.get_todos(),
                       key='todos',
                       enable_events=True,
                       size=(45, 10))
edit_button = psg.Button('Edit')

app_layout = [[label], [input_box, add_button], [list_box, edit_button]]

window = psg.Window('My To-Do App',
                    layout=app_layout,
                    font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case psg.WIN_CLOSED:
            break


window.close()
