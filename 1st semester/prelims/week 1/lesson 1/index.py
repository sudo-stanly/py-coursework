#LESSON 1: PYTHON VARIABLES: - SUMMARY -

"""
    1.Variables:
    -Used to store data values.
    -can change type after being declared.
    -CASTING:
       -int()
       -str()
       -float()
    
    2.Variable Rules:
    -Case-sensitive
    -Must start with a letter or _
    -Can only contain letters, numbers, _
    -Can't use Python keywords
    
    3.Variable Naming Conventions:
    -camelCase -> myVariableName
    -PascalCase -> MyVariableName
    -snake_case -> my_variable_name
    -CONSTANTS -> PI = 3.14
    
    4.Assigning values
    - x, y, z = "apple", "banana", "cherry"
    - x = y = z = "orange"
    - fruits = ["apple", "banana", "cherry"]; x, y , z = fruits
"""

x, y, z = "apple", "banana", "cherry"; print("original x:"+x+" y:"+y+" z:"+z); x, y, z = z, x, y; print("swapped x:"+x+" y:"+y+" z:"+z);