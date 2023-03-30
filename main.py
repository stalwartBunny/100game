import random

name = input('Input player name \n')
print('It is good to meet you, ' + name + '\n' + "A random number between 1 and 100 has been picked, you have six tries to guess it remaining. \n")

def restart():
    retry = input("\n Would you like to play again? Yes/No    \n")
    if retry == 'yes' or retry == 'Yes' or retry == "YES":
        game()

    if retry == "no" or retry == 'No' or retry == "NO":
        print("Another time.")

def game():
    number = random.randint(1, 100)
    attempts = 6
    selection = int(input("What number do you guess? \n"))
    while attempts > 1 and selection != number:
        if selection > number:
            attempts -= 1
            attemptStr = str(attempts)
            print("Your guess was too high, try again. You have " + attemptStr + " remaining.")

        else:
            attempts -= 1
            attemptStr = str(attempts)
            print("Your guess was too low, try again. You have " + attemptStr + " remaining.")

        selection = int(input("\n"))

    if attempts == 0 and selection != number:
        numStr = str(number)
        print("You were unsuccessful, the answer was " + numStr + ". Thank you for playing.")
        restart()

    else:
        numStr = str(number)
        print("You are correct! The number is " + numStr + ". Congratulations!")
        restart()

game()