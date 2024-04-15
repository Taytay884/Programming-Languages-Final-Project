# Programming Languages Final Project

by Itay Ben Shmuel, Kristina Kolesnyk, Doron Ben Zaken

### Assignment file

The assignment can be found in `finalProject2024New.pdf`.

### Documentation & Answers for the assignment

[Google Doc](https://docs.google.com/document/d/18LzRqjkmaxeEk0OPAKSMulB_E3oUl3rgVXZwKjL-xFg/edit?usp=sharing)

### In order to run the dynamic interpreter

- run in the terminal `python3 ./main.py`

### In order to test cases for python programs

- run in the terminal `python3 ./tests.py`

### In order to add more test cases

- Go to `tests.py`
- Add variable for your test case for example let's call it `test_case` and set there your program as a string.
- Add another variable `test_case_result` and set there a result string.
- Go to the bottom of the file
- Add there:

```
    print("------[START - Test case]------")
    run_program(test_case, test_case_result)
    reset_variables(variables)
    print("------[END - Test case]------")
    print()
```
