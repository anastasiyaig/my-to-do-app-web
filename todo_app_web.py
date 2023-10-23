import time

import functions
import streamlit as st

todos_list = functions.get_todos_from_file()

st.set_page_config(
    layout="centered",
    menu_items={
        'About': "This is a cool app :)"
    })


def add_todo_to_the_list():
    todo = st.session_state["new_todo_input"] + '\n'
    if todo != '\n':
        todos_list.append(todo)
    functions.write_todos_to_file(todos_list)
    st.session_state['new_todo_input'] = ""


st.title("My Todo App")
st.subheader("Plan. Complete. Simple.")
st.write("This app is to increase <b>your productivity</b>", unsafe_allow_html=True)
st.write("Today is " + time.strftime("%b %d, %Y"))

st.text_input(
    label="Enter a todo here",
    placeholder="What is your next todo?",
    on_change=add_todo_to_the_list,
    key='new_todo_input')

for index, item in enumerate(todos_list):

    checkbox = st.checkbox(item, key=f"checkbox_{index}")

    if checkbox:
        todos_list.pop(index)
        functions.write_todos_to_file(todos_list)
        del st.session_state[f"checkbox_{index}"]
        st.rerun()
