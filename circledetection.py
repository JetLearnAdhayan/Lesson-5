import cv2 
import numpy as np

image = cv2.imread("image.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blur1 = cv2.blur(gray,(3,3))

detected_circles = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT,1,20,param1 = 50,param2 = 30, minRadius=1,maxRadius=40)

print(detected_circles)

if detected_circles is not None: 
    #Convert the circle parameters x,y and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
    print(detected_circles)
    for i in detected_circles[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(image, (x,y), r,(0,255,0),2)
        cv2.circle(image,(x,y), 1,(0,0,255),2)

    cv2.imshow("detected circles", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

