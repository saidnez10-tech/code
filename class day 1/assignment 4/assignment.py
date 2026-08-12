customer_items=[{"name": "Ice cream", "price": 4, "quantity": 1}, {"name": "Bread", "price": 5, "quantity": 2}, {"name": "eggs", "price": 7, "quantity": 1}] 
total_bill=0   
for item in customer_items:
      cost=item["quantity"] *item["price"]  
      total_bill=total_bill+cost
print("Total_bill",total_bill)                                    