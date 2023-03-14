# User enter n number of the file path when say "NO" thane check all path file exist or not. print the exist file and non existing file.Using list.

import os

file_path = []
file_exist = []
file_not_exist = []

while True:
    path = input("Enter a file path, type 'NO' to stop: ")
    if path == "NO":
        break
    file_path.append(path)

for path in file_path:
    if os.path.exists(path):
        file_exist.append(path)
    else:
        file_not_exist.append(path)

print("Existing files:")
print(file_exist)

print("Non-existing files:")
print(file_not_exist)