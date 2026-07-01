# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
medical_cause=input("are you sick,Y for yes and N for no")
#    (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':
if medical_cause=="Y":
    print("You're allowed to attend the exam")
#    - Print that the student is allowed to attend the exam.
# 3) Otherwise (medical_cause is 'N'):
else:
    atten=int(input("attendence percentage"))
#    a) Ask for the student’s attendance percentage and store it in `atten`.
#    b) If `atten` is 75 or more:  
    if atten >= 75:
        print("allowed")
#       - Print "Allowed"
#    c) Else:
    else:
        print("not allowed")
#       - Print "Not allowed"