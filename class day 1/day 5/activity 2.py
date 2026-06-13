byprice=float(input("enter the byprice"))
saleprice=float(input("enter sale price"))
if saleprice > byprice:
    profit=saleprice-byprice
    print("total profit made", profit)
else:
    print("no profit")