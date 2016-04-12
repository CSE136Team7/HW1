#!/usr/bin/ruby

def printHTML()
	print "Content-Type: text/html;charset=utf-8\n\n"
	print "<!doctype html>\n<html lang='en'>\n<head>\n<title>HW1 in Ruby</title>\n</head>"
	print "<body >\n"
	printEnvTable()
	print "</body>\n</html>"
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
