# import the time & playsound module
import time
from playsound import playsound 
  
# define the countdown timer function
def countdown_timer(passedValueInSeconds):
    
    while passedValueInSeconds > 0:       

        mins = int(passedValueInSeconds / 60)
        secs = int(passedValueInSeconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        passedValueInSeconds -= 1
      
    print('Time Up!')

    playsound('mixkit-sound.wav')
  
  
# input time in seconds
seconds = input("Enter the time in number of seconds: ")
  
# function call
countdown_timer(int(seconds))