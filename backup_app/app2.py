from flask import Flask, Response, request, render_template, render_template_string, stream_with_context
import time

app = Flask(__name__)
import datetime
import time
def clock():
    while True:
        x = datetime.datetime.now().strftime("%H:%M:%S"), end="\r"
        time.sleep(1)

clock()

rest_hostname = "0.0.0.0"
rest_port = 4444

if __name__ == '__main__':
    app.run(host=rest_hostname, port=rest_port, debug=True)
