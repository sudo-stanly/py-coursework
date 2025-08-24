"""
    !A variable is created the moment you first assign a value to it.
"""
# *example 1:
#x, y = 5, "John Doe"; print(x, y);


# *example 2:
"""
    ! Variables do not need to be declared with any particular type, 
    ! and can even change type after they have been set.
"""
x = 4 # -> x is of type int
#print(type(x), "x:",x)

x = "Sally" # -> x is now of type str
#print(type(x), "x:",x)



""" 
    ! CASTING: this is when you want to specify the data type of a variable,
    ! this can be done with casting.
"""
#* example 1:
x,y,z = str(3), int(3), float(3) # x -> '3', y -> 3, z -> 3.0
#print("x:",x," y:",y," z:",z)


"""
    ! CASE SENSITIVE: Variable names are case-sensitive
"""
#* example 1:
a = 4; A = "Sally"; #A will not overwrite a
#print("a:",a,"\nA:",A)