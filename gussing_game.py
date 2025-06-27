import random
# This program generates a random number between 1 and 10 and allows the user to guess it.
number = random.randint(1, 10)
guess = 0
attempt = 3 
while attempt > 0:

    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:  
        attempt -= 1  # har wrong guess ke baad ye hona chahiye

        print("You guessed it right!")
    elif guess < number:
        attempt -= 1  # har wrong guess ke baad ye hona chahiye

        print("Too low! Try again. have {} attempts left.".format(attempt))
    else:
        attempt -= 1  # har wrong guess ke baad ye hona chahiye

        print("Too high! Try again.") 
        if attempt == 0:
            print("Game over!")