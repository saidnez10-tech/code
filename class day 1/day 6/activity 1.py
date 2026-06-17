# 1) Store values in `a`, `b`, and `c`.
a=5
b=7
c=0
# 2) Check an AND condition using `a and b and c`:
if a and b and c:
#    - This becomes True only if all three values are treated as True.
    print("all the numbers dont have bollean values")
#    - If the condition is True, print the “all true” message.
#    - Otherwise, print the “at least one false” message.
else:
    print("any one of the numbers is not bollean")
# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a=1
b=3
c=9
# 4) Check an OR condition: `a > 0 or b > 0`
if a > 0 or b > 0 or c > 0:
    print("anyone of the numbers are greater than 0")
else:
    print("none of the numbers are greater than 0")
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.