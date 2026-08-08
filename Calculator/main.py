try:
    a=float(input("Enter a number:  "))
    b=float(input("Enter another number:  "))
    print("What kind of operation do you want to perform?  Press + for addition, - for subtraction, * for multiplication, / for division")
    operation=input("Enter Operation:  ")
    match operation:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case _:
            print("Invalid operation")
except Exception as e:
    print("Enter a valid number of a and b")
