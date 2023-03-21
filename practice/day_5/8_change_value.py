# Change value of a key in a nested dictionary

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
people[2]['age'] = '24'
print(people)