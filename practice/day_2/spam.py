# spam message or not

enter = input("Enter spam or not spam: ")
spam = enter.find("spam")
not_spam = enter.find("not spam")
print(spam)
if spam != -1:
    print("It is a spam")
elif not_spam != -1:
    print("It is not a spam")
else:
    print("Invalid request")