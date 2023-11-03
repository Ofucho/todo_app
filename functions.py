FILEPATH = 'todos.txt'


def openFile(task_file=FILEPATH):
    """
    Read a text file and return a list
    of todo items
    """

    with open(task_file, 'r') as todo_file:
        todo_file = todo_file.readlines()
    return todo_file


# using two arguments
def writeFile(tasks, task_file=FILEPATH):
    """Write todos to the text file
    function does not return anything because no output is needed from it
    """
    with open(task_file, 'w') as todo_file:
        todo_file.writelines(tasks)


if __name__ == "__main__":
    print(openFile())
