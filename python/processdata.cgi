#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb, cgi

def main():
        cgitb.enable()
        print ("Content-Type: text/html;charset=utf-8")
        print ("")
        form = cgi.FieldStorage()
        try:
                username = validateString(form.getvalue('username'))
                password = validateString(form.getvalue('password'))
                magicnum1 = validateInt(form.getvalue('magicnum'))
        except ValueError:
                printHTML("<p>There was an error with your input</p>")
        else:
                s = "<h1>Hello {} with a password of {}</h1></br>".format(username,password)
                s = s * magicnum1
                printHTML(s)

def printHTML(string):
	print "<!doctype html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'><title>HW1 in Python</title>\n</head>"
	print "<body >\n"
	print string
	print "</body>\n</html>"

def validateString(string):
        if not string:
            raise ValueError
        return str(string)
def validateInt(string):
        m = 0
        m = int(string)
        if (m < 1):
            raise ValueError
        return m
if __name__ == "__main__":
        main()
