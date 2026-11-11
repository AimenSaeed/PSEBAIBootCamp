"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""

# Warm: Even, odd and sign
number=int(input("Enter a number: "))
if number == 0:
    print("The number is zero")
elif (number>0) and (number%2==0):
    print("The number is positive and even")
elif (number>0) and (number%2!=0):
    print("The number is positive and odd")
elif (number<0) and (number%2==0):
    print("The number is negative and even")
else:
    print("The number is negative and odd")

# Build: Grade Calculator
marks=int(input("Enter your marks (out of 100): "))
if (marks>=80) and (marks<=100):
    print("Your grade is A")
elif (marks>=70) and (marks<80):
    print("Your grade is B")
elif (marks>=60) and (marks<70):
    print("Your grade is C")
elif (marks>=33) and (marks<60):
    print("Your grade is D")
elif (marks>=0) and (marks<33):
    print("Your grade is F")
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")

# Challenge: Electricity Bill Calculator
units=int(input("Enter the number of units consumed: "))
if units<=100:
    bill=(units*10)+50
elif (units>100) and (units<=200):
    bill=(100*10)+((units-100)*15)+50
else:
    bill=((100*10)+(100*15)+((units-200)*20))+50
print(f"Your electricity bill is: {bill} Rs")

