import random

timesPlayed = 0
timesWon = 0
playAgain = 'y'
playGuess = 0
lowNum = 1
highNum = 100
numGuess = 5
count = 1

while playAgain == 'y':
    randNum = random.randint(lowNum, highNum)
    print "\n"
    print randNum
    if timesPlayed == 0:
        print ("\nLet\'s play a guessing game.")
    print ("\nYou get %i guesses." % numGuess)
    playGuess = input("\nI\'m thinking of a number between %i and %i,\n\ncan you guess what it is: " % (lowNum, highNum))
    if (lowNum > playGuess) or (playGuess > highNum):
        print ("\nWhoops, that\'s an invalid guess.")
        playGuess = input("\nI\'m thinking of a number between %i and %i,\n\ncan you guess what it is: " % (lowNum, highNum))
    while (lowNum <= playGuess) and (playGuess <= highNum):
        if playGuess > randNum:
            print ("\nSorry, that\'s too high.")
            count += 1
            playGuess = input("\nWhat\'s your next guess: ")
        elif playGuess < randNum:
            print ("\nNope, that\'s much too low.")
            count += 1
            playGuess = input("\nWhat\'s your next guess: ")
        if (count == 1) and (playGuess == randNum):
            timesWon += 1
            print ("\nAre you psychic or something?")
        if (count == numGuess) and (playGuess != randNum):
            print ("\nI\'m sorry, you ran out of guesses. The number I was thinking of was %i." % randNum)
        if (count != 1) and (playGuess == randNum):
            timesWon += 1
            print ("\nCool, you guessed it before your guesses ran out!")
        if (count == numGuess) or (randNum == playGuess):
            count = 1
            playGuess = 0
            timesPlayed += 1
            playAgain = raw_input("\nWould you like to play again?\n\n            \'y\' or \'n\': ")
            if playAgain == 'y':
                lowNum = input("\nWhat would you like the lowest number to be: ")
                highNum = input("\nWhat would you like the highest number to be: ")
                numGuess = input("\nHow many guesses do you want to be allowed: ")     
            else:
                print ("\nThanks for playing, you played won %i out of %i games!" % (timesWon, timesPlayed)) 
            



