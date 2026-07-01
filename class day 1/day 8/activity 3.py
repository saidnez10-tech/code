# 1) Store the given values:
#    `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.
mean1=4
wrong_number=5
correct_number=8
total_number=7
# 2) Calculate the total sum using the wrong mean:
#    - Multiply `mean1` by `total_number`
sum=mean1*total_number
#    - Store it in `sum`
#    - Print the sum.
print("sum",sum)
# 3) Fix the sum to get the correct total:
#    - Remove the wrong number (subtract `wrong_number`)
#    - Add the correct number (add `correct_number`)
#    - Store the corrected total in `num2`
num2=sum-((wrong_number)-(correct_number))
#    - Print the corrected sum.
print("sum-wrong_number+corrent_number",num2)
# 4) Find the correct mean:
#    - Divide `num2` by `total_number`
#    - Store it in `mean2`
mean2=(num2/total_number)
#    - Print `mean2`.
print(mean2)