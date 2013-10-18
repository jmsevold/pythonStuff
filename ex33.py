#i set to zero. create an empty list  'numbers'
i = 0
numbers = []

#as long as i, which is currently 0, is less than 6, run
# the printed statement with i, and append it to the empty list

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

#run printed statement, at this point, the list only has zero
#but now, the second printed statement has i, and we said
# to add i (0) to 1, making i now 1, in said statement
#at the bottom i is the new value of i- 1
#This 1, is then looped back, and since it's less than 6, the function
#continues
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    

print "The numbers: "

for num in numbers:
	print num