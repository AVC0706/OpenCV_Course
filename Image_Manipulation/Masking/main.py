import numpy as np
import argparse

import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

mask = np.zeros( image.shape[ : 2 ]  , dtype="uint8" )

(cx , cy) = ( image.shape[1]//2 , image.shape[0]//2 )
cv2.rectangle( mask , ( cx-75 , cy-75 ) , ( cx+75 , cy+75 ) , 255 , -1 )
cv2.imshow("Mask" , mask)
cv2.waitKey(0)

masked = cv2.bitwise_and( image , image , mask = mask )
cv2.imshow( "Masked Img" , masked )
cv2.waitKey(0)

(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)


#alternate method
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

#merge back the channels
merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)
cv2.waitKey(0)





