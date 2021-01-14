from flask_socketio import SocketIO,emit
import time

def background_task_test():
    print('Running background task test')
    time.sleep(5)
    return "Completed successfully"