# list in name present or not

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
to_find = input("Write the name of the language you want to find: ")
print(to_find)
if to_find in languages:
    print("Name Present")
else:
    print("Name not found")