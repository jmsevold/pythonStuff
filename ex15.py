print "Let's first select a file for python to open"

file = raw_input("> ")

print "Here is your file, %r: " % file

read_file = open(file)

print read_file.read()

print "and again"

print open(from_file).read()

