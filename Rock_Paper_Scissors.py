import random

# Variables, do not touch...

P1_WINS = "\nPlayer 1 wins!"
P2_WINS = "\nPlayer 2 wins!"
C_WINS = "\nThe Computer wins!"
Player_1_wins = 0
Player_2_wins = 0
Computer_wins = 0
TIE = "\nIt's a tie!"
P1_FAILED = "\nPlayer 1 failed to give proper input."
P2_FAILED = "\nPlayer 2 failed to give proper input."
C_FAILED = "\nThe Computer failed to give proper input."

# Code, you can touch this.

print()
choice = input("Human Opponent or Computer Opponent?: ").lower()

while choice not in ("human", "computer", "neither"):
    choice = input("\nUnknown input, please try again: ").lower()

if choice == "human":
    while Player_1_wins < 2 and Player_2_wins < 2:
        print("-----------------")
        print(f"Player 1 Wins: {Player_1_wins}")
        print(f"Player 2 Wins: {Player_2_wins}")

        print("\nRock...")
        print("Paper...")
        print("Scissors...")

        player_one = input("\nReady Player One!: ").lower()
        if player_one in ("i forfeit", "you win", "quit", "q", "exit"):
            print()
            break
        player_two = input("\nReady Player Two!: ").lower()
        if player_two in ("quit", "q"):
            print()
            break

        if player_one == player_two:
            print(TIE)
        elif player_one == "rock":
            if player_two == "scissors":
                print(P1_WINS)
                Player_1_wins += 1
            elif player_two == "paper":
                print(P2_WINS)
                Player_2_wins += 1
            else:
                print(P2_FAILED) 
        elif player_one == "paper":
            if player_two == "rock":
                print(P1_WINS)
                Player_1_wins += 1
            elif player_one == "scissors":
                print(P2_WINS)
                Player_2_wins += 1
            else:
                print(P2_FAILED) 
        elif player_one == "scissors":
            if player_two == "paper":
                print(P1_WINS)
                Player_1_wins += 1
            elif player_two == "rock":
                print(P2_WINS)
                Player_2_wins += 1
            else:
                print(P2_FAILED)
        else:
            print(P1_FAILED)
        print()

        if Player_1_wins == 2 or Player_2_wins == 2:
            if Player_1_wins > Player_2_wins:
                print(f"Player 1 wins with {Player_1_wins} points to Player 2's {Player_2_wins} points!")
            else:
                print(f"Player 2 wins with {Player_2_wins} points to Player 1's {Player_1_wins} points!")

            play_again = input("\nWould you like to play again? (y/n) ")

            while play_again != "y" and play_again != "n":
                play_again = input("\nI beg your pardon? (y/n) ")
                        
            if play_again == "y":
                Player_1_wins = 0
                Player_2_wins = 0
            else:
                print("\nThank you for playing! Please come again!\n")
                break

elif choice == "computer":
    while Player_1_wins < 2 and Computer_wins < 2:
        computer = random.choice(['rock', 'paper', 'scissors'])
        print("-----------------")
        print(f"Player 1 Wins: {Player_1_wins}")
        print(f"Computer Wins: {Computer_wins}")

        print("\nRock...")
        print("Paper...")
        print("Scissors...")

        player_one = input("\nReady Player One!: ").lower()
        if player_one in ("i forfeit", "you win", "quit", "q", "exit"):
            print()
            break
        print(f"The computer chose: {computer}!")

        if player_one == computer:
            print(TIE)
        elif player_one == "rock":
            if computer == "scissors":
                print(P1_WINS)
                Player_1_wins += 1
            elif computer == "paper":
                print(C_WINS)
                Computer_wins += 1
        elif player_one == "paper":
            if computer == "rock":
                print(P1_WINS)
                Player_1_wins += 1
            elif player_one == "scissors":
                print(C_WINS)
                Computer_wins += 1
        elif player_one == "scissors":
            if computer == "paper":
                print(P1_WINS)
                Player_1_wins += 1
            elif computer == "rock":
                print(C_WINS)
                Computer_wins += 1
        else:
            print(P1_FAILED)
        print()

        if Player_1_wins == 2 or Computer_wins == 2:
            if Player_1_wins > Player_2_wins:
                print(f"Player 1 wins with {Player_1_wins} points to the Computer's {Computer_wins} points!")
            else:
                print(f"The Computer wins with {Computer_wins} points to Player 1's {Player_1_wins} points!")

            play_again = input("\nWould you like to play again? (y/n) ")

            while play_again != "y" and play_again != "n":
                play_again = input("\nI beg your pardon? (y/n) ")
                        
            if play_again == "y":
                Player_1_wins = 0
                Computer_wins = 0
            else:
                print("\nThank you for playing! Please come again!\n")
                break

elif choice == "neither":
    break
