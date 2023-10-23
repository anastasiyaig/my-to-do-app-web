FILEPATH = 'files/todos.txt'


def get_todos_from_file(filepath=FILEPATH):
    """Read the text file and return the list of items in that file as a list"""
    with open(filepath, 'r') as f:
        todos_list_from_file = f.readlines()
    return todos_list_from_file


def write_todos_to_file(new_todos_list, filepath=FILEPATH):
    """Write the list of items in a text file"""
    with open(filepath, 'w') as f:
        f.writelines(new_todos_list)


if __name__ == "__main__":
    print("this was executed directly from functions.py")
