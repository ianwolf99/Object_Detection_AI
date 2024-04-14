import cv2
import threading
from ultralytics import YOLO

# Step 1.3: Import the Threading Module
import threading

# Step 2.1: Define Video File Paths
video_file1 = 'ultralytics\\test.mp4'  # Video file path
video_file2 = 0  # WebCam Path

# Step 2.2: Load YOLOv8 Models
model1 = YOLO('yolov8n.pt')  # YOLOv8n Model
model2 = YOLO('yolov8s.pt')  # YOLOv8s Model

# Step 2.3: Target Function for Thread
def run_tracker_in_thread(filename, model, file_index):
    """
    This function is designed to run a video file or webcam stream
    concurrently with the YOLOv8 model, utilizing threading.

    - filename: The path to the video file or the webcam/external
    camera source.
    - model: The YOLOv8 model instance.
    - file_index: An argument to specify the count of the
    file being processed.
    """

    video = cv2.VideoCapture(filename)  # Read the video file

    while True:
        ret, frame = video.read()  # Read the video frames

        # Exit the loop if no more frames in either video
        if not ret:
            break

        # Track objects in frames if available
        results = model.track(frame, persist=True)
        res_plotted = results[0].plot()
        cv2.imshow("Tracking_Stream_" + str(file_index), res_plotted)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release video sources
    video.release()

# Step-2.4: Create the Object Tracking Threads
tracker_thread1 = threading.Thread(target=run_tracker_in_thread,
                                   args=(video_file1, model1, 1),
                                   daemon=True)

tracker_thread2 = threading.Thread(target=run_tracker_in_thread,
                                   args=(video_file2, model2, 2),
                                   daemon=True)

# Step-2.5: Start the Object Tracking Threads
tracker_thread1.start()
tracker_thread2.start()

# Step-2.6: Thread Handling and Destroy Windows
tracker_thread1.join()
tracker_thread2.join()

# Clean up and close windows
cv2.destroyAllWindows()
