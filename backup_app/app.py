from flask import Flask, Response, request, render_template, render_template_string, stream_with_context
import time

app = Flask(__name__)
timing=0
@app.route('/content', methods=['POST', 'GET']) # render the content a url differnt from index. This will be streamed into the iframe
def content():
    global timing
    timing = 10
    # if request.form.get("submit"):
        # timing = request.form['timing']
        # print(timing)
    def countdown(t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            yield timer
            time.sleep(1)
            t -= 1
        # return timer
        
    return app.response_class(countdown(timing)) #at the moment the time value is hardcoded in the function just for simplicity
    # return render_template('display.html')
@app.route('/')
def index():
    value = "Bonjour"
    title_html = value
    return render_template('homepage.html', message=title_html) # render

rest_hostname = "0.0.0.0"
rest_port = 4444

if __name__ == '__main__':
    app.run(host=rest_hostname, port=rest_port, debug=True)
