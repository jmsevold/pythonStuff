from sys import argv

#when these are typed here, they will assume the arguments typed in Terminal
script, input_file = argv

#when called, this function will read the value of f
def print_all(f):
    print f.read()

#function named rewind that rewinds file to 0th byte
def rewind(f):
    f.seek(0)

#this function takes the two values inside () and prints line_count and readline
def print_a_line(line_count, f):
    print line_count, f.readline()

#variable that opens value of input_file(from argv)
current_file = open(input_file)

print "First let's print the whole file:\n"

#print_all, a previously defined function that does f.read().open(input_file)
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#previously defined function that opens input file, and rewinds it
rewind(current_file)

print "Let's print three lines:"

#call upon previously defined function which prints value of
#'current line' and also opens input_file and then reads one line at a time
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)