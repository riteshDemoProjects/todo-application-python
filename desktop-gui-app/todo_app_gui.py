from idlelib import window

import FreeSimpleGUI as sg
import function

label = sg.Text("Type in TO-Do")
input_box= sg.Input(key="todo")
add_button = sg.Button("Add")
#dispaly_box = sg.
gui_window = sg.Window('My To-Do App',[[label],[input_box,add_button]],font=('helvica',20))
while True:
    event,value = gui_window.read()
    match event:
        case "Add":
            todos = function.read_todos()
            todos.append(value.get("todo")+"\n")
            function.write_todos(todos)
            print(todos)
        case sg.WIN_CLOSED:
            break
gui_window.close()
