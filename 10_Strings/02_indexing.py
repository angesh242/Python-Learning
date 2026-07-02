name="Harry" 
#-1 type of thing means negative indexing, which means counting from the end of the string. 
print(name[0])  # Output: H -> -5
print(name[1])  # Output: a ->-4
print(name[2])  # Output: r -> -3
print(name[3])  # Output: r -> -2
print(name[4])  # Output: y -> -1
#print(name[5]) # Output: error (IndexError)
print(name[-1])  # Output: y