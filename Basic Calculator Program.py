def sub():
    print("Would you like to calculate another number?")
    positive_answers = ["duh," "of course", "sure", "yeah", "yes"]

    while True:
        _answer=input("> ").lower()
        if _answer in positive_answers:
            return True
        elif _answer == "help" or _answer == "halp":
            print("Type duh, of course, sure, yeah, yes, nah, or no.")
            sub()
            return True
        elif _answer == "no" or _answer == "nah":
            print("Thank you for using Sabbinator's 'Basic Calculator' Program. Have a nice day!")
            return False

def main():

    running = True
    
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'exponentiation' to multiply by exponents")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
        
    while running:
        user_input=input("> ").lower()
        if user_input=="add":
            num1=float(input("Enter a number: "))
            num2=float(input("Enter another number: "))
            result=str(num1 + num2)
            print("The answer is " + result)
            running = sub()
        elif user_input=="subtract":
            num1=float(input("Enter a number: "))
            num2=float(input("Enter another number: "))
            result=str(num1 - num2)
            print("The answer is " + result)
            running = sub()
        elif user_input=="multiply":
            num1=float(input("Enter a number: "))
            num2=float(input("Enter another number: "))
            result=str(num1 * num2)
            print("The answer is " + result)
            running = sub()
        elif user_input=="exponentiation":
            num1=float(input("Enter a number: "))
            num2=int(input("Enter a number: "))
            result=str(num1**num2)
            print("The answer is " + result)
            running = sub()
        elif user_input=="divide":
            num1=float(input("Enter a number: "))
            num2=float(input("Enter another number: "))
            result=str(num1 / num2)
            print("The answer is " + result)
            running = sub()
        elif user_input=="quit" or user_input=="die!":
            print("Goodbye")
            running = False
        else:
            print("Unknown input")
main()

# Does this work?