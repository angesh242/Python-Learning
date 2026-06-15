a=int(input("Enter a number between 1 to 100: "))
match (a):
    case 15:
        print("You won a free ticket to the concert!")
    case 25:
        print("You won a free movie ticket!")
    case 50:
        print("You won a free dinner voucher!")
    case _:
        print("Sorry, you didn't win anything this time. Better luck next time!")   
