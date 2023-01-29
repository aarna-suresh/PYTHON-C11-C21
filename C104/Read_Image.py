import cv2

# Read Image
img = cv2.imread("butterfly.jpg")

# Display Colored Image
cv2.imshow("Display Image",img)

# Convert Colored Image To Grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Display Grayscale Image
cv2.imshow("Grayscale", gray_img)


#print(gray_img)

cv2.waitKey(0)