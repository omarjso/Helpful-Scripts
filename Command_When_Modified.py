#!/usr/bin/env python3
import subprocess
import os
import time
import sys
import signal
FILE_SHORTHAND = "$F"
SECONDS_THRESH = 0.5

def handler(*_): 
    exit(print("\nstopped watching the file"))

signal.signal(signal.SIGINT, handler)

def main(filename):
    if filename == "":
        filename = input("Name of the watched file: ")
    command = input("Command to excute on file: ")
    command = command.replace(FILE_SHORTHAND, filename)
    command = command.split()

    lastMod = os.stat(filename).st_mtime
    while True:
        time.sleep(SECONDS_THRESH)
        # Sometimes after saving a file the system needs time to
        # recognize the new file leading it to believe that it doesn't
        # exist. This try, except catches that.
        try: 
            newTime = os.stat(filename).st_mtime 
            if newTime - lastMod > SECONDS_THRESH:
                p = subprocess.run(command)
                lastMod = newTime

        except FileNotFoundError:
            continue

if __name__ == "__main__":
    main(sys.argv[1])
