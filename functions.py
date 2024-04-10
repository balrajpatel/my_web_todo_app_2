FILEPATH = 'todo.txt'
def get_todos(filepath = FILEPATH) :
    """read text files and return the list of todo itmes"""
    with open(FILEPATH, 'r') as local_file:

        local_todos = local_file.readlines()
    return local_todos

#help(get_todos) Docstring useage

def write_todos(local_todos, filepath=FILEPATH) :
    """wrtie todo items list in text flie"""
    with open(FILEPATH, 'w') as local_file:
        local_file.writelines(local_todos)
