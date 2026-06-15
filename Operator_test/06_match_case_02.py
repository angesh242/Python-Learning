#Write a program using maatch case that simulates a simple calculator. 
# 1. The program should take two numbers and an operator (+, -, *, /) as input from the user 
# and perform the corresponding operation using match case statement. 
# If the operator is not valid, the program should print an error message.
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
operator=input("Enter the operator (+, -, *, /): ")
match operator:
    case "+":
        print("The result is: ",a+b)
    case "-":
        print("The result is: ",a-b)
    case "*":
        print("The result is: ",a*b)
    case "/":
        if b!=0:
            print("The result is: ",a/b)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")