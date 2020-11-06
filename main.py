#!/usr/bin/python3

import platform

# Processor name
def callPlatformName():
	print(platform.processor())

# Platform system
def callPlatformSystem():
	print(platform.system())
	
# Platform Linux uname
def callPlatformUname():
	print(platform.uname())

# Platform machine arch
def callPlatformMachine():
	print(platform.machine())

def main():
	callPlatformName()
	callPlatformSystem()
	callPlatformUname()
	callPlatformMachine()

if __name__ == "__main__":
	main()
