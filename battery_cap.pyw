import psutil
import time
from win10toast import ToastNotifier

last_power = 0
while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged and last_power >= 95 and percent >= 95:
        toaster = ToastNotifier()
        toaster.show_toast("Battery 95%",
                   "Disacharge laptop",
                   duration=10,
                   icon_path="C:\\Users\\Walter\\Desktop\\Všechno\\battery.ico")
        break

    last_power = percent
    time.sleep(1200)
