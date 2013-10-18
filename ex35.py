from sys import exit
#gold_room function will...
    # print... will first print a question
    # next...variable 'next' will hold the value of raw_input
    #if... there is a 0 or 1 in the user's input,
    # int(next) converts the user's input to an integer and
        #how_much... holds the value of that integer
    #if how_much 
    

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
#bear_room does...
    #prints 4 strings
    #sets variable bear_moved to False
    #While True = loop forever until broken
    #bear_moved is a variable set to False
    
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    #if "taunt_bear" and not False,
       set bear_moved to True
    #if "taunt bear" and bear_moved = True (we have redefined it as true
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

#function cthulhu_room will...
    #print 3 strings
    #prompt user for input and hold in variable 'next'
    # if "flee" in user's input 'next', run function start()
    #which takes us back to the beginning
    #if 'head' is in user's input, run dead function
    #any other response will continue to run the function
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

#function dead() will..
    #print 'why', the argument passed to it(which, if you
    #look at the other function is usually a means of 
    #death, and string 'good job!'
    #exit the script
def dead(why):
    print why, "Good job!"
    exit(0)

#function start is ran. It...
    #prints three strings
    # prompts user, and holds value in variable 'next'
    # if next, the user's input, is equivalent to 'left', 
    #run bear_room function
    #if it is equivalent to 'right', run cthulhu_room() function
    # Else, all other user input will run the function dead()
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
         cthulhu_room()
    else:
        dead("You stumbled around the room until you starve.")
        
start()