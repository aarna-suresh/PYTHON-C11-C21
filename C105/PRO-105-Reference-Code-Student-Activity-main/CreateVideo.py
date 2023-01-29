import os
import cv2


path = "C:/Users/daran/Documents/PYTHON/C105/PRO-105-Reference-Code-Student-Activity-main/Images"

listOfImages = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        listOfImages.append(file_name)
        
print(len(listOfImages))
count = len(listOfImages)

frame = cv2.imread(listOfImages[0])
height, width, channels = frame.shape
size = (width,height)
print(size)


out = cv2.VideoWriter('friendship.mp4',cv2.VideoWriter_fourcc('m','p','4','v'), 5, size)

#For SUNSET
#for i in range(0,count-1):

#For SUNRISE
for i in range(count-1,0,-1):
    frame = cv2.imread(listOfImages[i])
    out.write(frame)
    
out.release() # releasing the video generated
print("Done")


