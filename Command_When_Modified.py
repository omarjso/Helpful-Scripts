#!/usr/bin/env python3
import subprocess
import os
import time
import sys
import signal


def handler(*_): 
    exit(print("\nstopped watching the file"))

signal.signal(signal.SIGINT, handler)

def main(filename):
    if filename == "":
        filename = input("Name of the watched file: ")
    command = input("Command to excute on file: ")

    lastMod = os.stat(filename).st_mtime
    while True:
        # Sometimes after saving a file the system needs time to
        # recognize the new file leading it to believe that it doesn't
        # exist. This try, except catches that.
        try: 
            newTime = os.stat(filename).st_mtime 
            if newTime - lastMod > 0.1:
                p = subprocess.run(command.split())
                lastMod = newTime

        except FileNotFoundError:
            continue

if __name__ == "__main__":
    main(sys.argv[1])
