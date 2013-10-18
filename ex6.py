# d represents a number. x is a variable.
x = "There are %d types of people." % 10
# we are defining in order, the following two formatters which will take %s form
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# %r takes the place of the sentence that x represents
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 