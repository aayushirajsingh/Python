# student pass or fail

print("Enter marks obtained in 5 subjects")
english = float(input("Enter English Marks: "))
math = float(input("Enter Math score: "))
hindi = float(input("Enter Hindi Marks: "))
sst = float(input("Enter SST Marks: "))
science = float(input("Enter Science Marks: "))

total = english + math + hindi + sst + science
percentage = (total / 500) * 100
print("Your Percentage = ",percentage)
if percentage >= 33:
    print("You Passed!!")
else:
    print("You Failed.")