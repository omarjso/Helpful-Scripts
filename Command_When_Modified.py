#!/usr/bin/env python3
import subprocess
import os
import time
import sys
import signal
FILE_SHORTHAND = "$F"
SECONDS_THRESH = 0.5
TIMEOUT = 3600

def handler(*_): 
    exit(print("\nstopped watching the file"))

signal.signal(signal.SIGINT, handler)

def main(filename):
    if filename == "":
        filename = input("Name of the watched file: ")
    command = input("Command to excute on file (Tip: $F as filename): ")
    if FILE_SHORTHAND in filename:
        command = command.replace(FILE_SHORTHAND, filename)
    command = command.split()

    lastMod = os.stat(filename).st_mtime
    lastCheck = time.time()

    while True:
        time.sleep(SECONDS_THRESH)
        currentTime = time.time()
        if currentTime - lastCheck > TIMEOUT:
            print("No updates for an hour. Exiting.")
            break
        # Sometimes after saving a file the system needs time to
        # recognize the new file leading it to believe that it doesn't
        # exist. This try, except catches that.
        try: 
            newTime = os.stat(filename).st_mtime 
            if newTime - lastMod > SECONDS_THRESH:
                p = subprocess.run(command)
                lastMod = newTime
                lastCheck = time.time()

        except FileNotFoundError:
            continue

if __name__ == "__main__":
    main(sys.argv[1])
