# Add a list of elements to a set

a = {1,2,3}
b = ['a','b','c']
for item in b:
    a.update(item)
print(type(a))