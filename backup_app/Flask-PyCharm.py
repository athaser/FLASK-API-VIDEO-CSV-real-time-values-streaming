from flask import Flask, render_template, request
from flask_mail import Mail, Message
import asyncio
import sched, time
from threading import Thread
import datetime, time


app = Flask(__name__)
mail = Mail()

def do_something_1(sc): 
    print("Doing stuff...")
    #global g, aaa
    #aaa = table_sos[g-1]
    #print(aaa)
    #g=g+1
    return("aaa")


#g=int(0)
#table_time_update=[]
s = sched.scheduler(time.time, time.sleep)

def do_something_2(sc):
    global x
    while True:
        x = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        return(x)

#clock()


@app.route('/')
def index(name=None):
    #author = "Thanos"
    s.enter(3, 1, do_something_2, (s,))
    thread_1 = Thread(target = s.run(), args = (3, ))
    thread_1.start()
    thread_1.join()
    return render_template('homepage.html', name=name, random_quote=thread_1)

rest_hostname = "0.0.0.0"
rest_port = 4444

if __name__ == '__main__':
    app.run(host=rest_hostname, port=rest_port, debug=True)
