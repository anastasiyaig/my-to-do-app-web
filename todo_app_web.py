import time

import functions
import streamlit as st

todos_list = functions.get_todos_from_file()


def add_todo_to_the_list():
    todo = st.session_state["new_todo_input"] + '\n'
    todos_list.append(todo)
    functions.write_todos_to_file(todos_list)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity" + '\n')
st.write("Today is " + time.strftime("%b %d, %Y %H:%M:%S") + " Crush it!")

for index, item in enumerate(todos_list):

    checkbox = st.checkbox(item, key=f"checkbox_{index}")

    if checkbox:
        todos_list.pop(index)
        functions.write_todos_to_file(todos_list)
        del st.session_state[f"checkbox_{index}"]
        st.experimental_rerun()

st.text_input(
    label="Enter a todo here",
    placeholder="Add a new todo...",
    on_change=add_todo_to_the_list,
    key='new_todo_input')
