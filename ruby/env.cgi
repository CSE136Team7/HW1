#!/usr/bin/ruby

puts "Content-type: text/html\n\n"

puts "<h1>Hello World from Ruby @ " + Time.new.inspect + "</h1>"

puts "<html> <h1> Enviroment Variables</h1> </html>"

puts "<form> <br><b>CONTEXT_DOCUMENT_ROOT:</b>"
puts ENV['CONTEXT_DOCUMENT_ROOT']
puts "<form> <br> <b>CONTEXT_PREFIX: </b>"
puts ENV['CONTEXT_PREFIX']
puts "<form> <br> <b>DOCUMENT_ROOT: </b>"
puts ENV['DOCUMENT_ROOT']
puts " <form> <br> <b> GATEWAY_INTERFACE: </b> "
puts ENV['GATEWAY_INTERFACE']
puts " <form> <br> <b> HTTP_ACCEPT: </b> "
puts ENV['HTTP_ACCEPT']
puts " <form> <br> <b> HTTP_ACCEPT_ENCODING: </b> "
puts ENV['HTTP_ACCEPT_ENCODING']
puts " <form> <br> <b> HTTP_ACCEPT_LANGUAGE: </b> "
puts ENV['HTTP_ACCEPT_LANGUAGE']
puts " <form> <br> <b> HTTP_CONNECTION: </b> "
puts ENV['HTTP_CONNECTION']
puts " <form> <br> <b> HTTP_HOST: </b> "
puts ENV['HTTP_HOST']
puts " <form> <br> <b> HTTP_REFERER: </b> "
puts ENV['HTTP_REFERER']
puts " <form> <br> <b> HTTP_UPGRADE_INSECURE_REQUESTS: </b> "
puts ENV['HTTP_UPGRADE_INSECURE_REQUESTS']
puts " <form> <br> <b> HTTP_USER_AGENT: </b> "
puts ENV['HTTP_USER_AGENT']
puts " <form> <br> <b> PATH: </b> "
puts ENV['PATH']
puts " <form> <br> <b> QUERY_STRING: </b> "
puts ENV['QUERY_STRING']
puts " <form> <br> <b> REMOTE_ADDR: </b> "
puts ENV['REMOTE_ADDR']
puts " <form> <br> <b> REMOTE_PORT: </b> "
puts ENV['REMOTE_PORT']
puts " <form> <br> <b> REQUEST_METHOD: </b> "
puts ENV['REQUEST_METHOD']
puts " <form> <br> <b> REQUEST_SCHEME: </b> "
puts ENV['REQUEST_SCHEME']
puts " <form> <br> <b> REQUEST_URI: </b> "
puts ENV['REQUEST_URI']
puts " <form> <br> <b> SCRIPT_FILENAME: </b> "
puts ENV['SCRIPT_FILENAME']
puts " <form> <br> <b> SCRIPT_NAME: </b> "
puts ENV['SCRIPT_NAME']
puts " <form> <br> <b> SERVER_ADMIN: </b> "
puts ENV['SERVER_ADMIN']
puts " <form> <br> <b> SERVER_NAME: </b> "
puts ENV['SERVER_NAME']
puts " <form> <br> <b> SERVER_PORT: </b> "
puts ENV['SERVER_PORT']
puts " <form> <br> <b> SERVER_PROTOCOL: </b> "
puts ENV['SERVER_PROTOCOL']
puts " <form> <br> <b> SERVER_SIGNATURE: </b> "
puts ENV['SERVER_SIGNATURE']
puts " <form> <br> <b> SERVER_SOFTWARE: </b> "
puts ENV['SERVER_SOFTWARE']
