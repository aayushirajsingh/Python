# User enter any word, check in tuple word is there or not.

tuple1 = ("a","b","c","d","A")
word = input("Enter a word: ")
yes = False
for item in word:
    if item in tuple1:
        yes = True
        break
print(yes)
# if yes == True:
#     print(True)
# else:
#     print(False)