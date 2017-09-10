import cv2
image = cv2.imread('C:\Users\Rusdian\Documents\CodePython\Capture.PNG')
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('rusdy3.jpg', image)
