# find greatest of 4 num entered by the user
# if all numbers are same should not go into other 

print("Find out which number is greater")
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")
num4 = input("Enter number 4: ")

if num1 >= num2 and num1 >= num3 and num1 > num4:
    print(f"{num1} is greatest")
elif num2 > num3 and num2 > num4:
    print(f"{num2} is greatest")
elif num3 > num4:
    print(f"{num3} is greatest")
else:
    print(f"{num4} is greatest")