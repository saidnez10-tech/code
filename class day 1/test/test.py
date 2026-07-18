import random
number=random.randint(1,50)
for i in range(0,5):
    user_num=int(input("enter a number"))
    if number==user_num:
        print("You have won!")
    else:
        i=i+1
print(number)
