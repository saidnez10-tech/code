# Step 1: Define a function factorial(x) with a docstring describing what it calculates.
def factorial(x):
    """"hi"""
# Step 2: Write the base case: if x is 0 or 1, return 1 directly.
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
# Step 3: Write the recursive case: otherwise, return x multiplied by factorial(x-1).
# Step 4: Print factorial.__doc__ to display the function's docstring.
print(factorial.__doc__)
# Step 5: Call factorial() on 0, 1, 2, 5, and 10, printing each result.
print(factorial(3))
print(factorial(5))