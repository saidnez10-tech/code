#Step 1: Define a function total_calc(bill_amount, tip_perc) with two positional parameters.
def total_calc(bill_amount, tip_perc):
#Step 2: Calculate the total by adding the tip percentage onto the bill amount.
    tip=(bill_amount*tip_perc)/100
    total_amount=bill_amount+tip_perc
#Step 3: Round the total to two decimal places using round().
    round(total_amount,2)
#Step 4: Print the final total using an f-string.
    print("Please pay")
    print( round(total_amount,2))
    
#Step 5: Call total_calc(150, 20), passing the bill amount and tip percentage in that exact order.
total_calc(150, 20)