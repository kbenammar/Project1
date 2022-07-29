from SpacebotLED import stop_action,default_setup,bingo_action,blink_disco,picture_flash,loading_cycle,pulse
from flask import Flask

purple=(250,0,250)
green=(127,255,0)
green2=(118,238,0)
green3=(0,255,0)
green4=(0,238,0)
green5=(173,255,47)
orange=(255,128,0)
blue=(187,255,255)
blue2=(174,238,238)
blue3=(0,245,255)


app = Flask(__name__)

@app.route('/stop')
def stop():
    stop_action()
    return "Action stopped"

@app.route('/default')
def default():
    default_setup()
    return "Spacebot Blue"

@app.route('/disco')
def disco():
    for i in range(15):
        blink_disco(.5,.2)
    return "Disco party"

@app.route('/bingo')
def bingo():
    for i in range(15):
        bingo_action()
    return "Bingoooo"

@app.route('/picture')
def picture():
    picture_flash(2)
    return "Say Cheeeeeese"

@app.route('/loading')
def loading():
    for i in range(15):
        loading_cycle(purple)
    return "loading"

@app.route('/linked')
def linked():
    dark=.5
    speed=.1
    pulse(purple,dark,speed)
    return "linked"


@app.route('/leave')
def leave():
    dark=.6
    speed=.3
    for i in range(5):
        pulse(orange,dark,speed)
    return "Have a good night XP"
    

if __name__ == "__main__":
    app.run(debug=True,port=80,host='0.0.0.0')
