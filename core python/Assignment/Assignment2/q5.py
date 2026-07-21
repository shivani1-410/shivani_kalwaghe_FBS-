# WAP to calculate selling price of book based on cost price and discount.

cp = float(input("enter the cost of the book:"))
discount=float(input("enter the discount in percentage:"))
TA=(cp*discount)/100
Sp=cp-TA
print("selling price of book",Sp) 