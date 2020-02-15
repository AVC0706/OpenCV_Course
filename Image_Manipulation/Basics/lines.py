import numpy as np
import cv2

canvas = np.zeros( (500 , 500 , 3 ) , dtype="uint8" )


green = (0 , 255 , 0)
cv2.line(canvas , (0,0) , (255 , 255) , green , 10 )

red = (0 , 0 , 255)
cv2.rectangle( canvas , (50 , 50) , (150 , 150) ,red , -1 )

cv2.imshow("Canvas" , canvas)
cv2.waitKey(0)

#blue = ( 255 , 0 , 0 )
#cv2.circle( canvas , (100 , 100) , 20 , blue , 12) 

(cx , cy) = ( canvas.shape[1]//2 , canvas.shape[0]//2 )

white = (255 , 255 , 255)

for r in range( 0 , 250 , 25):
    cv2.circle( canvas , (cx , cy) , r , white , 3)

cv2.imshow("Canvas" , canvas)
cv2.waitKey(0)