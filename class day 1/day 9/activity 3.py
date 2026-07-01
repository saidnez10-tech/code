# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car

# 2) Take the user’s input and store it in `choice`.
choice=int(input("select a ride"))
# 3) If `choice` is 1 (Bike):
if choice==1:
    print("choose scooty or scooter")
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
    choice2=input("enter your choice")
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"
    if choice2=="scooty":
        print("you have chose scooty")
    else:
        print("you have chosen scooter")
# 4) Else if `choice` is 2 (Car):
elif choice==2:
    choice3=input("enter car model")
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
    if choice3=="Sedan":
        print("you have selected sedan")
#       Else, print "you have selected XUV"
    else:
        print("you have selected XUV")
# 5) Else (if `choice` is not 1 or 2):
else:
    print("wrong choice")
#    Print "Wrong choice!"