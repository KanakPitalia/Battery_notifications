## notificaton to alert user to unplug charger when its greater than 80%

from notifypy import Notify
import psutil
import math

switch_notification = False

##for continuously checking battery

while True:

   
   battery = psutil.sensors_battery()
   a = math.ceil(battery.percent)
   notification = Notify()
   notification.title = f"Battery is above {a}%"
   notification.message = "Charging band krde bhai"

   if battery.power_plugged == False:
      switch_notification==False

       
   if a>=80 and battery.power_plugged == True and switch_notification==False:
       
      notification.send()
      switch_notification = True
