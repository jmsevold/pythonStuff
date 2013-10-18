
#words, a var, splits the argument by spaces
# then returns that value to whatever var you later determine
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#alphabetically sorts and returns to a var
def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

#words, a variable holding the value of a previous defined
#function, break_words, is then put into previously defined function
#sort_words, and returned to a var. Break the words, sort them 
#alphabetically, and return value to a variable
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

#words, a variable holding the value of a previous defined
#function, which breaks the words of an arg, is then placed
#in two more functions, which print the first and last words respectively
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
#words, a variable holding the value of a previously defined
# function, which sorts the argument after having broken it, is placed
#in two functions which print the first and last words of the alphabetically
#sorted argument
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)