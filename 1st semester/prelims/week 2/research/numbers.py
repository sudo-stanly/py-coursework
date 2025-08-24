# -> PYTHON NUMBERS

#* THREE TYPES OF NUMERIC TYPES IN PYTHON:
# int, float, complex

#* example:
x = 1    #* -> int
y = 2.8  #* -> float
z = 1j   #* -> complex

#* TO VERIFY TYPE OF ANY OBJECT IN PYTHON, USE THE - type() - function
#print(f"x is a type of {type(x)}     : {x}")
#print(f"y is a type of {type(y)}   : {y}")
#print(f"z is a type of {type(z)} : {z}")


#* Int: int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

# print(f"x is a type of {type(x)}     : {x}")
# print(f"y is a type of {type(y)}   : {y}")
# print(f"z is a type of {type(z)} : {z}")


#* Float: or "floating point number" is a number, positive or negative, containig one or more decimals.
x = 1.10
y = 1.0
z = -35.59

# print(f"x is a type of {type(x)}     : {x}")
# print(f"y is a type of {type(y)}   : {y}")
# print(f"z is a type of {type(z)} : {z}")


#Float can also be scientific numbers with an "e" to indicate the power 10.
x = 35e3
y = 12E4
z = -87.7e100

# print(f"x is a type of {type(x)}     : {x}")
# print(f"y is a type of {type(y)}   : {y}")
# print(f"z is a type of {type(z)} : {z}")


#* Complex: Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

# print(f"x is a type of {type(x)}     : {x}")
# print(f"y is a type of {type(y)}   : {y}")
# print(f"z is a type of {type(z)} : {z}")

#* Type Conversion: You can convert from one type to another with the int(), float(), and complex() methods:
x = 1       # int
x = 2.8     # float
z = 1j      # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
#c = complex(z)

# print(a)
# print(b)
#print(c) #* -> you cannot convert complex numbers into another type

#* RANDOM NUMBER:
#Python does not have a random() dunction to make a random numner, but Python has a built-in module called random that can be used to make random numbers.

import random
#print(random.randrange(1, 10))

x = 10 + random.randint()
print(x)
