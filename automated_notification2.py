##notificaton to alert user to plug charger when its less than 40%

from notifypy import Notify
import psutil
import math

switch_notification = False

##for continuously checking battery

while True:
    
    battery = psutil.sensors_battery()
    a = math.floor(battery.percent)
    notification = Notify()
    notification.title = f"Battery is below {a}%"
    notification.message = "Charging pe lagade bhai"

    if battery.power_plugged == False:
        switch_notification==False

        
    if a<=40 and battery.power_plugged == False and switch_notification==False:
        
        notification.send()
        switch_notification = True
