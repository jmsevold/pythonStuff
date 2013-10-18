def two_argument(*args) :
    arg1, arg2, = args
    print "arg1: %r, arg2: %r" %  (arg1, arg2)
    
    
    
def two_argument_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def one_argument(arg1):
    print "arg1: %r" % arg1
    
    
    
def no_argument():
    print "I got nothin'."
    
    
two_argument("zed", "shaw")
two_argument_again("zed", "shaw")
one_argument("First!")
no_argument()
    
    