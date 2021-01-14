import os
from io import BytesIO
import shutil
import tempfile
from zipfile import ZipFile
import time
from datetime import timedelta
import re
import atexit
import subprocess

import eventlet
eventlet.monkey_patch()
from flask import Flask, session, Response, request, send_file, send_from_directory, make_response, jsonify
from flask_socketio import SocketIO,emit
from server_session import RedisSessionInterface
from redis import Redis
from rq import Queue
from rq.decorators import job
import urllib3
from PIL import Image
import numpy as np
import ffmpeg

from motor import Motor
from led import LED
from matrix import Matrix
from tasks import *

#============ Constants ============#
API_ROOT = 'http://localhost/api'
STREAM_URI = 'http://localhost/camera/stream'
CAPTURE_URI = 'http://localhost/camera/capture'

#============ Setup ============#
# Run external processes
processes = []
processes.append(subprocess.Popen(["rq", "worker"]))

# Set external processes to close on exit
def exit_processes():
    for p in processes:
        p.terminate()
    print("Terminated processes")

atexit.register(exit_processes)

# Setup hardware instances
m1 = Motor(0)
m2 = Motor(1)
m3 = Motor(2)

motors = []
for i in range(3):
    m = Motor(i)
    m.enable()
    m.set_step_type("micro-8")
    m.set_speed(25)
    motors.append(m)

x = motors[0]
y = motors[1]
z = motors[2]

led = LED()

matrix = Matrix()

# Set motors to close on exit
def exit_motors():
    for motor in motors:
        motor.disable()

atexit.register(exit_motors)

# Set led to turn off on exit
def exit_led():
    led.off()

atexit.register(exit_led)

# Create http pool manager instance to make http requests
http = urllib3.PoolManager()

# Setup Flask app
app = Flask(__name__)
app.config.from_pyfile('server.cfg')
app.session_interface = RedisSessionInterface()

# Setup Redis connection and queue
redis_conn = Redis()
app.q = Queue(connection=redis_conn)

# Set up storage dir
try:
    shutil.rmtree('data')
except FileNotFoundError:
    pass

os.mkdir('data')

# Set custom response which converts to json automatically
class ResponseCustom(Response):
    @classmethod
    def force_type(cls,r,environ=None):
        if isinstance(r,dict) or isinstance(r,list):
            r = jsonify(r)
        return super(ResponseCustom, cls).force_type(r,environ)

app.response_class = ResponseCustom

# Create flask-socketio app using above flask app
socketio = SocketIO(app, message_queue=app.config['SOCKETIO_REDIS_URL'],engineio_logger=app.config['DEBUG_ENGINE'])

#============ Helpers ============#
def get_response(data=None,status=200):
    date_string = time.strftime("%Y-%M-%d")
    time_string = time.strftime("%H:%M:%S")
    ts_string = date_string+' '+time_string
    response = {'status_code':status,'ts':ts_string,'data':data}

    return (response, status)

def capture():
    # Get raw image bytearray
    r = http.request('GET', CAPTURE_URI, timeout=2.0)

    # Convert bytearray to buffered stream
    jpg = BytesIO(r.data)

    return jpg

#============ Socket routes ============#
@socketio.on('motor',namespace='/gui')
def socket_motor(message):
    d = message["direction"]
    steps = message["steps"]
    axis = message["axis"]

    if(axis=="x"):
        m = x
    elif(axis =="y"):
        m = y
    elif(axis=="z"):
        m = z

    if(d==1):
        m.steps(steps)
    elif(d==0):
        m.steps(-steps)
    emit('log',{'data':'Moved {} motor {} steps in {} direction'.format(axis, steps,d)})

@socketio.on('led',namespace='/gui')
def socket_led(message):
    status = message["status"]

    if(status==1 or status=="on"):
        print("LED: on")
        led.on()
    elif(status==0 or status=="off"):
        print("LED: off")
        led.off()

    emit('log',{'data':'LED set to {}'.format(status)})

@socketio.on('ledbrightness',namespace='/gui')
def socket_led_brightness(message):
    increment = message['increment']
    led.up(increment)
    emit('log',{'data':'LED brightness changed by {}'.format(increment)})

@socketio.on('matrix',namespace='/gui')
def socket_matrix(message):
    status = message["status"]

    if(status==1 or status=="on"):
        print("Matrix: on")
        matrix.on()
    elif(status==0 or status=="off"):
        print("Matrix: off")
        matrix.off()

    emit('log',{'data':'Matrix set to {}'.format(status)})

@socketio.on('matrixbrightness',namespace='/gui')
def socket_matrix_brightness(message):
    print('received')
    increment = message['increment']
    matrix.up(increment)
    emit('log',{'data':'Matrix brightness changed by {}'.format(increment)})

@socketio.on('matrixpattern',namespace='/gui')
def socket_matrix_pattern(message):
    pattern = message['pattern']
    matrix.send_command(pattern)
    emit('log',{'data':'Matrix pattern changed to {}'.format(pattern)})

@socketio.on('motoronoff',namespace='/gui')
def socket_motoronoff(message):
    status = message["status"]

    if(status==1 or status=="on"):
        print("Motors: on")
        for motor in motors:
            motor.enable()
    elif(status==0 or status=="off"):
        print("motors: off")
        for motor in motors:
            motor.disable()

    emit('log',{'data':'LED set to {}'.format(status)})

#============ Normal routes ============#
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js',path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css',path )

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts',path )

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/timelapse', methods=['GET'])
def get_timelapse():
    return send_file('data/timelapse.mp4', mimetype='video/H264', attachment_filename='out.mp4',as_attachment=True)

@app.route('/zstack', methods=['GET'])
def get_zstack():
    return send_file('data/zstack.tiff', mimetype='image/tiff', attachment_filename='stack.tiff',as_attachment=True)

@app.route('/stitch', methods=['GET'])
def get_stitch():
    return send_file('data/stitch/stitch.zip', mimetype='application/zip', attachment_filename='stitch.zip',as_attachment=True)

#============ API routes ============#
@app.route('/api/help', methods=['GET'])
def help():
    text = '<h1>ENDPOINTS</h1>'
    text += '/camera/capture: capture '+'<br/>'
    text += '/camera/brightness: set brightness (0-100)' + '<br/>'
    return text

@app.route('/api/test',methods=['GET'])
def test():
    return get_response({'test':'ok'})

def get_all_settings():
    cmd = ['/usr/bin/v4l2-ctl', '-L']
    ret = subprocess.run(cmd, text=True, capture_output=True)

    output = ret.stdout
    lines = output.split('\n')

    settings = {}

    last_setting = ''
    for line in lines:
        setting = line.split(':')
        if len(setting) > 1:
            if setting[0].startswith('\t'):
                menu_name = setting[0].strip()
                menu_val = setting[1].strip().split(' ')[0]
                settings[last_setting]['menu'].append((menu_name, menu_val))
            else:
                setting_name = setting[0].strip().split(' ')[0]
                last_setting = setting_name
                setting_type = setting[0].strip().split(' ')[2]
                setting_type = setting_type.lstrip('(').rstrip(')')
                setting_params = setting[1].strip()
                setting_params = re.findall("(\w*)=(\w*)",setting_params)
                setting_params = dict(setting_params)
                setting_params['type'] = setting_type
                if 'menu' in setting_type:
                    setting_params['menu'] = []

                settings[setting_name] = setting_params

    return settings

def get_setting(control):
    cmd = ['/usr/bin/v4l2-ctl', '-C', control]
    ret = subprocess.run(cmd, text=True, capture_output=True)
    val = ret.stdout.split(control+': ')[1].rstrip()

    return val

def set_setting(control=None,value=None):
    if control is not None and value is not None:
        print("set")
        cmd = ['/usr/bin/v4l2-ctl', '-c', '{}={}'.format(control,value)]

        ret = subprocess.run(cmd, text=True, capture_output=True, check=True)

        value_new = get_setting(control)

        return value_new

@app.route('/api/camera/',methods=['GET'])
def camera_api():
    data = ['settings']
    return get_response(data)

@app.route('/api/camera/settings',methods=['GET'])
def camera_settings():
    r = get_all_settings()

    return get_response(r, 200)

@app.route('/api/camera/settings/<control>', methods=['GET','POST'])
def camera_setting(control=None):
    if control is not None:
        if request.method == "GET":
            val = get_setting(control)
            return get_response(val,200)
        elif request.method == "POST":
            data = request.get_json()

            if "value" in data:
                r = set_control(control,data["value"])
                return get_response(data=r["data"],status=r["status"]), r["status"]
            else:
                return get_response(data={"error": "Missing 'value' in POST data"}, status=400), 400

@app.route('/api/camera/settings/<control>/<val>', methods=['GET'])
def camera_setting_set(control=None, val=None):
    if control is not None and val is not None:
        val = set_setting(control, val)
        return get_response(val,200)


@app.route('/api/camera/capture', methods=['GET'])
def camera_capture():
    # Get query string arguments (after ?)
    args = request.args.copy()

    # Set default args
    default_args = {'format': 'jpg', 'filename': None}
    for key,value in default_args.items():
        args.setdefault(key,default=value)

    # Grab raw jpeg
    jpg = capture()

    # Store image in session
    if 'images' not in session:
        session['images'] = []

    # Store image in session
    if 'images' not in session:
        session['images'] = []

    # jpg.seek(0)
    session['images'].append(jpg)
    max_image = len(session['images'])

    # Return image url
    return get_response({'image': API_ROOT+'/images/'+str(max_image)})

@app.route('/api/images/', methods=['GET'])
def get_images():
    images = []
    if 'images' in session:
        images = [API_ROOT+'/images/'+ str(i+1) for i,img in enumerate(session['images'])  ]

    return get_response(images)

@app.route('/api/images/<id>', methods=['GET'])
def get_image(id):
    # Get query string arguments (after ?)
    args = request.args.copy()

    # Set default args
    default_args = {'filename': None}
    for key,value in default_args.items():
        args.setdefault(key,default=value)

    # Get image
    if 'images' not in session:
        session['images'] = []
    if 'images' in session:
        img = None
        if id == 'last':
            img = session['images'][-1]
            return send_file(img, mimetype='image/jpeg')
        else:
            try:
                img = session['images'][int(id)-1]
            except IndexError:
                return get_response({'status': 'Image not found'},404)
        if img is None:
            return "Error", 505

        if args["filename"] is None:
            return send_file(img, mimetype='image/jpeg')
        else:
            return send_file(img, mimetype='image/jpeg',attachment_filename=args["filename"],as_attachment=True)

    else:
        return "error"

@app.route('/api/images/<id>/delete', methods=['GET'])
def delete_image(id):
    if 'images' not in session:
        session['images'] = []
    if 'images' in session:
        if id == 'last':
            del session['images'][-1]
            return ([API_ROOT+'/images/'+ str(i+1) for i,img in enumerate(session['images'])])
        else:
            try:
                del session['images'][int(id)-1]
                return get_response([API_ROOT+'/images/'+ str(i+1) for i,img in enumerate(session['images'])])
            except IndexError:
                return get_response({'status': 'Image not found'},404)
    else:
        return "error"

#============ Task routes ============#
@app.route('/task/test')
def task_test():
    task = app.q.enqueue(background_task_test)
    return task.get_id()

@app.route('/task/test/<id>', methods=['GET'])
def task_test_status(id):
    task = app.q.fetch_job(id)
    if task is not None:
        return jsonify({'id': id, 'status': task.get_status(), 'result': task.result})
    else:
        return "Task not found"

@app.route('/task/timelapse', methods=['POST'])
def task_timelapse():
    data = request.get_json()

    # Build capture command
    cmd = ['/usr/bin/ffmpeg', '-i', STREAM_URI, '-t', str(data['t']), '-y', 'data/timelapse.mp4']

    # Emit start signal
    socketio.emit('timelapse_start', {}, namespace = "/task")

    # Run capture and emit completion signal
    try:
        ret = subprocess.run(cmd)

        if not ret.returncode:
            socketio.emit('timelapse_end', {'status': 'ok'}, namespace = "/task")
    except:
        socketio.emit('timelapse_end', {'status': 'fail'}, namespace = "/task")

    return get_response("ok")

@app.route('/task/zstack', methods=['POST'])
def task_zstack():
    data = request.get_json()
    steps = int(data['n'])
    stepsize = int(data['step'])

    # Emit start signal
    socketio.emit('zstack_start', {}, namespace = "/task")

    # Build image stack
    stack = []
    for i in range(0, steps):
        img = capture()
        stack.append(Image.open(img))

        # Emit progress
        socketio.emit('zstack_progress', {'curr': str(i+1), 'max': str(steps)}, namespace = "/task")

        # Take a step
        z.steps(stepsize)

        # Pause
        time.sleep()

    # Return to start
    z.steps(-steps*stepsize)

    # Create tiff export
    im = stack[0]
    im.save('data/zstack.tiff', format="tiff", append_images=stack[1:], save_all=True)

    # Emit job completion
    socketio.emit('zstack_complete', {'status': 'ok'}, namespace = "/task")

    return get_response("ok")

@app.route('/task/stitch', methods=['POST'])
def task_stitch():
    data = request.get_json()

    # Emit start signal
    socketio.emit('stitch_start', {}, namespace = "/task")

    try:
        shutil.rmtree('data/stitch')
    except FileNotFoundError:
        pass
    os.mkdir('data/stitch')

    images = []

    for j in range(0, int(data['y_steps'])):
        if j != 0:
            y.steps(int(data['y_stepsize']))

        for i in range(0,int(data['x_steps'])):
            if x != 0:
                if j % 2:
                    x.steps(-int(data['x_stepsize']))
                else:
                    x.steps(int(data['x_stepsize']))

            img = capture()

            images.append(img)

            # Emit progress
            socketio.emit('stitch_progress', {'curr_x': str(i+1), 'curr_y': str(j+1), 'max_x': data['x_steps'], 'max_y': data['y_steps']}, namespace = "/task")

    with ZipFile('data/stitch/stitch.zip', 'w') as myzip:
        for i,image in enumerate(images):
            im = Image.open(image)
            fname = 'data/stitch/'+str(i)+'.jpg'
            im.save(fname)
            myzip.write(fname)

    # Emit job completion
    socketio.emit('stitch_complete', {'status': 'ok'}, namespace = "/task")

    return get_response("ok")

def run():
    socketio.run(app,port=5000,debug=app.config['DEBUG_SERVER'])

if __name__ == '__main__':
    run()
