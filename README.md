# Installation
## Create and activate a new virtual environment (Recommended)
For example:
```
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```

## Install required packages
```
pip install -r requirements.txt
```
NB. For development without a Raspberry Pi, also install requirements-dev.txt

## Set up camera image stream
An mjpeg image stream is expected at localhost/camera/stream. This can be achieved using software such as mjpg-streamer. 

If using the official Raspberry Pi camera, instructions to install this can be found here: https://github.com/jacksonliam/mjpg-streamer. Once built, mjpg-streamer can be used as follows to set up a stream on localhost at port 8080, for example:

```
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
```

## Serve the application
Set up a reverse proxy to serve flask the application via the conventional port 80 and the image stream on /camera/stream.

An example nginx configuration (using the default Flask port of 5000) is given below:

```
server {
    listen 80;
    server_name _;

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000;
    }

    location /socket.io {
        include proxy_params;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_pass http://127.0.0.1:5000/socket.io;
    }

    location /camera/stream {
        proxy_pass http://127.0.0.1:8080/?action=stream;
    }

    location /camera/capture {
        proxy_pass http://127.0.0.1:8080/?action=snapshot;
    }

}
```

# Usage
```
python server.py
```