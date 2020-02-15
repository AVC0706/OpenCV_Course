import argparse
import cv2 


ap = argparse.ArgumentParser()
ap.add_argument( "-i" , "--image" , required = True , help="Path to image" )
args = vars( ap.parse_args() ) 

image = cv2.imread( args["image"] )

(b,g,r) = image[0,0]
print("Pixel at 0,0 - R {} , G {} , B {}\n".format(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print("Pixel at 0,0 - R {} , G {} , B {}".format(r,g,b))

corner = image[0:100 , 0:100]
cv2.imshow("Corner" , corner)
cv2.waitKey(0)

image[0:100 , 0:100] = (0 , 255 , 0) 
cv2.imshow("Image" , image)
cv2.waitKey(0)
cv2.imwrite("greencat.jpeg" , image)