FILE_CONSTANT = "../files/todos.txt"
def get_todos(file_name=FILE_CONSTANT):
    with open(file_name,"r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos,file_name=FILE_CONSTANT):
    with open(file_name,'w') as file:
        file.writelines(todos)