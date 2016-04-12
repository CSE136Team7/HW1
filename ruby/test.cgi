#!/usr/bin/ruby

puts "Content-type: text/html\n\n"

a = ENV['QUERY_STRING']

puts a

res= a.split('&')
username = res[0].split('=')[1]
password = res[1].split('=')[1]
magicnum = res[2].split('=')[1]

for i in 0..magicnum
  puts " <h1> Hello " + username + " with the password of " + password + "</h1>"
end
