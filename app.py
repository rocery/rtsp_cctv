from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)

# URL RTSP untuk dua channel
rtsp_url_1 = "rtsp://admin:Admin123@192.168.7.201:554/Streaming/Channels/101"
rtsp_url_2 = "rtsp://admin:Admin123@192.168.7.202:554/Streaming/Channels/101"

import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

def generate_frames(rtsp_url):
    # Buka koneksi ke stream RTSP
    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print(f"Error: Tidak dapat membuka stream RTSP: {rtsp_url}")
        return

    while True:
        # Baca frame dari stream
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Gagal membaca frame dari {rtsp_url}.")
            break

        # Resize frame untuk mengurangi ukuran video
        scale_percent = 50  # Resize to 50% of the original size (adjust as needed)
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        resized_frame = cv2.resize(frame, (width, height))

        # Encode frame ke format JPEG
        ret, buffer = cv2.imencode('.jpg', resized_frame)
        if not ret:
            continue

        # Konversi frame ke byte dan kirim sebagai respons
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Tutup koneksi
    cap.release()

@app.route('/video_feed_1')
def video_feed_102():
    # Kirim stream MJPEG untuk channel 1
    return Response(generate_frames(rtsp_url_1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_2')
def video_feed_202():
    # Kirim stream MJPEG untuk channel 2
    return Response(generate_frames(rtsp_url_2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, threaded=True, debug=True)