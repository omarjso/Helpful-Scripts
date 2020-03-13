#!/usr/bin/env python3
import os
import time


def main():
	filename = input("Name of the watched file: ")
	command = input("Command to excute on file: ")

	lastMod = os.stat(filename).st_mtime
	while True:
		time.sleep(3)
		
		# Sometimes after saving a file the system needs time to recognize the
		# new file leading it to believe that it doesn't exist. This try, 
		# except catches that.
		try:
			newTime = os.stat(filename).st_mtime
			if newTime > lastMod:
				os.system(command)
				lastMod = newTime

		except FileNotFoundError:
			continue

if __name__ == "__main__":
	main()
