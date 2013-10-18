#first we define and name the function
#it will take the values of the variables within the ()
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "you have %d cheeses!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "get a blanket. \n"

# 20 takes the place of cheese_count, 30 the same for boxes_of_crackers
#It will not run all tabbed statements seen above 
print "we can just give the function numbers directly:"
cheese_and_crackers (20,30)

#we give the variables a value, then call the variables in the parameters
#of the function
print "or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#uses the values of 10 and 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#referring to the function now, and not the variables above
print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#above we defined the variables, here we don't so it takes the last defined values
#of 10 and 50 plus the number's we've added
print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)