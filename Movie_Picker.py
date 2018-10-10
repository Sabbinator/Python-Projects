# Original version, by myself.
"""
from random import randint

movie0 = 0
movie1 = 0
movie2 = 0
On = True
num = randint(0,3)

def random_num_gen():
    global num
    num = randint(0,3)
    roll()

def random_num():
    random_num_gen()

def movie_count_display():
    global On
    if movie0 == 3:
        print("\nWe're watching Star Wars: The Phantom Menace")
        On = False
    elif movie1 == 3:
        print("\nWe're watching Wonder Woman")
        On = False
    elif movie2 == 3:
        print("\nWe're watching Thor: Ragnarok")
        On = False
    else:
        print(f"\nCurrent Scores for Star Wars, Wonder Woman, and Thor respectively: {movie0}, {movie1}, and {movie2}.")
        random_num_gen()

def movie_count():
    global movie0
    global movie1
    global movie2

    if num == 0:
        movie0 += 1
        movie_count_display()
    elif num == 1:
        movie1 += 1
        movie_count_display()
    else:
        movie2 += 1
        movie_count_display()

def roll_again():
    global On

    user_input = input("\nWould you like to roll again? (y/n): ")
    if user_input == "y":
        movie_count()
    else:
        print()
        On = False

def roll():
    global num
    if num == 0:
        num = "Star Wars: The Phantom Menace"
        print(f"\nThe movie rolled was {num}")
        roll_again()
    elif num == 1:
        num = "Wonder Woman"
        print(f"\nThe movie rolled was {num}")
        roll_again()
    elif num == 2:
        num = "Thor: Ragnarok"
        print(f"\nThe movie rolled was {num}")
        roll_again()

while On == True:
    random_num_gen()
print()
"""
# Version 2, by the Python Discord and myself.
"""
from random import randint

movie0 = 0 # Star Wars: The Phantom Menace
movie1 = 0 # Wonder Woman
movie2 = 0 # Thor: Ragnarok
On = True

while On:
    def roll():
        global movie0
        global movie1
        global movie2

        num = randint(0, 2)
        if num == 0 and movie0 != 2:
            print("\nThe computer rolled Star Wars: The Phantom Menace.")
            movie0 += 1
        elif num == 1 and movie1 != 3:
            print("\nThe computer rolled Wonder Woman.")
            movie1 += 1
        elif num == 2 and movie2 != 3:
            print("\nThe computer rolled Thor: Ragnarok.")
            movie2 += 1
        else:
            if movie0 == 2:
                print("\nWe're watching Star Wars: The Phantom Menace.")
                print()
            elif movie1 == 3:
                print("\nWe're watching Wonder Woman.")
                print()
            elif movie2 == 3:
                print("\nWe're watching Thor: Ragnarok.")
                print()
            global On
            On = False
        input_function()

    def input_function():
        user_input = input("\nWould you like to roll again?: ")
        if user_input == "y":
            roll()
        else:
            global On
            print("\nBye!\n")
            On = False
    
    roll()
    """
# Version 3, by Syntaxaire. Comments by me with help from Poke.
"""
# Code courtesy of Syntaxaire, explanations by Poke. 
from random import randint # Imports `randint` from `Random`

movies = ["Star Wars: The Phantom Menace",
          "Wonder Woman",
          "Thor: Ragnarok"] # A list of movies.
scores = [0] * len(movies) # Makes a list equal to the amount of items in movies

while max(scores) < 3: # While the highest value of 'scores' is less than three, it'll run this code.
    num = randint(0, 2) # Chooses a number between 0 and 2, including 2. `Randint` is weird.
    scores[num] += 1 # num represents the movie that was picked as a number (Star Wars is represented 
    # by zero, for example); scores is just like that, but is a list instead; so, since all the values of 
    # 'scores' is equal to zero, it adds a point to the movie chosen, up to three; in which case, the while
    # loop ends because of its argument '< 3'
    print(f"\nThe computer rolled {movies[num]}.") # Prints "The computer..." and includes the rolled movie.
    if max(scores) == 3: # If the higest score in scores is equal to 3, run this...
        print(f"\nWe're watching {movies[scores.index(3)]}.\n") # Prints the movie to be watched. Syntax is as 
        # follows; From the scores list, it grabs the position of the value 3, and uses that position to find
        # and print the corresponding movie in "movies". E.g, Star Wars is 0 in both, movies and scores, and
        # Wonder Woman is 2. Thor is 1.
    else: # If the highest value in scores is not equal to three, run this.
        user_input = input("\nWould you like to roll again?: ") # Retrieves input from user.
        if user_input != "y": # If user input does not equal y, do this.
            exit() # Ends the program. """

# Version 3.1; based on Syntaxaire's code, modified by me so that it cheats.
"""
from random import randint

movies = ["Star Wars: The Phantom Menace",
          "Wonder Woman",
          "Thor: Ragnarok"]
scores = [0] * len(movies)

while max(scores) < 3:
    num = randint(0, 2)
    scores[num] += 1
    print(f"\nThe computer rolled {movies[num]}.")
    if scores[2] == 1:
        print(f"\nWe're watching {movies[2]}.\n")
        exit()
    elif max(scores) == 3:
        print(f"\nWe're watching {movies[scores.index(3)]}.\n")
    else:
        user_input = input("\nWould you like to roll again?: ")
        if user_input != "y":
            exit()
"""
# Version 4; based on Syntaxaire's code, modified by me to choose movies with Dad too.
from random import randint

def withDad():
    movies = ["Jurassic World: Fallen Kingdom",
            "Deadpool 2",
            "Solo: A Star Wars Story"]
    scores = [0] * len(movies)

    while max(scores) < 3:
        num = randint(0, 2)
        scores[num] += 1
        print(f"\nThe computer rolled {movies[num]}.")
        if scores[2] == 1:
            print(f"\nWe're watching {movies[2]}.\n")
            exit()
        elif max(scores) == 3:
            print(f"\nWe're watching {movies[scores.index(3)]}.\n")
        else:
            user_input = input("\nWould you like to roll again?: ")
            if user_input != "y":
                exit()

def withJill():
    movies = ["Star Wars: The Force Awakens",
            "Wonder Woman",
            "Thor: Ragnarok"]
    scores = [0] * len(movies)

    while max(scores) < 3:
        num = randint(0, 2)
        scores[num] += 1
        print(f"\nThe computer rolled {movies[num]}.")
        if scores[0] == 1:
            print(f"\nWe're watching {movies[0]}.\n")
            exit()
        elif max(scores) == 3:
            print(f"\nWe're watching {movies[scores.index(3)]}.\n")
        else:
            user_input = input("\nWould you like to roll again?: ")
            if user_input != "y":
                exit()

print()
withWhom = input("Who are you watching the movie with?: ")

if withWhom == "Dad":
    withDad()
elif withWhom == "Jill":
    withJill()