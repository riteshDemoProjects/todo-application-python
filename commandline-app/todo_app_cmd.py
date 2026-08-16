import function


user_action = "Enter add,show,edit,complete or exit :"

while True:
    user_input = input(user_action)

    if user_input.startswith(("Add","add")):
        todos = function.read_todos()
        #print(f"Existing todos :{todos}")
        todo = user_input[3:]
        #print(len(todo))
        if len(todo)<=0:
            todo=input("You Haven't entered your todos; Enter a todo :")
        todos.append(todo.strip()+"\n")
        function.write_todos(todos)
    elif user_input.startswith(("show","Show")):
        todos = function.read_todos()
        # for item,todo in enumerate(todos):
        #    print(f"{item+1}-{todo.strip('\n')}")
        # List Comprehension
        new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item}")
    elif user_input.startswith(("Edit","edit")):
        todos = function.read_todos()
        print("Select which todo to edit :")
        for item, todo in enumerate(todos):
            print(item + 1, todo.strip("\n"))
        todo_number = int(input("Enter the todo number :"))
        print(f"current Todo at {todo_number} is {todos[todo_number - 1].strip("\n")}")
        edited_todo = input("Enter modified todo :")
        todos[todo_number - 1] = edited_todo
        function.write_todos(todos)
    elif user_input.startswith(("Complete","complete")):
        remove_item = int(input("Enter todo number to mark as complete: "))
        todos = function.read_todos()
        todos.pop(remove_item - 1)
        function.write_todos(todos)
    else:
        break
print("Byee !!!")