import time
import random
while True:
    temparature = random.randint(1,1500)
    humidity = random.randint(1,200)
    print("Current temparature:",temparature)
    print("Current Humidity:",humidity)
    if(temparature > 70 and humidity < 50):
        print("Alarm Rings")
        time.sleep(2)
    else:
        print("normal state")
        time.sleep(2)
    
