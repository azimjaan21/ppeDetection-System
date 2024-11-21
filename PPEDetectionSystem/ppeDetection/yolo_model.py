from ultralytics import YOLO
import cv2
import numpy as np

# My PPE YOLOv8 Model
model = YOLO("yolov8n.pt")  


#class names
class_names = ['Person', 'goggles', 'helmet', 'no-goggles', 'no-helmet', 'no-vest', 'vest']


def run_detection(frame):
    results = model(frame)
    detections = []
    for r in results[0].boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = r
        detections.append({
            "x1": int(x1),
            "y1": int(y1),
            "x2": int(x2),
            "y2": int(y2),
            "confidence": conf,
            "class_id": int(cls),  
            "label": class_names[int(cls)],  
        })
    return detections