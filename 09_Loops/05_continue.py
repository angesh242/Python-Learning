for i in range(1,20):
    if i==10:
        #break #break statement is used to exit the loop when a certain condition is met. In this case, when i equals 10, the loop will stop executing and will not print any numbers after 10.
        continue #continue statement is used to skip the current iteration of the loop when a certain condition is met. In this case, when i equals 10, the loop will skip the print statement and move on to the next iteration, which means it will not print 10 but will print all other numbers from 1 to 20.
    print(i)