from variables import *
from blocks import *
from engine import *

exit_command = 'exit'

def dynamic_interpreter():
    command = ''
    session_is_running = True
    print(f"Enter your commands, to finish type: {exit_command}")
    while(session_is_running):
        command = input("next_command >>> ")
        if(command.lower()  != exit_command.lower()):
            run_program_line(command)
        else:
            session_is_running = False
    print(f"memory state: \n {variables}")
    reset_variables(variables)

if __name__ == '__main__':
   print("Welcome to our language dynamic interpreter, \n" +
         "in this command prompt you will be able to exectute *Simple* commands like variable initializations and aritmetic operations ONLY.\n"+
         "Lets start: \n")
   dynamic_interpreter()
