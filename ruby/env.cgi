#!/usr/bin/ruby

puts "Content-type: text/html\n\n"
puts "<!doctype html>"
puts "<head>"
puts "<meta charset='UTF-8'>
puts "</head>"
puts "<body>"

puts "<h1>Hello World from Ruby @ " + Time.new.inspect + "</h1>"
puts "<hr>"

envTables()

puts "</body></html>"

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

