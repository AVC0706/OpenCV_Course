import cv2
import numpy as np


#Translations
def translate(image , x ,y):
     M = np.float32( [ (1 , 0 , x) , (0 , 1 , y) ] )
     shifted = cv2.warpAffine( image , M , ( image.shape[1] , image.shape[0] ) )
     return shifted

#Rotation
def roatate( image , angle , center=None , scale=1.0 ):
    (h , w) = image.shape[:2]
    if center is None:
        center = ( h//2 , w//2 )

    M = cv2.getRotationMatrix2D( center , angle , scale )
    rotated = cv2.warpAffine( image , M , ( w , h ) )         
    return rotated

#Rresize
def resize( image , width = None , height = None , inter = cv2.INTER_AREA ):

    dim = None

    ( h , w ) = image.shape[ : 2 ]

    if width is None and height is None :
        return image

    if width is None :
        ratio = height / float(h)
        dim = (  int(w * ratio) , height )

    else :
        ratio = width / float(w)
        dim = ( width , int( h * ratio) )

    resized = cv2.resize( image , dim , interpolation = inter )
    return resized    

