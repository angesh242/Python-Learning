# Write a program that asks the user for a number  and prints whether the number is positive, negative or zero.
number=float(input("Enter the number: "))
if number>0:
    print("The number is positive")
elif(number<0):
    print("The number is negative")
else:
    print("The number is zero")