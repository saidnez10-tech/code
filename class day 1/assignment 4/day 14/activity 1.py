def greet_customer():
    print("Welcome to my shop")
    print("If you're having a bad day then just have a cup of tea")
greet_customer()
price=float(input("how much does the tea cost"))
amount=int(input("how much cups of tea you want to buy"))
def calculate_price(p,a):
    total=p*a
    return total
total_cost=calculate_price(price,amount)
print(round(total_cost,2))
change=int(input("ask the user to pay the amount"))
def calculate_change(p,a):
    change=p-a
    return change
change_due=calculate_change(change,total_cost)
def thank_customer():
    print("Thanks")
    print("")
thank_customer()
print("=============")
print("Tea")
print("price per cup",price)
print("amount of cups",amount)
print("Total cost of tea",total_cost)
print("amount paid by customer",change)
print("amount of change given to customer",change_due)
thank_customer()
print("----========")