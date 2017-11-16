#!/usr/bin/env python3
import sys
def Hours(minutes):
	try:
		hour = 0
		minu = 0	
		if(minutes >= 0):
			while(minutes >= 60):
				minutes -= 60
				hour+=1
			minu = minutes
		else:
			raise ValueError("A value error")
		print("{} H, {} M".format(hour,minu))
	except	ValueError:
		print("ValueError:Inpute number cannot be negative")

if __name__ == "__main__":
	Hours(int(sys.argv[1]))
