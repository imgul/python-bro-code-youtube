import random

options = ('rock', 'paper', 'scissors')
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("Tie!!!")
        elif player == 'rock' and computer == 'scissors':
            print('You Won!')
        elif player == 'paper' and computer == 'rock':
            print('You Won!')
        elif player == 'scissors' and computer == 'paper':
            print('You Won!')
        else:
            print('You Loose!')

    if input("Play Again? (y/n): ").lower() != 'y':
        playing = False

print("Good Bye ;)")
