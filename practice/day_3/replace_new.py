# Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 10]
for item in range(len(list1)):
    if list1[item] == 10:
        list1[item] = 100
print(list1)