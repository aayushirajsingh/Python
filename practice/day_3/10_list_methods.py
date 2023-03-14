# All list Methods using writ one program.

list1 = [3, 7, 9, 1, 5, 2, 8, 4, 6]

print("Original list:", list1)

list1.append(10)
print("Appending:", list1)

list1.sort()
print("Sorting:", list1)

list1.reverse()
print("Reversing:", list1)

list1.insert(3, 11)
print("Inserting:", list1)

list1.remove(5)
print("Removing:", list1)

popped_item = list1.pop(2)
print("Popping:", list1)
print("Popped item:", popped_item)

count = list1.count(7)
print("Count of 7:", count)

index = list1.index(2)
print("Index of 8:", index)

list1.clear()
print("Clearing the list:", list1)