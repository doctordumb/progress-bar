#!/usr/bin/python3

import sys
import time
import argparse

color_dict = {"red": "\033[91m",
		"green": "\033[92m",
		"yellow": "\033[93m",
		"na": ""
		}

reset_color = "\033[0m"
reset_cursor = "\033[1000D"

parser = argparse.ArgumentParser(description="Custom loading bar.",
				formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-b", "--bar", metavar="", action="store", type=int, default=50, help="desired length of bar")
parser.add_argument("-e", "--elements", metavar="", action="store", type=int, default=100, help="number of elements")
parser.add_argument("-c", "--color", metavar="", action="store", default="na", help="Color of bar (red, yellow, green")
parser.add_argument("-s", "--symbol", metavar="", action="store", default="#", help="Symbol to use in a bar")

args = parser.parse_args()
bar_length = args.bar
num = args.elements
color = args.color
symbol = args.symbol

bar_color = color_dict[color]

for x in range(num):
	time.sleep(0.1)
	width = int((x+1)/(num/bar_length))
	bar = "[" + bar_color + symbol * width + " " * (bar_length - width) + reset_color + "]"
	sys.stdout.write(reset_cursor + bar)
	sys.stdout.flush()
print("")
