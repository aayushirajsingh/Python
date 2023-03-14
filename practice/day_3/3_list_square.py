# Write a program to turn every item of a list into its square.

numbers = []
numb = input("Enter 7 numbers: ")
for item in numb.split():
    n = int(item)
    numbers.append(n)
print(numbers)
square = []
for i in numbers:
    square.append(i * i)
print(square)