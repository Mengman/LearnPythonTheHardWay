from sys import argv #import modules sys

script, filename = argv #set user input to variable

txt = open(filename) #open file

print "Here's your file %r: " % filename
print txt.read()  #print file content

txt.close()


print "I'll also ask you to type it again: "
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
