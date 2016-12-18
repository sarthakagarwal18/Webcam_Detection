import cv2

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascade_face.xml')

#Initialize Webcam
webcam=cv2.VideoCapture(0)

while (webcam.isOpened()):
	
	# Capture frame-by-frame
	# cap.read() returns a bool (True/False). If frame is read correctly, it will be True..this is stored in ret
	ret,img=webcam.read()

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = 0)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow('faces',img)
	
	#Press Esc to close window
	k=cv2.waitKey(1)
	if k==27:
		break

webcam.release()
cv2.destroyAllWindows()