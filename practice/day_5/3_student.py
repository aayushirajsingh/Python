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
test_1 = dict1.get("class").get("student1").get("maths").sem[0].get("test1")

# ["class"]["student1"]["marks"]["maths"]["sem2"][0]["test1"][0]
print("Values of test1 key: ", test_1) # get and index
# print("Values of test2 key: ", dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test2"])


# v = dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test1"] = tuple(22,)
# print(type(v))
# print(dict1)
# print("After removing 12 from test1: ", dict1["class"]["student1"]["marks"]["maths"]["sem2"][0]["test1"])
# yikes = dict1.get("class").get("student1").get("marks").get("maths")
# yikes.clear()
# print(dict1.get("class").get("student1").get("marks").get("maths"))
# print(dict1)