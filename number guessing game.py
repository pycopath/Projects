#This is a number guessing game where the player plays against themself.
#They will choose a maximum number (basically like saying pick a nummber between 1 and 'max number')
#Then they will be able to make guesses at the random number that was chosen by the computer. 
# They will continue to be able to guess until the correct number is guessed.

#We only need this module for the randint function. It generates our secret number.
import random
#This game is played against a cpu. AKA single player.
#Taking the player's input of the highest possible nuber to be guessed in the guessing game.
#  This is so the player can choose how hard the game will be. Larger max numbers will be harder to guess.
top_of_range = input('type number: ')
#Using .isdigit is used to test if a string is a number. It will give out a true or false. remember this for all of the other "isdigit" functions.
#In this case, we check if the top of range is a number, because if there is a letter, we will get an error later on because it needs a number to compare with.
if top_of_range.isdigit():
    #If it is a number, convert the string into an integer
    top_of_range = int(top_of_range)
    #Make sure the top of range is greater than 0
    if top_of_range < 0:
        #if not, tell the player to pick a higher number then quit the game because later you will see that the number has to be at least 1
        print("use a number greater than 0")
        quit()
#If the top of range is not a number (AKA the isdigit function reads false), quit the game so we don't get an error. There are other ways to do this without quitting the game, but this is a beginner program.
else:
    print("type a number")
    quit()
#Generate a random number between 0 and the top of range. This is the secret number
#randint creates a random integer between 2 numbers. in the game it is between 1 and the top of range from line 4. 
#We do this because we want the number to be secret and generated randomly so the player actually has to guess instead of them already knowing the number they are trying to guess.
number = random.randint(1, top_of_range)
#starting number of guesses is 0 for now. This will go up as the player tries to guess the number
#We do this to keep track of how many guesses the player has taken and we can show them how many guesses they have taken.
guesses = 0
#start a while loop
#Now everything in this while loop will eventually return to the top UNLESS there is a break statement, breaking out of the loop.
#There is only one way to break out of the loop and that is by winning the game.
#Every time the player guesses, it will add a guess and either restart the loop if the guess was incorrect, or break the loop if you guessed correctly and won the game.
while True:
    #Take input of the player's guess. This will be used to compare to the secret number to see if the guess was too high, low, or perfect.
    user_guess = input("guess the number: ")
    #Check if the guess is a number using isdigit again
    if user_guess.isdigit():
        #Add to the guess count to keep track of how many guesses. Then we will read them how many guesses they have taken when they guess the number.
        guesses = guesses + 1
        #Convert the user's guess from a string to an integer because in order to compare 2 variables with "<>=" they both have to be integers
        user_guess = int(user_guess)
        #if the user's guess is less than or = to 0, tell them to try again and send them back to the top of the loop.
        if user_guess <= 0:
            print('type a number greater than 0')
    #if the user guess is not a number, tell them to choose a number and send them back to the top of the loop.
    else:
        print("type a number not letter")
# Remember the guess has already counted for this round from here on out.
    #Check if the guess is equal to the secret number. If so, they win.
    if user_guess == number:
        #if they won, tell the player that they won in however many guesses thay had
        #splitting the quotes and adding commas to add the guesses variable is onw beginner way to add a variable to a print statement
        print("you win!!! you guessed the number in", guesses, "guesses.")
        #break the loop and end the program if they won the game
        break
#If the program gets to this section, the player got the guess wrong and they will be sent back to the top of the loop regardless because their guess was either too high or short.
    #If the user guess is lower than the secret number, notify the player and return to the top of the loop.
    elif user_guess < number:
        print("Too low! Try again.")
    #If the guess is higher than the secret number, notify the player and return to the top of the loop
    elif user_guess > number:
        print("Too High! Try again.")