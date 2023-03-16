# Initialize dictionary with default values

employees = ['Radha', 'Emma']
defaults = {"designation": 'Internship', "salary": 5000}
dict1 = dict.fromkeys(employees,defaults)
print(dict1)