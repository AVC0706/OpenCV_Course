import cv2
import argparse
import utils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument( "-i" , "--image" , required = True , help="Path to image" )
args = vars( ap.parse_args() ) 

image = cv2.imread( args["image"] )

#Translations
shifted = utils.translate( image , 100 , 100 )

cv2.imshow("Shited" , shifted)
cv2.waitKey(0)

#Rotation
rotated = utils.roatate( image , -45 , (100 , 100)  )

cv2.imshow( "Roatated" , rotated )
cv2.waitKey(0)


#Rresize
resized = utils.resize( image , width=200  )

cv2.imshow( "Resized" , resized )
cv2.waitKey(0)


#flip
flipped = cv2.flip( image , 0 )
cv2.imshow( "Hflip" , flipped )
cv2.waitKey(0) 

flipped = cv2.flip( image , -1 )
cv2.imshow( "Bflip" , flipped )
cv2.waitKey(0)


#cropping
cropped = image[ 15:300 , 150 : 400 ]
cv2.imshow( "Cropped Image" , cropped )
cv2.waitKey(0)