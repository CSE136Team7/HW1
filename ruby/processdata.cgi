#!/usr/bin/ruby
require 'cgi'
cgi = CGI.new
res = cgi.params
puts "Content-type: text/html\n\n"

a = ENV['QUERY_STRING']


username = cgi['username']
password = cgi['password']
magicnum = cgi['magicnum'].to_i

def printHTML(string)
	puts "<!doctype html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'><title>HW1 in Ruby</title>\n</head>"
	puts "<body >\n"
	puts string
	puts "</body>\n</html>"
end

text1 = "<h1> Hello " + username + " with the password of " + password + "</h1>\n"
res = ""
for i in 0...magicnum do
	res << text1
end

printHTML(res)
