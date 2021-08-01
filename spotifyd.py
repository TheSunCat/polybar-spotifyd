#!/usr/bin/env python3
import os
import sys

if len(sys.argv) == 1:
	stream = os.popen("playerctl metadata")
	output = stream.read()

	for line in output.split("\n"):
		if "spotifyd xesam:title" in line:
			title = line[20:].strip()
		
		if "spotifyd xesam:artist" in line:
			artist = line[21:].strip()

	if not title or not artist:
		print("⏵ Could not fetch title or artist!")
	else:
		print("⏵ " + title + " - " + artist)
else:
	arg = sys.argv[1]
	
	if arg == "toggleplay":
		
		# toggle
		stream = os.popen("playerctl status")
		output = stream.read()
		
		if "Playing" in output:
			os.popen("playerctl pause")
		else: # Paused
			os.popen("playerctl play")
	elif arg == "previous":
		os.popen("playerctl previous")
	elif arg == "next":
		os.popen("playerctl next")
	else:
		print("Unknown argument! Valid args are: toggleplay, previous, next")
