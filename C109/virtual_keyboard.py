
#import statements
import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
#initialize keyboard as the controller object
keyboard = Controller()
#opening the webcam and reading the frames and saving them in cap variable
cap = cv2.VideoCapture(0)
#capturing the cameras window width and height and 
#saving them in variables width and height respectivelly 
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
#loading the predefined data sets for hand gestures, landmarks, positions
#drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
#detecting how well it can identify the hand and its motion
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
#landmarks for the tips of each finger
tipIds = [4, 8, 12, 16, 20]
#creating state variable with no initial value
state = None

# Define a function to count fingers
def countFingers(image, hand_landmarks, handNo=0):
#using the state variable inside the function
# to make sure the value of the state variable is updated every time
#we open or close the fingers and thats why we are changing the scope of the variable
#state as global

    global state

    if hand_landmarks:
        # Get all Landmarks of the FIRST Hand VISIBLE
        landmarks = hand_landmarks[handNo].landmark

        # Count Fingers        
        fingers = []

        for lm_index in tipIds:
                # Get Finger Tip and Bottom y Position Value
                finger_tip_y = landmarks[lm_index].y 
                finger_bottom_y = landmarks[lm_index - 2].y

                # Check if ANY FINGER is OPEN or CLOSED
                if lm_index !=4:
                    if finger_tip_y < finger_bottom_y:
                        fingers.append(1)
                        # print("FINGER with id ",lm_index," is Open")

                    if finger_tip_y > finger_bottom_y:
                        fingers.append(0)
                        # print("FINGER with id ",lm_index," is Closed")

        
        totalFingers = fingers.count(1)
        
        # PLAY or PAUSE a Video
        if totalFingers == 4:
            state = "Play"

        if totalFingers == 0 and state == "Play":
            state = "Pause"
            keyboard.press(Key.space)

        # Move Video FORWARD & BACKWARDS    
        finger_tip_x = (landmarks[8].x)*width
 
        if totalFingers == 1:
            if  finger_tip_x < width-400:
                print("Play Backward")
                keyboard.press(Key.left)

            if finger_tip_x > width-50:
                print("Play Forward")
                keyboard.press(Key.right)
        
        
# Define a function to 
def drawHandLandmarks(image, hand_landmarks):

    # Draw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



while True:
    success, image = cap.read()

    image = cv2.flip(image, 1)
    
    # Detect the Hands Landmarks 
    results = hands.process(image)

    # Get landmark position from the processed result
    hand_landmarks = results.multi_hand_landmarks

    # Draw Landmarks
    drawHandLandmarks(image, hand_landmarks)

    # Get Hand Fingers Position        
    countFingers(image, hand_landmarks)

    cv2.imshow("Media Controller", image)

    # Quit the window on pressing Sapcebar key
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
