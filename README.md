BELUM DICOBA PADA OS WINDOWS

1. Install venv, pip, dan ffmpeg
   sudo apt install python3-venv pyhton3-pip ffmpeg -y
2. mkdir cctv
3. cd cctv
4. python3 -m venv venv
5. source ./venv/bin/activate
6. pip3 install flask opencv-python
7. python3 app.python3


Jika dirasa bandwidth streaming terlalu besar, atur konfigurasi kamera
atau turunkan persentase 'resize, pada app.py

edit variabel ini
rtsp_url_1 = "rtsp://admin:Admin123@192.168.7.201:554/Streaming/Channels/101"
rtsp_url_2 = "rtsp://admin:Admin123@192.168.7.202:554/Streaming/Channels/101"