
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b
try:
    a=float(input("enter a number"))
    b=float(input("enter a number"))
    print(add(a,b))
    print(subtract(a,b))
    print(divide(a,b))
    print(multiply(a,b))
except ZeroDivisionError:
    print("You cant enter zero!")
except ValueError:
    print("You enter anything except numbers")