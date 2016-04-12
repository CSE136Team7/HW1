#!/usr/bin/ruby

puts "Content-type: text/html\n\n"

a = ENV['QUERY_STRING']

puts a

res= a.split('&')
username = res[0].split('=')[1]
password = res[1].split('=')[1]
magicnum = res[2].split('=')[1]

puts username
puts password
puts magicnum

puts "Hello " + username + " with the password of " + password

