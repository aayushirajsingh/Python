# Get the key of a minimum value from the following dictionary

marks_dict = {'Physics': 82, 'Math': 65, 'history': 65}
dict1 = {}
minvalue = min(marks_dict.values())
for k,v in marks_dict.items():
    if v == minvalue:
        dict1.update({k:v})
print(dict1)