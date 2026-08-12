# Step 1: Define a function calculate_change(paid, price) that subtracts price from paid and returns the result.
def calculate_change(paid,price):
# Step 2: Set the snack price and print a greeting showing the price and the accepted coin values.
    change=paid-price
    return change
snack_price=5
print("Welcome to  SNACK")
print("Each snack costs 5")
print("Dont think just buy")
# Step 3: Start a while True loop that keeps asking for coins, using continue to reject any coin that isn't 1, 5, 10, or 20.
total_inserted=0
while True:
    coin=int(input("enter the coin"))
    if coin != 1 and coin != 5:
        print("Invalid coin")
        continue
    total_inserted=coin+total_inserted
# Step 4: Add every valid coin to a running total and print how much has been inserted so far.
    print("Total_inserted",total_inserted)
# Step 5: Use break to stop the loop the moment the total reaches or passes the snack price.
    if total_inserted >= snack_price:
        print("Enough money inserted")
        break
# Step 6: Call calculate_change() with the total inserted and the snack price to work out the change.
change=calculate_change(total_inserted, snack_price)
print("Here is your snack")
if change==0:
    pass
else:
    print("Here is your change", change)
# Step 7: Use pass when the change is exactly zero, or print the change amount otherwise, then print a purchase summary.
print("======SNACK=======")
print("Snack price:", snack_price)
print("Total inserted:", total_inserted)
print("Total_change:", change)
print("====================")
print("Thank you for your purchase")