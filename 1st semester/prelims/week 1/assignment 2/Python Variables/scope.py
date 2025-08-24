"""
    !LOCAL & GLOBAL VARIABLE SCOPE
"""
globalVar = "I am global"

def myFunc():
    localVar = "I am local"
    #print(globalVar)
    
myFunc()
#print(localVar) # -> localVar is not defined within this scope


"""
    ! If you create a variable with the same name inside a function, this variable will be local, 
    ! and can only be used inside the function. The global variable with the same name will remain as it was, 
    ! global and with the original value.
"""
x = "Hello, World!"
def myFuncFunc():
    x = "I am now local"
    #print(x)
myFuncFunc()
#print("I am global again: ", x)



"""
    ! Global keyword: Normally, when you create a variable inside a function, 
    ! that variable is local, and can only be used inside that function.
"""
def globalFunc():
    global y
    y = "awsome"
globalFunc()
#print("Python is ", y)


#* Also, use the global keyword if you want to change a global variable inside a function.
z = "awsome"
def globalFuncFunc():
    global z
    z = "fantastic"
globalFuncFunc()
print("Python is ", z)