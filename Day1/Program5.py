p1=int(input("Enter runs scored by Player1 in 60 balls:"))
p2=int(input("\nEnter runs scored by Player2 in 60 balls:"))
p3=int(input("\nEnter runs scored by Player3 in 60 balls:"))
sr1=p1*100/60
sr2=p2*100/60
sr3=p3*100/60
print("\nStrike rate of Player1 is",sr1)
print("Strike rate of Player2 is",sr2)
print("Strike rate of Player3 is",sr3)
print("Strike rate of Player1 if he played 60 more balls is",sr1*2)
print("Strike rate of Player2 if he played 60 more balls is",sr2*2)
print("Strike rate of Player3 if he played 60 more balls is",sr3*2)
print("Max. sixes Player1 could hit is",p1//6)
print("Max. sixes Player2 could hit is",p2//6)
print("Max. sixes Player3 could hit is",p3//6)
