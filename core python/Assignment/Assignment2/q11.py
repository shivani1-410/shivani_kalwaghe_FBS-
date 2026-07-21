#11. Write a program to accept an integer amount from user and tell minimumnumber of notes needed for representing that amount.

amount=int(input("enter the number of amount:"))
note1=amount//50
amount=amount%50

note2 = amount//40
amount = amount%40

note3 = amount//30
amount= amount%30

note4 = amount//20
amount=amount%20

note5 = amount//10
amount = amount%10

print("50 notes",note1)
print("40 notes",note2)
print("30 notes",note3)
print("20 notes",note4)
print("10 notes",note5)
