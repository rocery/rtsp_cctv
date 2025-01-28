import cv2

# URL RTSP dari DVR Hikvision
rtsp_url = "rtsp://admin:admin123@192.168.10.245:554/Streaming/Channels/501"

import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"  # Gunakan UDP untuk mengurangi latensi
cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

# Periksa apakah stream berhasil dibuka
if not cap.isOpened():
    print("Error: Tidak dapat membuka stream RTSP.")
    exit()

# Buat jendela dengan nama "RTSP Stream"
cv2.namedWindow("RTSP Stream", cv2.WINDOW_NORMAL)

# Set jendela ke mode maximized
# cv2.setWindowProperty("RTSP Stream", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Loop untuk membaca dan menampilkan frame
while True:
    # Baca frame dari stream
    ret, frame = cap.read()

    # Jika frame tidak berhasil dibaca, hentikan loop
    if not ret:
        print("Error: Gagal membaca frame.")
        break

    # Tampilkan frame di jendela
    cv2.imshow("RTSP Stream", frame)

    # Tekan 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup koneksi dan jendela
cap.release()
cv2.destroyAllWindows()