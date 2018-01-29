import random

def funkymonkey():
    alpha= list(' abcdefghijklmnopqrstuvwxyz ')
    for i in range (len(alpha)): #Range is given as 28 characters
        randAZ= random.shuffle(alpha)# the shuffle method is used to randomize the string
        newAZ= ' '.join(alpha) #join method is used to concatenate the resulting string
        return newAZ
 

def comparemonkeys(sentence):
    word1= str(sentence) #turn the input into a string
    word= list(word1)#list is used to separate each character in the string into a list
    score = 0 #initiate counter
    target = "methinks it is like a weasel"
    string2 = list(target) 
    for i in range(len(list(target))): #compares both strings using indexing
        if word[i] == string2[i]:
            score += 1
    return score
##    percentage= (score//28)*100
##    return percentage

    
def shakespeare():
    hiscore = 0;
    counter= 0
    thousand_tracker = 1000 #let the function run a 1000x
    highscore_word = ""
    while counter != thousand_tracker:
        x = funkymonkey() #to call function1
        y = comparemonkeys(x)#call function2 with input from function1
        if  hiscore < y: 
            hiscore = y
            highscore_word = x
        counter = counter + 1
    print("New high score is %d" % (hiscore))
    print("The string is " + ''.join(highscore_word))
        
    print ("Done!")
##    shakespeare()
