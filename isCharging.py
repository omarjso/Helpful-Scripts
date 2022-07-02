#!/usr/local/bin/python3
import psutil
import time
SECS_THRESH = 5

def notify(notif_type):
    if notif_type == "print":
        print("Laptop is Charging")

def main():
    counter = 0
    while True:
        time.sleep(1)
        if psutil.sensors_battery().power_plugged:
            counter += 1
        else:
            conter = 0

        if counter == SECS_THRESH:
            notify("print")
            break

if __name__ == "__main__":
    main()
