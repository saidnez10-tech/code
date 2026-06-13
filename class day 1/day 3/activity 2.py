# 1) Create variables to store different types of values:
#    - `name` as text (string)
n="Zain"
#    - `age` as a whole number (integer)
age=13
#    - `is_student` as True/False (boolean)
is_student=True
#    - `weight` as a decimal number (float)
weight=42.5
# 2) Print each variable’s value.
print("my name is", n )
# 3) Print the datatype of each variable using `type()`.
print("type of n", type(n))
print("my age is", age)
print("type of age", type(age))
print("am I a student?", is_student)
print("type of is student", type(is_student))
print("my weight is", weight)
print("type of weight", type(weight))
# 4) Show a message that type casting will happen next.
print("we are going to change the data type")
# 5) Convert `age` from an integer to a string and store it 
age=str(age)
print("str", age)
print("type of age", type(age))
# 6) Print `age` and print its datatype again to confirm it changed.
# 7) Convert `weight` from a float to an integer and store it 
weight=int(weight)
print("int", weight)
print("type of weight", type(weight))

# 8) Print `weight` and print its datatype again to confirm it changed.