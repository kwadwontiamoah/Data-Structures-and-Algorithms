import random


def sentence_generator():
    theString = "methinks it is like a weasel"
    options = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    options = options.split()
    options.append(' ')
    random_string = [random.choice(options) for i in range(len(theString))]
    return random_string

def sentence_scorer(sentence):
    """
    takes as input a sentence from sentence_generator
    and then evaluates how close to "methinks it is like a weasel"
    it is.
    The high score is 28/28 characters being a match!
    """
    score = 0
    theString = "methinks it is like a weasel"

    #turns every single charcter from theString into an element of a list
    theString2 = list(theString) 
    for i in range(len(theString)):
        if sentence[i] == theString2[i]:
            score += 1
    return score

def generator():
    high_score = 0
    while high_score != 28:
        x = sentence_generator()
        y = sentence_scorer(x)
        if high_score < y:
            high_score = y
            print ("The new high score is %d" % (high_score))
            print ("The string is " + ''.join(x))
    print ("Done!")
