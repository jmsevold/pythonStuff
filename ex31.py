print "You enter a dark room with three doors. do you go through door  #1,#2, or #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your face off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulus retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. good job!"
        
else:
    print "You stumble and fall on a knife. great job!"
    
if door == "3":
	print "1. You see a massive pot of gold."
	print "2. Stuff as much gold into your pockets."
	print "3. Refrain. This isn't your gold."
	
	decision = raw_input("> ")
	
	if decision == "2":
	    print "A leprachaun appears and blasts you back with a shotgun."
	elif decision == "3":
	    print "God rewards you for your humility with everlasting life."
	
	
    
