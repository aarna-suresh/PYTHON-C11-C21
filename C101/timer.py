# import the time module
import time


# define the countdown timer function while recieving given number of seconds
def countdown_timer(passedValueInSeconds):

    #
    #
    while passedValueInSeconds>0:
        #
        minutes = int(passedValueInSeconds / 60)
        #
        secs = int(passedValueInSeconds % 60)
        #
        timer = f'{minutes}:{secs}'
        #
        print(timer)
        #
        passedValueInSeconds -= 1


# input time in seconds
userInput = int(input("enter the time in seconds: "))


#call the countdown timer  function while passing given number of seconds
countdown_timer(userInput)