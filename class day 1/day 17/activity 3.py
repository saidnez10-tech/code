# Step 1: Set a flag variable valid to False, and start a while not valid loop.
valid=False
while not valid:
# Step 2: Inside the loop, start a try block and read a number using int(input(...)).
    try:
        number=int(input("enter a number"))
# Step 3: Start an inner while loop that keeps running as long as the number is even (n % 2 == 0).
        while number % 2 ==0:
# Step 4: Inside that inner loop, print "bye", then ask for a new number.
            print("bye")
# Step 5: Once an odd number is entered, the inner loop ends and valid is set to True, stopping the outer loop.
        valid=True
# Step 6: Add an except ValueError block that prints "Invalid" if the entered text isn't a number, letting the outer loop ask again.
    except ValueError:
        print("Invalid")