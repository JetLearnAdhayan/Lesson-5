import cv2
import numpy as np

image = cv2.imread("image.png",0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.8

params.filterByConvexity = True
params.minConvexity = 0.9

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

key_points = detector.detect(image)

print(key_points)

number_of_blobs = len(key_points)

print(number_of_blobs)

#drawKeypoints(input_image, key_points, output_image,colour,,flag)

blank = np.zeros((1,1))

blobs = cv2.drawKeypoints(image, key_points,blank,(0,0,255), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

text = "Number of Circular Blobs:" + str(number_of_blobs)

position = (50,50)
font = cv2.FONT_ITALIC
color = (0,255,0)
thickness = 2 

cv2.putText(blobs,text,position,font,1,color,thickness)













cv2.imshow("final image", blobs)




cv2.waitKey(0)
cv2.destroyAllWindows()


