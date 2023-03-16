# Convert two tuple into a dictionary

keys = ('a', 'b', 'c')
values = (10, 20, 30)

if len(keys) == len(values):
    dictionary = dict(zip(keys, values))
print(dictionary)