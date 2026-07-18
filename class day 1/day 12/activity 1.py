# 1) Add the activity details.

# a) Mention the activity name as "ATM Cash Dispenser".
print("ATM Cash dispenser")
# b) Introduce the program as a cash withdrawal and denomination tracker.
print("Cash withdrawal")
# 2) Display the welcome message.

# a) Print the ATM title.

# b) Explain that customers will be served one at a time.

# 3) Create starting variables.

# a) Store available note values in the `notes` list.
notes=[100,50,20,10,5,1]
# b) Create `customers_served` to count total customers.
customers_served=0
# c) Create `total_dispensed` to track total cash withdrawn.
total_dispensed=0
# d) Create `log` to store each customer's note breakdown.
log=[]
serving=True
# 4) Use the outer while loop.
while serving:
    name=input("enter your name")
    amount=int(input("enter a number"))
    if amount < 0:
        print("invalid amount")
        continue
    remaining=amount
# a) Use `serving = True` to keep the ATM session running.

# b) Ask for the customer name and withdrawal amount.

# c) Use `continue` if the amount is invalid.

# 5) Break the amount into notes.

# a) Store the withdrawal amount in `remaining`.

# b) Use an inner while loop to check each note value.
    used={}
    i=0
    while i < len(notes):
        count=remaining//notes[i]
        if count > 0:
            used[notes[i]]=count
            print(notes[i],"are",count)
            remaining%=notes[i]
        i=i+1
    customers_served=customers_served+1
    total_dispensed+=amount
    log.append({"name":name,"used":used})
    print("transaction completed")
    a=input("need a new customer")
    if a != "YES":
        serving=False
print(customers_served)
print(total_dispensed)
for i in notes:
    total_notes=0
    for customer in log:
        total_notes+=customer["used"].get(i,0)
        print("total_notes",total_notes)
# c) Use floor division `//` to calculate note count.

# d) Use subtraction to reduce the remaining amount.

# e) Store used notes in the `used` dictionary.

# 6) Update transaction records.

# a) Increase the number of customers served.

# b) Add the withdrawal amount to the total dispensed cash.

# c) Save the customer's note breakdown in `log`.

# d) Print a transaction complete message.

# 7) Ask for the next customer.

# a) Ask whether another customer should be served.

# b) Stop the outer loop if the answer is not "yes".

# 8) Create the daily denomination report.

# a) Use an outer for loop to go through each note value.

# b) Use an inner for loop to check every customer's note usage.

# c) Use `.get()` to safely read note counts from each record.

# d) Print only the notes that were dispensed.

# 9) Display the final summary.

# a) Print the total number of customers served.

# b) Print the total cash dispensed.

# c) Print the ATM session closing message.