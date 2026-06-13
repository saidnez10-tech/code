# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.
math=int(input("enter math mark"))
english=int(input("enter english mark"))
science=int(input("enter science mark"))
arabic=int(input("enter arabic mark"))
# 2) Add all 4 subject marks and store the total in `sum`.
sum=math+science+english+arabic
# 3) Print the total marks stored in `sum`.
print("sum of all subjects", sum)
# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.
percentage=(sum/400)*100
# 5) Print the percentage stored in `perc`.
print("percentage of all numbers", percentage)