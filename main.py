from variables import *
from engine import *

exit_command = 'exit'


def dynamic_interpreter():
    print("Welcome to our language dynamic interpreter, \n" +
          "in this command prompt you will be able to execute *Simple* commands like variable initializations and " +
          "aritmetic operations ONLY.\n" +
          "Lets start: \n")
    print(f"Enter as many commands as you like, to finish the session type: '{exit_command}'")

    command = ''
    session_is_running = True
    while session_is_running:
        command = input("next command >>> ")
        if command.lower() != exit_command.lower():
            run_program_line(command)
        else:
            session_is_running = False
    print(f"memory state: \n {variables}")
    reset_variables(variables)
    print(f"Goodbye :)")


if __name__ == '__main__':
    try:
        dynamic_interpreter()
    except CustomError as e:
        print(f"\nExiting due to an error: {e}")
        exit(1)


