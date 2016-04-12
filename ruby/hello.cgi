#!/usr/bin/ruby

puts("Content-type: text/html \n\n");
def randomBackground()
	num = rand(1...16)
	bgs = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
		 			"navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
	dark = [1,2,4,8,10]
	txtcolor = (dark.include? num - 1) ? "white" : "black"
	return "background-color: " + bgs[num - 1] + "; color: " + txtcolor + ";"
end
puts("<!DOCTYPE html>");
puts("<html lang='en'>");
puts("<head>");
puts("<title>HW1 in Ruby</title>");
puts("</head><body style='" + randomBackground() + "'>");
puts("<h1>Hello World from Ruby @ 2016-04-12 00:35:24 -0700</h1>");
puts("</body>");
puts("</html>");
