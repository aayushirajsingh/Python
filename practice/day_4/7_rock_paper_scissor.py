import random

choice = input("Choose rock, paper, or scissor: ").lower()
print("Your choice: ",choice)
game = ('rock','paper','scissor')
computer =  random.choice(game)
print("Computer's choice: ",computer)

if choice == computer:
    print("It's a tie!")
elif choice == 'rock' and computer == 'paper':
    print("Computer wins")
elif choice == 'rock' and computer == 'scissor':
    print("You win")
elif choice == 'paper' and computer == 'rock':
    print("You win")
elif choice == 'paper' and computer == 'scissor':
    print("Computer wins")
elif choice == 'scissor' and computer == 'rock':
    print("Computer wins")
elif choice == 'scissor' and computer == 'paper':
    print("You win")