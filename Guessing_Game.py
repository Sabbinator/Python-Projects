# Don't touch pls and thank you.
from random import randint

i = 1
random_number = randint(1, 101)
random_number_check = 0
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 
    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', 
    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', 
    '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', 
    '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', 
    '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', 
    '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', 
    '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
application = True

# Go ahead and touch this, if you want.

while application == True:
    to_play_or_not_to_play = input("\nWould you like to play: (y/n) ")
    if to_play_or_not_to_play == "y":
        while True:
            guess = input("\nGuess a number between 1 and 100: ")
            if guess not in nums:
                print("\nYou've typed an invalid input, please try again.")
            else:
                guess = int(guess)
                if guess > 100:
                    print("\nYou've typed an invalid input, please try again.")
                elif guess < random_number:
                    print("\nToo low, try again.")
                    i += 1
                elif guess > random_number:
                    print("\nToo high, try again.")
                    i += 1
                else:
                    if random_number >= 60:
                        random_number_check += 1

                    print(f"\nYou won, it took you {i} tries!")
                    play_again = input("\nWould you like to play again? (y/n) ")

                    while play_again != "y" and play_again != "n":
                        play_again = input("\nI beg your pardon? (y/n) ")
                    
                    if play_again == "y":
                        if random_number_check >= 3:
                            random_number = randint(1, 60)
                            random_number_check = 0
                        else:
                            random_number = randint(1, 101)
                            
                        guess = None
                        i = 1
                    else:
                        print("\nThank you for playing! Please come again!")
                        break
        print()
        application = False
    elif to_play_or_not_to_play == "n":
        break
