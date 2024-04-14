from ultralytics import YOLO
import torch
#LOAD THE MODEL
model = YOLO('yolov5n.pt')

results = model.predict(source='http://127.0.0.1:8002/bus.jpg',save=True)


