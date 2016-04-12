#!/usr/bin/python
print "Content-type: text/html \n\n"

def printHTML():
	print "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<title>HW1 in Python</title>\n</head>"
	print "<body style='{}'>\n".format(randomBackground())
	printGreeting()
	print "</body>\n</html>"
  
def printGreeting():
	print "<h1>Hello World from Python @ {}</h1>".format(time.strftime("%d/%m/%Y"))

def randomBackground():
	num = randint(1,16)
	bgs = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
		 			"navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
	dark = [1,2,4,8,10]
	txtcolor = "white" if num - 1 in dark else "black"
	return "background-color: {}; color: {}".format(bgs[num - 1], txtcolor)
