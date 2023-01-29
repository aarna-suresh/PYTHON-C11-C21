import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("output", img)

# height, width, number of channels in image 
dimensions = img.shape
height = img.shape[0] 
width = img.shape[1] 
channels = img.shape[2]
 
print('Image Dimension : ',dimensions) 
print('Image Height : ',height) 
print('Image Width : ',width) 
print('Number of Channels : ',channels)


cv2.waitKey(10000)




#labels for the sun
cv2.putText(img,"Sun",(70,400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for mercury : 
cv2.putText(img,"Mercury",(120, 300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for venus : 
cv2.putText(img,"Venus",(300, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for earth : 
cv2.putText(img,"Earth",(400, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for mars : 
cv2.putText(img,"Mars",(500, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for jupiter : 
cv2.putText(img,"Jupiter",(600, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for saturn : 
cv2.putText(img,"Saturn",(700, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for neptune : 
cv2.putText(img,"Neptune",(800, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
#labels for uranus : 
cv2.putText(img,"Uranus",(900, 400),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))

cv2.imwrite("Solar_systemwithname.jpg",img)
imgWithLabels = cv2.imread("Solar_systemwithname.jpg")
cv2.imshow("outputWithLabels", imgWithLabels)
cv2.waitKey(5000)