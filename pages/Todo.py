import streamlit as st
import functions

todo_list = functions.openFile()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_list.append(todo.capitalize())
    functions.writeFile(todo_list)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is a <b>productivity</b> increase app",
         unsafe_allow_html=True)

st.text_input(label="Todo", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")

for index, item in enumerate(todo_list):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todo_list.pop(index)
        functions.writeFile(todo_list)
        del st.session_state[item]
        st.experimental_rerun()


# st.session_state
