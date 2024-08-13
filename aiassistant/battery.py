import psutil #we can use the psutil library, which provides an easy way to retrieve system and process information

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        is_plugged = battery.power_plugged
        if is_plugged:
            return f"{percent}% and plugged in"
        else:
            return f"{percent}% and running on battery"
    else:
        return "Battery information not available"