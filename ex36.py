from sys import argv 

script, user_name = argv

def start():
    print "Hello %s, would you like to play a game of life and death?" % user_name
    answer = raw_input("> ")

    if "yes" in answer:
        dark_alley()
    elif "no" in answer:
        exit(0)
    else:
        print "Please choose 'yes' or 'no'."
        start()
        
    


def dark_alley():
    print "You walk down a dark alley."
    print "A thug appears before you."
    print "'Gimme your fuckin' wallet!', he says, wielding a knife."
    print "You realize you have two options: Obey, or fight back."
    print "What do you do?"
    
    choice = raw_input(">  ")
    
    if "obey" in choice:
        survived("'Thanks bitch.' He runs down the alley and disappears.") 
    elif "fight" in choice:
        print "Do disarm the knife?"
        print  "Or kick him in the balls?"
        
        choice = raw_input("> ")
        if "disarm" in choice:
            disarm_knife()
        elif "kick" in choice:
            kick_balls()
        else:
            print "You must choose. Try again."
            dark_alley()
    else:
        print "You must choose. Try again."
        dark_alley
        

def disarm_knife():
    print "You grab ahold of his arm with both hands. "
    print "You are matched in strength. Two options flash in your mind: "
    print "Stomp his shin with all your weight, or turn rotate your body"
    print "and throw him against the wall. What do you do?"
    
    choice =raw_input("> ")
     
    if "stomp" in choice:
        print "You stomp his shin with all your weight."
        print "You feel his leg crack. He screams in pain. Realizing you might"
        print "be arrested, you turn and flee, your adrenaline racing."
        survived("You have defeated your enemy and survived")
    
    elif "turn" or "body" in choice:
        print "You turn and throw him. He slams against the wall, dazed."
        print "You spot the knife. Do you pick it up, or turn and run?"
        choice = raw_input("> ")
        
        if "pick" in choice:
            survived("You pick up the knife, and brutally stab him over 50 times.")
        elif "run" in choice:
            survived("You sprint and don't look back. You survived.")
        else:
            dead("Learn to answer correctly, jerk.")
    else:
        dead("You failed to act. He stabs you to death.")



def kick_balls():
    print "You kick him in the balls, but as you do so he stabs the knife"
    print "into your leg. You fall down, and he proceeds to kill you"
    dead("Better luck next time.")
        


def dead(why):
    print why, "Game Over."
    exit(0)
    
def survived(why):
   print why, "Game Over."
   exit(0)

start()