import random

myguess_number= random.randint(1,12)
guess_input= int(input("please enter a number to guess"))
if myguess_number== guess_input:
    print("you guessed right")
elif guess_input < myguess_number:
    print("you guessed low the guess number was", myguess_number)
elif guess_input > myguess_number:
    print("your guess high the guess number was ", myguess_number)
else:
    print("you guessed wrong the guess number was", myguess_number)
