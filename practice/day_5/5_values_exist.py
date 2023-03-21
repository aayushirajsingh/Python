# Check if a value exists in a dictionary. User enter any word check in dict word meaning exist or not. If exist print meaning.

dictionary = {'hello': 'it is a greeting', 'bye': 'it is said at departure'}
word = input("Enter word: ").lower()
for item in dictionary:
    if item == word:
        print(dictionary.get(word))
        break
else:
    print("Word not found")