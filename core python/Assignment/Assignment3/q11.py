''''Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

age1=int(input("enter the age of the first person: "))
tkprice1=float(input("enter the Ticket price of first person: "))
totalprice=0
if age1<12:
    totalprice=totalprice+(tkprice1*0.07)
elif age1>59:
    totalprice=totalprice+(tkprice1+0.50)
else:
    totalprice=totalprice+tkprice1
print("Total Ticket Amount =", totalprice)
    
age2 =int(input("enter the age of second person:"))
tkprice2 = float(input("enter the Ticket of second person: "))
if age2<12:
    totalprice=totalprice+(tkprice2*0.07)
elif age2>59:
    totalprice=totalprice+(tkprice2+0.50)
else:
    totalprice=totalprice+tkprice2
print("Total Ticket Amount =", totalprice)
    
age3=int(input("enter the age of third person:"))
tkprice3= float(input("enter the Ticket of third person: "))
if age3<12:
    totalprice=totalprice+(tkprice3*0.07)
elif age3>59:
    totalprice=totalprice+(tkprice3+0.50)
else:
    totalprice=totalprice+tkprice3
print("Total Ticket Amount =", totalprice)

age4=int(input("enter the age of four person:"))
tkprice4= float(input("enter the Ticket of third person: "))
if age4<12:
    totalprice=totalprice+(tkprice4*0.07)
elif age4>59:
    totalprice=totalprice+(tkprice4+0.50)
else:
    totalprice=totalprice+tkprice4
print("Total Ticket Amount =", totalprice)

age5=int(input("enter the age of five person:"))
tkprice5= float(input("enter the Ticket of third person: "))
if age5<12:
    totalprice=totalprice+(tkprice5*0.07)
elif age5>59:
    totalprice=totalprice+(tkprice5+0.50)
else:
    totalprice=totalprice+tkprice5
print("Total Ticket Amount =", totalprice)

