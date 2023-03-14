# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# You are not allowed to use the choice() function

import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
#person_who_will_pay = random.choice(names)
print(person_who_will_pay+" is going to buy the meal today")