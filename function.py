TODO_FILE ="../files/todos.txt"

def read_todos(todos_file=TODO_FILE):
    with open(todos_file,'r') as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(content,todos_file=TODO_FILE):
    with open(todos_file,'w') as file:
        file.writelines(content)

