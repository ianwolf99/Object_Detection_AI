import cv2
import torch
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Define the video source (local video file path or URL)
video_source = 'video1.mp4'  # Update with your video file path or URL

# Open the video source using OpenCV
cap = cv2.VideoCapture(video_source)

# Check if the video source was opened successfully
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Loop through the video frames
while True:
    # Read a frame from the video source
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break  # Break the loop if no more frames

    # Perform inference with YOLOv5 on the frame
    results = model(frame)

    # Get bounding boxes, labels, and scores of detected objects
    bboxes = results.xyxy[0]  # Get all detected bounding boxes
    labels = bboxes[:, 5]  # Get labels (class indices) of detected objects
    scores = bboxes[:, 4]  # Get confidence scores of detected objects

    # Draw bounding boxes and labels on the frame
    for bbox, label, score in zip(bboxes[:, :4], labels, scores):
        x1, y1, x2, y2 = map(int, bbox)  # Convert bounding box coordinates to integers
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw bounding box
        cv2.putText(frame, f'{model.names[int(label)]} {score:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Draw label and score

    # Display the frame with detected objects
    cv2.imshow('Object Detection', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video source and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
