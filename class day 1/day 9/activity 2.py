# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.
units=int(input("enter number of electricity units"))
# 2) Use if–elif–else to decide the cost based on `units`:
#    - If `units` is less than 50:
if units < 50:
    
#      Set `amount` as units × 2.60 and set `surcharge` as 25.
    amount=units * 2.60
    surcharge=25
#    - Else if `units` is 100 or less:
elif units <= 100:
#      Set `amount` as (cost for first 50 units) + (remaining units × 3.25)
    amount=130+((units-50)*3.25)
#      Set `surcharge` as 35.
    surcharge=35
#    - Else if `units` is 200 or less:
elif units <=200:
#      Set `amount` as (cost for first 50 units) + (cost for next 50 units) + (remaining units × 5.26)
    amount=130+162.5+((units-100)*5.26)
#      Set `surcharge` as 45.
    surcharge=45
#    - Else (units more than 200):
else:
    if units > 200:
#      Set `amount` as (cost for first 50) + (next 50) + (next 100) + (remaining units × 8.45)
        amount=130+162.5+526+((units-200)*8.45)
#      Set `surcharge` as 75.
        surcharge=75
# 3) Calculate the final bill:
#    total = amount + surcharge.
total=amount+surcharge
# 4) Print the electricity bill (`total`) in 2 decimal places.
print("total",total)