import numpy as np
import argparse

import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow( "Bgr" , image )
cv2.waitKey(0)

#Grey
grey = cv2.cvtColor( image , cv2.COLOR_BGR2GRAY )
cv2.imshow( "Grey" , grey )
cv2.waitKey(0)


#HSV
hsv = cv2.cvtColor( image , cv2.COLOR_BGR2HSV )
cv2.imshow( "Hsv" , hsv )
cv2.waitKey(0)

#Lab
lab = cv2.cvtColor( image , cv2.COLOR_BGR2LAB )
cv2.imshow( "Lab" , lab )
cv2.waitKey(0)





