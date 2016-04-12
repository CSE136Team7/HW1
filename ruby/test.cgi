#!/usr/bin/ruby

puts "Content-type: text/html\n\n"

a = ENV['QUERY_STRING']


res= a.split('&')
username = res[0].split('=')[1]
password = res[1].split('=')[1]
magicnum = res[2].split('=')[1]

def printHTML(string, magicnum)
	puts "<!doctype html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'><title>HW1 in Python</title>\n</head>"
	puts "<body >\n"
	for i in 0..magicnum
    puts string
  end
	puts "</body>\n</html>"
end

printHTML("<h1> Hello " + username + " with the password of " + password + "</h1>", magicnum)

