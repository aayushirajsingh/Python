# Remove all occurrences of a specific item from a list.

list1 = [5, 10, 16, 201, 25, 54, 22]
for item in list1:
    print(item)
    if item % 5 == 0:
        # print(item)
        list1.remove(item)
# print(list1[0])
# print(list1[0]%5==0)