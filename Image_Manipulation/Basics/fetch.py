import argparse
import cv2 


ap = argparse.ArgumentParser()
ap.add_argument( "-i" , "--image" , required = True , help="Path to image" )
args = vars( ap.parse_args() ) 

image = cv2.imread( args["image"] )
print( "width : {} pixels".format(image.shape[0]) )
print( "height : {} pixels".format(image.shape[1]) )
print( "channels : {} pixels".format(image.shape[2]) )

cv2.startWindowThread()
cv2.namedWindow("preview")
cv2.imshow( "Image Title" , image)
cv2.waitKey(0)
cv2.imwrite( "newcat.jpg" , image)