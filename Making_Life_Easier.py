# This was just pure gold, it's not an infinity loop;
# it's funnier, don't believe me? Run it.
# So I kept it.
""" num = 1
string = ""

while num < 100:
    string += str(num) + ', '
    num += 1
    print(string)"""

# Was an indentation error. Fuck.
# Finally fixed the string variable. Probably could've done it better.
# I'm an idiot noob. :P
"""num = 1
string = ""

while num < 100:
    string += "'" + str(num) + "'" + ', '
    num += 1
print(string)"""

# According to Volcacy (A mod on PyDiscord), 
# it could be accomplished like this too.

nums = [str(n) for n in range(1, 101)]
print(nums) # What the Fucking shit? Valkyr and I wasted a fucking hour
# on this shitty fucking program and we could've just done it like this!?
# FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK