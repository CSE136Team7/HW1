#!/usr/bin/ruby

puts "Content-type: text/html\n\n"
puts "<!doctype html>"
puts "<head>"
puts "<meta charset='UTF-8'>"
puts "</head>"
puts "<body>"

# puts "<html> <h1> Enviroment Variables</h1> </html>"
#
# puts "<form> <br><b>CONTEXT_DOCUMENT_ROOT:</b>"
# puts ENV['CONTEXT_DOCUMENT_ROOT']
# puts "<form> <br> <b>CONTEXT_PREFIX: </b>"
# puts ENV['CONTEXT_PREFIX']
# puts "<form> <br> <b>DOCUMENT_ROOT: </b>"
# puts ENV['DOCUMENT_ROOT']
# puts " <form> <br> <b> GATEWAY_INTERFACE: </b> "
# puts ENV['GATEWAY_INTERFACE']
# puts " <form> <br> <b> HTTP_ACCEPT: </b> "
# puts ENV['HTTP_ACCEPT']
# puts " <form> <br> <b> HTTP_ACCEPT_ENCODING: </b> "
# puts ENV['HTTP_ACCEPT_ENCODING']
# puts " <form> <br> <b> HTTP_ACCEPT_LANGUAGE: </b> "
# puts ENV['HTTP_ACCEPT_LANGUAGE']
# puts " <form> <br> <b> HTTP_CONNECTION: </b> "
# puts ENV['HTTP_CONNECTION']
# puts " <form> <br> <b> HTTP_HOST: </b> "
# puts ENV['HTTP_HOST']
# puts " <form> <br> <b> HTTP_REFERER: </b> "
# puts ENV['HTTP_REFERER']
# puts " <form> <br> <b> HTTP_UPGRADE_INSECURE_REQUESTS: </b> "
# puts ENV['HTTP_UPGRADE_INSECURE_REQUESTS']
# puts " <form> <br> <b> HTTP_USER_AGENT: </b> "
# puts ENV['HTTP_USER_AGENT']
# puts " <form> <br> <b> PATH: </b> "
# puts ENV['PATH']
# puts " <form> <br> <b> QUERY_STRING: </b> "
# puts ENV['QUERY_STRING']
# puts " <form> <br> <b> REMOTE_ADDR: </b> "
# puts ENV['REMOTE_ADDR']
# puts " <form> <br> <b> REMOTE_PORT: </b> "
# puts ENV['REMOTE_PORT']
# puts " <form> <br> <b> REQUEST_METHOD: </b> "
# puts ENV['REQUEST_METHOD']
# puts " <form> <br> <b> REQUEST_SCHEME: </b> "
# puts ENV['REQUEST_SCHEME']
# puts " <form> <br> <b> REQUEST_URI: </b> "
# puts ENV['REQUEST_URI']
# puts " <form> <br> <b> SCRIPT_FILENAME: </b> "
# puts ENV['SCRIPT_FILENAME']
# puts " <form> <br> <b> SCRIPT_NAME: </b> "
# puts ENV['SCRIPT_NAME']
# puts " <form> <br> <b> SERVER_ADMIN: </b> "
# puts ENV['SERVER_ADMIN']
# puts " <form> <br> <b> SERVER_NAME: </b> "
# puts ENV['SERVER_NAME']
# puts " <form> <br> <b> SERVER_PORT: </b> "
# puts ENV['SERVER_PORT']
# puts " <form> <br> <b> SERVER_PROTOCOL: </b> "
# puts ENV['SERVER_PROTOCOL']
# puts " <form> <br> <b> SERVER_SIGNATURE: </b> "
# puts ENV['SERVER_SIGNATURE']
# puts " <form> <br> <b> SERVER_SOFTWARE: </b> "
# puts ENV['SERVER_SOFTWARE']

def printHTML()
	print "Content-Type: text/html;charset=utf-8\n\n"
	print "<!doctype html>\n<html lang='en'>\n<head>\n<title>HW1 in Ruby</title>\n</head>"
	print "<body style='" + randomBackground() + "'>\n"
	printGreeting()
	envTables()
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

printHTML()

def envTables()
    puts "<h1>Environment Variables</h1>"
    ENV.sort
    browser = []
    server = []
    bindex = 0
    sindex = 0
    for e in ENV
        if e.include? 'HTTP' || e.include? 'REQUEST' || e.include? 'REMOTE' || e.include? 'QUERY' || e.include? 'I'
            browser[bindex] = e
            bindex = bindex + 1
        else
            server[sindex] = e
            sindex = sindex + 1
        end
    end
    puts "<h1>Browser</h1>"
    puts "<table>"
    for bi in 0..bindex
        puts "<tr><td><strong>"
        puts browser[bi]
        puts ":</strong></td><td>"
        puts ENV[browser[bi]]
        puts "</td><tr>"
    end
    puts "</table>"
    puts "<h1>Server</h1>"
    puts "<table>"
    for si in 0..sindex
        puts "<tr><td><strong>"
        puts server[si]
        puts ":</strong></td><td>"
        puts ENV[server[si]]
        puts "</td></tr>"
    end
    puts "</table>"
end
