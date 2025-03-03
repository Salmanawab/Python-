print ("Question 1: Arithmetic Operations")
# Addition
a = 10
b = 30
print ("Add:",a + b)
# Subtraction
a = 30
b = 10
print ("Sub:",a - b)
# Multiplication
a = 10
b = 30
print ("Mul:",a * b)
# Division
a = 50
b = 30
print ("Div:",a / b)
# In python the division operator always returns a floating point even if the result is a whole number becouse the python division operator perform TRUE division.It returns the exact result of the division
# Modulus
a = 40
b = 30
print ("Mod:",a % b)
print("Question 2: Relational (Comparison) Operators")
# Equal to
a = 10
b = 30
print ("Equal to:",a == b)
# Not Equal to
a = 10
b = 30
print ("Not Equal to :",a != b)
# Less than
a = 10
b = 30
print ("Less than:",a < b)
# Greater than
a = 10
b = 30
print ("Grater than:",a > b)
print("Question 3: Assignment Operators")
# Initializing a variable
x = 10
y = 5
# Using different assignment operators
print("Initial values: x =", x, ", y =", y)
x += 5   
print("After x += 5: x =", x)
x -= 3   
print("After x -= 3: x =", x)
x *= 2   
print("After x *= 2: x =", x)
x /= 4   
print("After x /= 4: x =", x)
x //= 2  
print("After x //= 2: x =", x)
x %= 3   
print("After x %= 3: x =", x)
x **= 2  
print("After x **= 2: x =", x)
print("Question 4: Logical Operators")
# Define Boolean Variables
a = True
b = False
c = True
# Evaluate Logical Conditions
and_result = a and b
or_result = a or b
not_result = not a
xor_result = (a and not b) or (not a and b)
print("a and b =", and_result)
print("a or b =", or_result)
print("not a =", not_result)
print("XOR result =", xor_result)
