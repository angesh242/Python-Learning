# Write the program that keeps asking to user to enter a password until the correct password is entered. 
# The correct password is "python123". 
# Once the correct password is entered, the program should print "Access granted".
cpswd="python123"
pswd=""
while pswd!=cpswd:
    pswd=input("Enter the password: ")
print("Access granted")