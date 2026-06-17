# 1) Store values in `a`, `b`, and `c`.
a=8
b=3
c=4
# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).
print(not(a==b))
# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).
print(not(b==c))
# 4) Store two strings in `a` and `b`.
a1="zain"
b2="malik"
# 5) If `a` is not equal to `b`, print a message saying they are different.
if not(a==b):
    print("a is not equal to b")
# 6) Store new numeric values in `a` and `b`.
a=6
b=2
# 7) Check this condition: (a equals 1) is not the same as (b equals 5).
#    - If exactly one of these comparisons is True, the condition becomes True.
if not((a==1)==(b==5)):
#    - If the condition is True, print "Hello".
    print("Hello")
# 8) Take an integer input from the user and store it in `a`.
a=input("enter a number")
# 9) Check if `a` is not divisible by 2 (remainder is not 0).
a=int(a)
#    - If true, print that `a` is not an even number (it is odd).
if not(a%2==0):
    print("it is an odd number")