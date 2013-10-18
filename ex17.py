from sys import argv
from os.path import exists

script, oldfile, newfile = argv

print "Copying from %s to %s" % (oldfile, newfile)

# we could do these two on one line too, how?
in_file = open(oldfile)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(newfile)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(newfile, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()