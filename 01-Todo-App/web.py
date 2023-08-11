import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['todo_text'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

st.text_input(label='Enter new todo:',
              label_visibility='hidden',
              placeholder='Add new todo...',
              on_change=add_todo, key='todo_text')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
