# 1) Ask the user to enter their height in centimeters and store it in `height`.
height=float(input("enter the height"))
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
weight=float(input("enter your weight"))
# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
BMI=weight/(height/100)**2
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.

# 4) Print the BMI value.
print("your bmi is", BMI)
# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
if BMI <=18.4:
    print("you are under weight")
#    - Else if BMI is 24.9 or less → print "healthy"
elif BMI <=24.9:
    print("you are healthy")
#    - Else if BMI is 29.9 or less → print "over weight"
elif BMI <=29.9:
    print("you are overweight")
#    - Else if BMI is 34.9 or less → print "severely over weight"
elif BMI <=34.9:
    print("you are severly overweight")
#    - Else if BMI is 39.9 or less → print "obese"
elif BMI <=39.9:
    print("you are obese")
#    - Else → print "severely obese"
else:
    print("you are severly obese")