"""Calculate the sum and average of the digits present in a string

Given a string s1, write a program to return the sum and average of 
the digits that appear in the string, ignoring all other characters.

Given: """

str1 = "Eightech29@#8496"
sum = (int(str1[-1])+int(str1[-2])+int(str1[-3])+int(str1[-4])+int(str1[-7])+int(str1[-8]))
avg = sum//6
print("Sum = ",sum)
print("Avg = ",avg)