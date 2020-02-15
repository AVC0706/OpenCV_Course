from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])


chans = cv2.split( image )
colors = ( "b" , "g" , "r" )

plt.figure()
plt.title("Color Hist")
plt.xlabel( "Bins" )
plt.ylabel( "No. of Pixels" )


for (chan , color) in zip(chans , colors):
    hist = cv2.calcHist( [chan] , [0] , None , [256] , [0 , 256] )
    plt.plot( hist , color = color )
    plt.xlim( [ 0 , 256 ] )

plt.show()
# # BGR to GRAY
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("GRAY", gray)
# cv2.waitKey(0)

# hist = cv2.calcHist( [image] , [0] , None , [256] , [ 0 , 256 ] )

# plt.figure()
# plt.title( "Gray Scale" )
# plt.xlabel( "Bins" )
# plt.ylabel( "No. of Pixels" )
# plt.plot(hist)
# plt.xlim( [ 0 , 256 ] )
# plt._show()

cv2.waitKey(0)