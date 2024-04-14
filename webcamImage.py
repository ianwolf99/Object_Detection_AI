import cv2

cap = cv2.VideoCapture("Could today's global conflicts bring a Third World War closer. - Inside Story.mp4")
# read from default webcam

# Set video properties

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# set width

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# set height

cap.set(cv2.CAP_PROP_BRIGHTNESS, 180)
# set brightness

cap.set(cv2.CAP_PROP_CONTRAST, 50)
# set contrast

success, img = cap.read()
while success:
	cv2.imshow("Webcam", img)

	# Press ESC key to break the loop
	if cv2.waitKey(10) & 0xFF == 27:
		break
	success, img = cap.read()

cap.release()
cv2.destroyWindow("Webcam")