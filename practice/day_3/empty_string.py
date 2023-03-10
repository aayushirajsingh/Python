# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
length = len(list1)
for item in list1:
    if item == "":
        list1.remove("")
print(list1)