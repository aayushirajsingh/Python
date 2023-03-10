# Write a program to turn every item of a list into its square.

numbers = []
n = input("Enter 7 numbers: ")

square = []
for i in numbers:
    square.append(i * i)
print(square)