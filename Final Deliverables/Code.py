import wiotp.sdk.device
import time
import random
import ibmiotf.application
import ibmiotf.device
import requests, json

myConfig = { 
    "identity": {
        "orgId": "e4jrbo",
        "typeId": "SignsWithSmartConnectivity",
        "deviceId":"12345"
    },
    "auth": {
        "token": "1234567890"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

 
#OpenWeatherMap Credentials

URL = "http://api.openweathermap.org/data/2.5/weather?q=Kāraikkudi,IN&units=metric&appid=76e08ef85f6173baed5302d8d21a6d24"


while True:
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        vis = (data['visibility'])/1000
        place=data['name']
        wea= data['weather'][0]['main']

        vis_ms=""
        if vis>=10:
            vis_ms+="Road is visible"
        else:
            vis_ms+="Visiblity is Low, Drive safely"

        msg=random.randint(0,5)
        if msg==1:
            message="GO SLOW, SCHOOL ZONE AHEAD"
        elif msg==2:
            message="NEED HELP, POLICE STATION AHEAD"
        elif msg==3:
            message="EMERGENCY, HOSPITAL NEARBY"
        elif msg==4:
            message="DINE IN, RESTAURENT AVAILABLE"
        elif msg==5:
            message="PETROL BUNK NEARBY"
        else:
            message=""
            
        speed=random.randint(0,150)
        if speed>=100:
            speedMsg="Speed Limit Exceeded"
        elif speed>=60 and speed<100:
            speedMsg="Moderate Speed"
        else:
            speedMsg="Slow and steady"


        if temperature < 24:
            visibility="cold weather, Drive Slow"
        elif temperature < 20:
            visibility="Bad Weather, Be Careful"
        else:
            visibility="Clear Weather, Safe Journey"


        sign=random.randint(0,6)
        if sign==1:
            signMsg="Right Diversion"
        elif sign==2:
            signMsg="Speed Breaker"
        elif sign==3:
            signMsg="Left Diversion"
        elif sign==4:
            signmsg="U Turn"
        elif sign==5:
            signMsg="Under Repair"
        else:
            signMsg=""
        
        
        myData={'Temperature':temperature,'Visibility':vis, 'temp-msg':visibility, 'Sign_msg':signMsg, 'Vis_msg':vis_ms, 'LM_msg':message, 'Speed_msg':speedMsg, 'Humidity':humidity, 'Place':place, 'Weather':wea}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully:", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
client.disconnect()

