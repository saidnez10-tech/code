# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount=int(input("enter amount you want to withdraw"))
# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.
note1=amount//100

# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.
note2=amount%100
# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.
note2=note2//50
# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.
note3=amount%100
note3=((amount%100)%50)//10
# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print("100 dirham note",note1)
print("50 dirham note", note2)
print("10 dirham note", note3)