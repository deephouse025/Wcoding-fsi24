# """
#     Stopwatch - Features:
#     - Persists between browser refreshes.
#     - Updates per second
#     - Start/stop/reset
#     - Stores all previous times just prior to reset
# """


import time
from datetime import datetime
from flask import Flask

app = Flask(__name__)

start_time = 0

# @app.get("/start")

running = True
start_time = datetime.now()

while True:
    elapsed_time = datetime.now() - start_time
    print(elapsed_time)
    time.sleep(0.1)
    if elapsed_time.seconds >= 2:
        exit()



