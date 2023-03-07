# Write a program that adds the digits in a 2 digit number. e.g. if input = 35, output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
#print(type(two_digit_number))
add = int(two_digit_number[0]) + int(two_digit_number[1])
print(add)