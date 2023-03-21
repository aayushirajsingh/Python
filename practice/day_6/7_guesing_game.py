# Create a simple guessing game using Python and sets.
# The game will work as follows:
# 1) The computer will generate a random number between 1 and 50.
# 2) The player will have to guess the number.
# 3) If the player's guess is too high, the computer will let the player know and ask for another guess.
# 4) If the player's guess is too low, the computer will let the player know and ask for another guess.
# 5) If the player guesses the correct number, the game will end and the player will be congratulated and total number of guess show.

import random
number = random.randint(1,50)
guess = int(input("Enter any number between 1 to 50: "))
guesses = set()
count = 1
while number != guess:
    if guess <= number:
        count += 1
        print("Too low")
        guess = int(input("Enter number again: "))
        guesses.add(guess)
    elif guess >= number:
        count += 1
        print("Too high!")  
        guess = int(input("Enter number again: "))
        guesses.add(guess)
    else:
        # count += 1
        # guesses.add(guess)
        break
print("You Guessed It Right!!")
print(f"Number of Guesses: {count} \n {guesses}")