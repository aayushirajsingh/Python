# Find all occurrences of a substring in a given string by ignoring the case
#Write a program to find all occurrences of “India” in a given string ignoring the case.
#Given:

str1 = "Welcome to INDIA. india awesome, isn't it?".lower()
find = "india"
count = str1.count(find)
print(f"Occurrences of India = {count}")
print(str1)