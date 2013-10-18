#Function defined to do the following:
# set y as a variable that holds the user input, prompted by
#a question where %s is a formatter for x, whatever is entered for ()
#when the user calls the function
# returns the value to the variable
def collect_info(x):
    y =raw_input('what is your %s\'s name?' % x)
    return y

#animal is a variable that holds a questions
animal = raw_input("What kind of animal?")

#this is a variable that holds value that the function
#'collect_info' returns to it. Animal is substituted for X
pet_name = collect_info(animal)

print "your %s is named %s." % (animal, pet_name)