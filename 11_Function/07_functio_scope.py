def sum(a, b):
    c = a + b
    global z#Please modify global z
    z=0 #This will reffer to global variable z and not create a local variable z
    return c
z=3   
print(sum(2, 3))    
print(z)

