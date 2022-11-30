def get_todos():
    """" Fetches and returns saved todos."""
    with open("todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos):
    """"Writes todo to saved todos."""
    with open("todos.txt", 'w') as file:
        file.writelines(todos)

if __name__=="__main__":
    print(get_todos())