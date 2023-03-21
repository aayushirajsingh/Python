# Create student profile. User to ask que and create profile.

student_profile = {}
name = input("Enter the student name: ")
stud_id = input("Enter the student id: ")
student_profile.update({'Name' : name, 'Student ID' : stud_id})
print(student_profile)