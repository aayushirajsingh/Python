# enter user name char is less and equle 10

username = input("Enter your username: ")
char = len(username)

if char <= 10:
    print("Username = ",username)
else:
    print("Username too long")