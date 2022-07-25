from glob import glob
import re
import sys
from flask import Flask, render_template
from turbo_flask import Turbo


app = Flask(__name__)
turbo = Turbo(app)

@app.route('/')
def index():
    global rou
    rou = True
    return render_template('index.html')

@app.route('/page2')
def page2():
    global rou
    rou = False
    return render_template('page2.html')

import csv
counter=0
counter2=0

@app.context_processor
def inject_load():
    #load = [int(random.random() * 100) / 100 for _ in range(3)]
    with open('predictions_normal.csv', newline='') as csvfile:
        global counter
        reader=csv.reader(csvfile)
        load=[r for r in reader]
        #print (load[counter][1])
        counter+=1
    with open('predictions_fight.csv', newline='') as csvfile_2:
        global counter2
        reader_2=csv.reader(csvfile_2)
        load_2=[r for r in reader_2]
        #print (load_2[counter][1])
        counter2+=1
    return {'load1': load[counter][0], 'load5': load[counter][1], 'load15': load_2[counter2][0], 'load20':load_2[counter2][1]}

import time

def update_load():
    with app.app_context():
        while True:
            time.sleep(0.5)
            if rou == True:
                turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))
            else:
                turbo.push(turbo.replace(render_template('loadavg_2.html'), 'load'))
            #turbo.push(turbo.replace(render_template('loadavg_2.html'), 'load_2'))

import threading


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

rest_hostname = "0.0.0.0"
rest_port = 4444

if __name__ == '__main__':
    app.run(host=rest_hostname, port=rest_port, debug=True)
