# Create two dict. below dict key name given
#    1) name, designation, is_staff, is_active
#    2) student_profile
# User enter your name
# Check the user enter name  and is staff than user student_profile can be create profile.student profile crate using practice program 9 using.
#  Check the user enter name  and is active than user can not crate profile.

# dict1 = {'name': 'jay', 'designation': 'web', 'is_staff': True, 'is_active': False}
# dict2 = {'student_profile': {}}

# designation = input("Enter designation: ")
is_staff = 'no'
is_active = 'yes'

student_profile = {}
staff = {'teacher1': {'name': 'seema', 'designation': '', 'is_staff': '', 'is_active': ''}}

staff = {'seema':['HOD','yes','yes'],
         'kiran':['Teacher','yes','no'],
         'harsh':['accountant','no','yes'],
         'fizul':['accountant','no','no']}
name = input("Enter name: ").islower()
for item in staff:
    if item == name and is_staff == 'yes' :
        print("You can create student profile.")
# for item in range(2):
#     name = input("Enter the student name: ")
#     stud_id = input("Enter the student id: ")

#     student_profile[name] = stud_id
# print(student_profile)