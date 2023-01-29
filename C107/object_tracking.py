import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("bb3.mp4")

# Load tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
#tracker.init(img, bbox)


if (img.x >= 0 and img.y >= 0 and (img.width + img.x < video.cols) and img.height + img.y < video.rows):
    tracker.init(img, bbox)
else:
    pass


print(bbox)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255, 0, 255), 3, 1)

    cv2.putText(img, "Tracking", (75, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# the code to draw a circle at the center point of
# the basketball:
# ● Create a variable c1 and c2
# To get the center point of the bounding box, we will add
# half of width in x and half of height in y.
# ● Set the values of c1 as x plus half the width of the
# bounding box.
# ● Set the values of c2 as y plus half the height of the
# Get the center points:
# ● Create a point at the center(approximately) of
# the basketball hoop and the basketball
# bounding box.
# 6. Plot the trajectory using center points
# ● Calculate distance between the two points.
# ● If distance is less than a value, then display
# the goal on the video.


def goal_track(img, bbox):
    #     "Parameters:
    # ○ image: The image to draw the circle on.
    # ○ center points: x and y coordinates of the
    # center of the circle, which is represented by
    # c1 and c2 in this case.
    # ○ radius: Radius of the circle.
    # ○ color: Color of the circle, red (0, 0, 255) in
    # this case.
    # ○ thickness: Thickness of the circle"
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    # Get the CENTER Points of the Bounding Box
    c1 = x + int(w/2)
    c2 = y + int(h/2)

    # Draw a small circle using CENTER POINTS
    cv2.circle(img, (c1, c2), 2, (0, 0, 255), 5)

    cv2.circle(img, (int(p1), int(p2)), 2, (0, 255, 0), 3)

    # Calculate Distance
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    # Goal is reached if distance is less than 20 pixel points
    if (dist <= 20):
        cv2.putText(img, "Goal", (300, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0, 0, 255), 5)


while True:

    check, img = video.read()

    # Update the tracker on the img and the bounding box
    success, bbox = tracker.update(img)

    # Call drawBox()
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost", (75, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Call goal_track()
    goal_track(img, bbox)

    # Display Video
    cv2.imshow("result", img)

    # Quit Display Window when Spacebar key is pressed
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break

video.release()
cv2.destroyALLwindows()
