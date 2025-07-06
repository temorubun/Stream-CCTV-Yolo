from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import numpy as np

app = Flask(__name__)

# Inisialisasi model YOLO
model = YOLO('yolov8n.pt')

def generate_frames():
    # RTSP URL
    rtsp_url = 'rtsp://admin:BGENWW@192.168.100.28:554/stream'
    
    # Buka koneksi RTSP
    cap = cv2.VideoCapture(rtsp_url)
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Lakukan deteksi menggunakan YOLO
            results = model(frame)
            
            # Gambar hasil deteksi
            annotated_frame = results[0].plot()
            
            # Encode frame untuk streaming
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 