import io 
import cv2
import numpy as np

from PIL import Image
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

model = YOLO("yolov8n.pt") 

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files['image']
    image = Image.open(image.stream)
    print(type(image))
    results = model.predict(image)

    detections = []
    for r in results:        
        boxes = r.boxes
        for box in boxes:
            x, y, w, h = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            cls = box.cls
            conf = box.conf
            label = model.names[int(cls)]

            detections.append({'label': label, 'confidence': float(conf), 'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})

    return jsonify(detections)


if __name__ == '__main__':

    app.run(debug=True)