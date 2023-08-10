import functions
import PySimpleGUI as psg
import time

psg.theme('DarkGrey2')

label_clock = psg.Text(text='', key='clock')
label = psg.Text(text="Type in a todo:")
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_button = psg.Button(size=2, image_source='add.png', tooltip="Add Todo", key='add')
list_box = psg.Listbox(values=functions.get_todos(),
                       key='todos',
                       enable_events=True,
                       size=(36, 9))
edit_button = psg.Button('Edit')
complete_button = psg.Button(size=4, image_source='complete.png', tooltip="Complete Todo", key='complete')
exit_button = psg.Button('Exit')

app_layout = [[label_clock],
              [label],
              [input_box, add_button],
              [list_box, edit_button, complete_button],
              [exit_button]]

window = psg.Window(title='My To-Do App',
                    layout=app_layout,
                    font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Please select an item first", font=('Helvetica', 16))
        case 'complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                psg.popup("Please select an item first", font=('Helvetica', 16))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case psg.WIN_CLOSED:
            break


window.close()
