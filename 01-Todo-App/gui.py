import functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo:")
input_box = psg.InputText(tooltip="Enter todo")
add_button = psg.Button("Add")

window = psg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
