name = input("Enter the name: ")
date = input("Enter the date: ")
occasion = input("Enter the occasion: ")
company = input("Enter the company's name: ")

# Way 1 using comma
print("Hello",name,"good to see you,")

# Way 2 using f-string
print(f"on {date}, on the occasion of {occasion}, there is a holiday!")

# Way 3 using .format
print("We the Employees of {}, wish you a very Happy Holi!".format(name))