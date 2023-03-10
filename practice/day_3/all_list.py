# All list Methods using writ one program.

# Adds List Element as value of List.
list1 = ['Mathematics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]


list1.append(20544)
list1.insert(2,10087)	
list2.extend(list1)
print(sum(list2))
print(list1.count(1))
print(len(list2))
print(list2.index(2))
print(list1.pop(0))
del list2[0]
print(list2)
list1.remove(3)
print(list1)