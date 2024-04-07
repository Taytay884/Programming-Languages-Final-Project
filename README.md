# Programming Languages Final Project

by Itay Ben Shmuel, Kristina, Doron Ben Zaken

### Assignment file
The assignment can be found in `finalProject2024New.pdf`.

### Documentation
[Google Doc](https://docs.google.com/document/d/18LzRqjkmaxeEk0OPAKSMulB_E3oUl3rgVXZwKjL-xFg/edit?usp=sharing)

### In order to run the code
- run in the terminal `python3 ./main.py`

### In order to add more test cases
- Go to `tests.py`
- Add variable for your test case for example let's call it `test_case` and set there your program as a string.
- Add another variable `test_case_result` and set there a result string.
- Go to `main.py` to the bottom of the file
- Add there: 
```print("------[START - Test case]------")
    program = tests.test_case
    run_program(program)
    print(f"Expected Result:    {tests.test_case_result}")
    print(f"Result:             {variables}")
    reset_variables(variables)
    print("------[END - Test case]------")
 ```