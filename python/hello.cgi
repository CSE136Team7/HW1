#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import os
import time
from random import randint

def getSortedEnvVars():
	list = os.environ.keys()
	list.sort()
	return list

def printHTML():
	print "Content-Type: text/html;charset-utf-8"
	print "<!DOCTYPE html>\n\t<html lang='en'>\n\t<head>\n\t<title>HW1 in Python</title>\n</head>"
	print "<body style='{}'>\n".format(randomBackground())
	printGreeting()
	printEnvTable()
	print "</body>\n</html>"

def printEnvTable():
	server = ""
	client = ""
	for param in getSortedEnvVars():
		varString = "<tr><td><b>%s</b></td> <td>%s</td></tr>\n" % (param, os.environ[param])
		if any(x in param for x in ["HTTP","REQUEST","QUERY"]):
			client += varString
		else:
			server += varString
	print "<h2>Browser</h2>\n<table>"
	print client
	print "</table>"
	print "<h2>Server</h2>\n<table>"
	print server
	print "</table>"

def printGreeting():
	print "<h1>Hello World from Python @ {}</h1>".format(time.strftime("%d/%m/%Y"))

def randomBackground():
	num = randint(1,16)
	bgs = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
		 			"navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
	dark = [1,2,4,8,10]
	txtcolor = "white" if num - 1 in dark else "black"
	return "background-color: {}, color: {}".format(bgs[num - 1], txtcolor)


def main():
	cgitb.enable()
	printHTML()

if __name__ == "__main__":
	main()
