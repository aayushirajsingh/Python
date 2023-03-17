# Create two dict. below dict key name given
#    1) name, designation, is_staff, is_active
#    2) student_profile
# User enter your name
# Check the user enter name  and is staff than user student_profile can be create profile.student profile crate using practice program 9 using.
# Check the user enter name  and is active than user can not crate profile.

# dict1 = {'name': 'jay', 'designation': 'web', 'is_staff': True, 'is_active': False}
# dict2 = {'student_profile': {}}

dict1 = {'teacher1': {'name': 'seema', 'designation': 'teacher', 'is_staff': True, 'is_active': False}}
dict2 = {'student_profile': {}}

name_check = input("Enter name: ")

if dict1['teacher1']['name'] == name_check and dict1['teacher1']['is_staff'] == True :
    print("You can create student profile.")
    name = input("Enter the student name: ")
    stud_id = input("Enter the student id: ")
    dict2[name] = stud_id
    print(dict2)
else:
    print("You are not authorized to create a student profile.")