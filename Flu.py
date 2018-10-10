# NO TOUCHING ======================================

from random import choice, randint
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================

print()
print("Information...")
print(f"Sick: {actually_sick}")
print(f"Kinda Sick: {kinda_sick}")
print(f"Hatred for Job: {hate_your_job}")
print(f"You have {sick_days} sick days.")
print()

print("The Results...")
if actually_sick:
    if hate_your_job:
        if sick_days > 0:
            print("Taking the day off to get better and catch up on Game of Thrones.")
        else:
            print("Argh, whatever; I'll just get my co-workers sick. I'll get Meg Griffin sick, fuck Meg.")
    else:
        if sick_days > 0:
            print("Damn, guess I have to take a day off.")
        else:
            print("Welp, I hope everyone won't get sick because of me.")
else:
    if kinda_sick:
        if hate_your_job:
            if sick_days > 0:
                print("I hate work, I'm staying home and watching Game of Thrones all day.")
            else:
                print("Welp, time to go to work")
        else:
            print("Time to go to work!")
    else:
        if hate_your_job:
            print("Argh, I hate my job. Going to quit soon.")
        else:
            print("(In Spongebob Voice) It's the best day ever (best day ever)")
print()
