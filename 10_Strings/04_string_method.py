chk="Hello World" #strings are immutable means new string is created when we change the value of a string
#name[0]="h" #this will give an error because we cannot change the value of a string
a=len(chk)
print (a)
#print(chk.upper()) #this will convert the string to upper case
#print(chk.lower()) #this will convert the string to lower case
#print(chk.replace("World", "Universe"))
#print(chk.split(" ")) #this will split the string into a list of words
#print(chk.find("World")) #this will return the index of the first occurrence of the substring
#print(chk.title()) #this will convert the string to title case

text=" Hello World"
print(text.strip()) #this will remove the leading and trailing whitespaces
print(text.lstrip()) #this will remove the leading whitespaces
print(text.rstrip()) #this will remove the trailing whitespaces