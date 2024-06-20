from os import system, name

# define our clear function
def clear():
    if name == 'nt':     # for windows
        _ = system('cls')
    else:                # for mac and linux(here, os.name is 'posix')
        _ = system('clear')
