print("<b>VARIABLES AND BASIC DATA MANIPULATION (TYPECASTING CONCEPT)</b>")
print("<h1>Personal information</h1>")
name = "Salma Nawab"
address= "Kohat City pakistan"
age = 23
degree ="BSCS"
gender = "female"
mobile_no = "03189217845"
email = "salmanawab@222gmail.com"
print("Name:",name)
print(type(name))
print("Age:",age)
print(type(age))
print("Gender:",gender)
print(type(gender))
print("Number:",mobile_no)
print(type(mobile_no))
print("Email:",email)
print(type(email))
print("Address:",address)
print(type(address))
print("Degree:",degree)
print(type(degree))
print("Swapping two variables")
a = 10      # Integer
b = 20.5    # Float
# Print the values before swapping
print("Before Swapping:")
print("a =", a, "b =", b)
# Swapping with type casting
a, b = int(b), float(a)
# Print the values after swapping
print("After Swapping:")
print("a =", a, "b =", b)
print("Different Data tyeps")
# Declaring variables with different data types
a = 10             
b = 20.5              
c = "Hello, World!"  
d = True            
e = [1, 2, 3, 4, 5]    
f = (1, 2, 3)         
g = {"key": "value"}   
# Displaying the variables with their data types
print("Variable: integer_var =", a, "Data Type:", type(a))
print("Variable: float_var =", b, "Data Type:", type(b))
print("Variable: string_var =", c, "Data Type:", type(c))
print("Variable: boolean_var =", d, "Data Type:", type(d))
print("Variable: list_var =", e, "Data Type:", type(e))
print("Variable: tuple_var =", f, "Data Type:", type(f))
print("Variable: dict_var =", g, "Data Type:", type(g))
