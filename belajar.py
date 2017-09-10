import cv2
image = cv2.imread('C:\Users\Rusdian\Documents\CodePython\Capture.PNG')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('rusdy.jpg', gray)
