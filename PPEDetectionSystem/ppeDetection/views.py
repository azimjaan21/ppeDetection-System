from django.shortcuts import render

from django.http import StreamingHttpResponse
from .yolo_model import run_detection
import cv2

def video_feed():
    camera = cv2.VideoCapture(0)  # 0 for webcam

    while True:
        success, frame = camera.read()
        if not success:
            break

        # Run YOLO Detection
        detections = run_detection(frame)

        # Draw Bounding Boxes
        for detection in detections:
            x1, y1, x2, y2 = detection["x1"], detection["y1"], detection["x2"], detection["y2"]
            label = f"{detection['label']} ({detection['confidence']:.2f})"
            color = (0, 255, 0) if "no-" not in detection["label"] else (0, 0, 255)  # Green for compliance, Red for non-compliance
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')