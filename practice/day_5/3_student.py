# Print the value of key ‘history’ from the below dict.(student)
# Print the value of key 'test2' and 'test1' from the below dict.(student1)
# Update dict test1 value  remove '12' and add '22'.(student1)
# Delete a list of keys from a dictionary : list = ['sem1', 'sem2']

dict1 = {
    "class": {
        "student": {
            "name": "raju",
            "marks": {
                "physics": 70,
                "history": 80,
            }
        },
        "student1": {
            "name": "jay",
            "marks": {
                "physics": 70,
                "history": 80,
                "maths": {"sem1":24, "sem2":[{"test1":(12,), "test2":10}]}
            }
        }
    }
}
list1 = ['sem1', 'sem2']

# Printing the key 'history'
print("Values of history key: ", dict1.get("class").get("student").get("marks").get("history"))

# Printing the key  of test2 and test1
test_1 = dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test1"][0]
test_2 =  dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test2"]
print("Values of test1 key: ", test_1) 
print("Values of test2 key: ", test_2)

# Updating the value of test1
test_update = dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test1"] = (22,)
print("Updated value of test1: ", test_update[0])
print(type(dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test1"]))

# Deleting the list of keys
for item in list1:
    dict1['class']['student1']['marks']['maths'].pop(item)
print(dict1)