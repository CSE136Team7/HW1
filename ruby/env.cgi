#!/usr/bin/ruby

def printHTML()
	print "Content-Type: text/html;charset=utf-8\n\n"
	print "<!doctype html>\n<html lang='en'>\n<head>\n<title>HW1 in Ruby</title>\n</head>"
	print "<body style='" + randomBackground() + "'>\n"
	printGreeting()
	printEnvTable()
	print "</body>\n</html>"
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

def printEnvTable()
	server = ""
	client = ""
	filter = ["HTTP", "REQUEST", "QUERY"]
	for env in getSortedEnvVars() do
		varString = "<tr><td><b>" + env + "</b></td> <td>" + ENV[env] + "</td></tr>\n"
		if filter.any? { |e|  env.include? e}
			client << varString
	  else
			server << varString
		end
	end
	puts "<h2>Browser</h2>\n<table>"
	puts client
	puts "</table>"
	puts "<h2>Server</h2>\n<table>"
	puts server
	puts "</table>"''
end

def getSortedEnvVars()
	return ENV.keys.sort
end

printHTML()
