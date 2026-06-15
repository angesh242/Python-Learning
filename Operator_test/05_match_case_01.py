#Ask the user to enter a day number(1-7) and print the corresponding day name using match case statement.
from unittest import case


daynum=int(input("Enter the day number(1-7): "))
match daynum:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")                
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")