# Merge two Python dictionaries into one

dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}

# Way 1
print(dict1|dict2)

# Way 2
print({**dict1, **dict2})

# Way 3
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)