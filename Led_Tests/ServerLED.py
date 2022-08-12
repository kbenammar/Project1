from SpacebotLED import stop_action,default_setup,bingo_action,blink_disco,picture_flash,loading_cycle,pulse,solid
from WeatherAPI import get_weather
from flask import Flask
from flask import render_template

color_dict = {
'red':(255,0,0),
'purple':(250,0,250),
'green':(127,255,0),
'green2':(0,150,0),
'ice_blue':(173,255,47),
'blue':(16,78,139),
'dark_blue':(0,0,139),
'yellow':(150,50,0),
'orange':(200,30,0),
'dark_orange':(250,30,0),
'dust':(150,40,0),
'dark_grey':(250,250,250),
}

app = Flask(__name__)

@app.route('/stop')
def stop():
    stop_action()
    return "Action stopped"

@app.route('/default')
def default():
    default_setup()
    return "Spacebot Blue"

@app.route('/<color>')
def steady(color):
    solid(color_dict[color])
    return render_template("running.html",color=color)

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
        loading_cycle(color_dict['purple'])
    return "loading"

@app.route('/linked')
def linked():
    dark=.5
    speed=.1
    pulse(color_dict['purple'],dark,speed)
    return "linked"


@app.route('/leave')
#triggered at 5pm?
def leave():
    weather_dict = get_weather()
    id = weather_dict['weather'][0]['id']
    main = weather_dict['weather'][0]['main']
    description = weather_dict['weather'][0]['description']
    icon = weather_dict['weather'][0]['icon']
    temperature = weather_dict['main']['temp']
    
    if main=="Clear":
        
        if temperature > 30:
            dark=.3
            speed=.1
            for i in range(5):
                pulse(color_dict['dark_orange'],dark,speed)
            return "Hot weather, make sure to stay hydrated"
        elif 15 <= temperature and temperature < 30:
            dark=.5
            speed=.3
            for i in range(5):
                pulse(color_dict['orange'],dark,speed)
        elif temperature <15:
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['yellow'],dark,speed)
                
    elif main == "Clouds":
        
        if id == 801:
            #top led line yellow, rest light grey, slow, clouds
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['light_grey'],dark,speed)
        elif id == 802:
            #light grey,normal, clouds
            dark=.5
            speed=.3
            for i in range(5):
                pulse(color_dict['light_grey'],dark,speed)  
        elif id == 803 or id == 804:
            #drk grey, fast, clouds
            dark=.3
            speed=.1
            for i in range(5):
                pulse(color_dict['dark_grey'],dark,speed)
                
    elif main=="Rain":
        
        if id == 500 or id == 501:
            #blue, slow, raindrops
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['blue'],dark,speed)  
        elif id == 502:
            #top led line grey, rest-dark-blue, regular, raindrops
            dark=.5
            speed=.3
            for i in range(5):
                pulse(color_dict['blue3'],dark,speed)
        elif id == 503 or id == 504:
            #top led line dark grey, rest dark-blue, fast, raindrops
            dark=.3
            speed=.1
            for i in range(5):
                pulse(color_dict['blue3'],dark,speed)  
        elif id == 511 :
            #light-blue/ice-blue, slow, raindrops
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['ice_blue'],dark,speed)  
        elif id == 520:
            #top led line yellow, rest blue, slow, raindrops
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['blue'],dark,speed)  
        elif id == 521:
            #top led line yellow, rest dark blue, regular, raindrops
            dark=.5
            speed=.3
            for i in range(5):
                pulse(color_dict['blue3'],dark,speed)  
        elif id == 522 or id == 531:
            #top led line yellow, rest dark blue, fast, raindrops
            dark=.3
            speed=.1
            for i in range(5):
                pulse(color_dict['blue3'],dark,speed)
                
    elif main == "Drizzle":
        #top led line grey, rest-dark-blue, slow, raindrops
        dark=.7
        speed=.5
        for i in range(5):
            pulse(color_dict['blue3'],dark,speed)
            
    elif main == "Thunderstorm": 
        #top led line dark-gry, rest blue, regular, raindrops, borrom line/left corner blink/thunder yellow fast
        dark=.5
        speed=.3
        for i in range(5):
            pulse(color_dict['blue3'],dark,speed)
            
    elif main == "Snow":
        
        if id == 600 or id == 615:
            #ice-blue/white, slow, raindrops
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['blue'],dark,speed)  
        elif id == 612 or id == 620:
            #top led line yellow, rest ice-blue/white, slow, raindrops
            dark=.7
            speed=.5
            for i in range(5):
                pulse(color_dict['blue'],dark,speed)  
        elif id == 601 or id == 611 or id == 616:
            #ice-blue/white,regular, raindrops
            dark=.5
            speed=.3
            for i in range(5):
                pulse(color_dict['blue'],dark,speed)  
        elif id == 613 or id == 621:
            #top led line yellow, retice-blue/white, regular, raindrops
            dark=.5
            speed=.3
            for i in range(5):
                pulse(colro_dict['blue'],dark,speed)  
        elif id == 602 or id == 622:
            #ice-blue/white, fast, raindrops
            dark=.3
            speed=.1
            for i in range(5):
                pulse(color_dict['blue'],dark,speed)
                
    elif id == 701 or id == 711 or id == 721 or id == 741 or id == 771:
        #light-grey/grey, slow, wind
        dark=.7
        speed=.5
        for i in range(5):
            pulse(color_dict['grey'],dark,speed)
            
    elif id == 731 or id == 751 or id == 761 or id == 762:
        #dark-yellow/brown, regular, wind
        dark=.5
        speed=.3
        for i in range(5):
            pulse(color_dict['dark_orange'],dark,speed)
            
    elif main == "Tornado":
        #red fast rainbow-cycle
        dark=.3
        speed=.1
        for i in range(5):
            pulse(color_dict['red'],dark,speed)
        return "Join safely the nearest shelter as soon as possible"
    
    return f"Have a good night XP, {main}, {description}, {temperature} C"
    

if __name__ == "__main__":
    app.run(debug=True,port=80,host='0.0.0.0')
