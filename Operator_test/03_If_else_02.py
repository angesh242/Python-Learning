#Create the programs that check if a person is eligible to vote or not. A person is eligible to vote if his/her age is greater than or equal to 18 years.
age=int(input("Enter the age of the person: "))
if age>18:
    print ("The person is eligible to vote")
elif age==18:
    print ("The person is eligible to vote")
else:
    print ("The person is not eligible to vote")