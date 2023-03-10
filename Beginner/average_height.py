# You are going to write a program that calculates the average student height from a list of heights.

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # total_height += student_heights[n]
    # number_of_student += 1

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_student = 0
for student in student_heights:
    number_of_student += 1
print(number_of_student)

avg_height = round(total_height/number_of_student)
print ("The average height is",avg_height)