import numpy as np
import cv2

rectangle = np.zeros( (300 , 300) , dtype="uint8" )
cv2.rectangle( rectangle , ( 25, 25 )  , ( 275 , 275 ) , 255 , -1 )
cv2.imshow("Retangle" , rectangle)

circle = np.zeros( (300 , 300) , dtype="uint8" )
cv2.circle( circle , ( 150 , 150 )  , 150 , 255 , -1 )
cv2.imshow("Circle" , circle)
cv2.waitKey(0)

bitwisAnd = cv2.bitwise_and( rectangle , circle )
cv2.imshow( " And " , bitwisAnd)
cv2.waitKey(0)

bitwisor = cv2.bitwise_or( rectangle , circle )
cv2.imshow( " Or " , bitwisor)
cv2.waitKey(0)
bitwisxor = cv2.bitwise_xor( rectangle , circle )
cv2.imshow( " xor " , bitwisxor)
cv2.waitKey(0)

bitwisenot = cv2.bitwise_not( rectangle , circle )
cv2.imshow( " not" , bitwisenot)
cv2.waitKey(0)