<!DOCTYPE html>
<html>

<head>
    <title>Object Detection AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }

        h1,
        h2,
        h3 {
            color: #007bff;
        }

        .repo-description {
            margin-bottom: 20px;
        }

        .code-block {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        .section {
            margin-bottom: 30px;
        }

        .list-item {
            margin-bottom: 10px;
        }

        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 12px;
            color: #666;
        }
    </style>
</head>

<body>

    <h1>Object Detection AI</h1>
    <p class="repo-description">Welcome to the Object Detection AI repository! This project contains scripts and resources for object detection using various AI models and computer vision techniques.</p>

    <div class="section">
        <h2>Scripts</h2>
        <div class="list-item">
            <strong>FLIP.py:</strong> Python script to flip images horizontally and vertically.
        </div>
        <div class="list-item">
            <strong>Grayscale_images.py:</strong> Python script to convert images to grayscale.
        </div>
        <div class="list-item">
            <strong>Rotate.py:</strong> Python script to rotate images by a specified angle.
        </div>
        <div class="list-item">
            <strong>detect.py:</strong> Python script for object detection using YOLOv5 model.
        </div>
        <!-- Add more scripts here -->
    </div>

    <div class="section">
        <h2>Models</h2>
        <div class="list-item">
            <strong>yolov5n.pt:</strong> Pre-trained YOLOv5 model checkpoint.
        </div>
        <div class="list-item">
            <strong>yolov5s.pt:</strong> Pre-trained YOLOv5 small model checkpoint.
        </div>
        <div class="list-item">
            <strong>yolov8n-seg.pt:</strong> Pre-trained YOLOv8 segmentation model checkpoint.
        </div>
        <!-- Add more models here -->
    </div>

    <div class="section">
        <h2>Images and Videos</h2>
        <div class="list-item">
            <strong>bus.jpg:</strong> Sample image of a bus.
        </div>
        <div class="list-item">
            <strong>car.jpg:</strong> Sample image of a car.
        </div>
        <div class="list-item">
            <strong>video1.mp4:</strong> Sample video file for testing object detection.
        </div>
        <!-- Add more images and videos here -->
    </div>

    <div class="section">
        <h2>Usage</h2>
        <p>To run the scripts, ensure you have the required dependencies installed. You can use the following commands:</p>
        <div class="code-block">
            pip install -r requirements.txt
        </div>
    </div>

    <div class="section">
        <h2>Contributing</h2>
        <p>Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.</p>
    </div>

    <footer>
        &copy; 2024 Object Detection AI | Created by ianwolf99
    </footer>

</body>

</html>
