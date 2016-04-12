#!/usr/bin/ruby
def printHTML()
	puts "Content-Type: text/html;charset=utf-8\n\n"
	puts "<!doctype html>\n<html lang='en'>\n<head>\n<title>HW1 in Ruby</title>\n</head>"
	puts "<body style='" + randomBackground() + "'>\n"
	printGreeting()
	puts "</body>\n</html>"
end

def printGreeting()
  puts "<h1>Hello World from Ruby @ " + Time.new.inspect + "</h1>"
end

def randomBackground()
	num = rand(1...16)
	bgs = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
		 			"navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
	dark = [1,2,4,8,10]
	txtcolor = (dark.include? num - 1) ? "white" : "black"
	return "background-color: " + bgs[num - 1] + "; color: " + txtcolor + ";"
end
