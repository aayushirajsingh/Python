# Remove all occurrences of a specific item from a list.

list1 = [5, 10, 16, 201, 25, 54, 22]
list2 = []
# list1 = [item for item in list1 if item % 5 != 0]
for item in list1:
    if item % 5 != 0:
        list2.append(item)
print(list2)