# Write a Python program to convert a tuple to a string

tuple1 = (1, 2, 3, "abc")
str1 = ''
for item in tuple1:
    str1 = str1 + str(item,)
print(str1)

#can use slicing