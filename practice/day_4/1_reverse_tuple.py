# Reverse the tuple

tuple1 = (1, 2, 3, 4, 5)
new_tup = ()
for item in reversed(tuple1):
    new_tup = new_tup + (item,)
print(new_tup)
# print(tuple1[::-1])