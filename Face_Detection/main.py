
from PIL import Image
import face_recognition
import cv2


image = face_recognition.load_image_file( "g1.jpg" )

face_locations = face_recognition.face_locations( image )

# printing the number of items in the array

for face_location in face_locations:

	#print location of each face in this image
	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

	#access and show each face in the image
	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	
	pil_image.show()


