# -*- coding: utf-8 -*-
# James Taddei
# Dice Statistics
# 10/20/20

# Only works up to 2 as of now

def start():
    # Variable Input
    roll = raw_input("What would you like to roll (format: 2d8)? ")
    num = 0
    numOfDice = str()
    
    # Finds Number of Dice being Rolled
    while (roll[num] != "d"):
        numOfDice += roll[num]
        num += 1
    numOfDice = int(numOfDice)
    
    # Finds the Maximum Roll of a Die (its identifier number)
    dice = int(roll[num+1:len(roll)])
    
    # Selects Which Process to Take based on Number of Dice being Rolled
    if (numOfDice == 1):
        one_die(numOfDice, dice)
    elif (numOfDice == 0):
        print ("Error, number of dice can't be 0")
        start()
    elif (numOfDice > 0):
        multiple_dice(numOfDice, dice)
    
def one_die(numOfDice, dice):
    # Finds and Prints the Probability for Each Possible Roll
    for i in range(1, dice + 1):
        eachProb = (float(100)) / dice
        print("Probability of " + str(i) + ": " + str(eachProb) + "%")
    
    # Printsw the Probability for the Minimum and Maximum Roll
    print ("\nProbability of max (" + str(dice) + "): " + str(eachProb) + "%")
    print ("Probability of min (" + str(1) + "): " + str(eachProb) + "%")
    
    # Finds the Total of All Possible Results
    all_num = 0
    for a in range(1, dice + 1):
        all_num += a
    
    # Finds and Prints the Average Roll of one x (or dice) Sided Die
    average = float(all_num / dice)
    print ("The average roll is: " + str(average))
        
def multiple_dice(numOfDice, dice):
    # Finds Every Possible Outcome
    all_num = list()
    for i in range(1, dice + 1):
        all_num.append(i)
    all_num2 = all_num
    allAddedNum = list()
    for x in all_num:
        for y in all_num2:
            allAddedNum.append(x + y)
    
    # Find and Prints the Probability for each Outcomes
    zList = list()
    probList = list()
    for z in range(numOfDice, numOfDice * dice + 1):
        counter = float(allAddedNum.count(z))
        prob = ((counter / (dice * dice)) * 100)
        print("Probability of " + str(z) + ": " + str(prob) + "%")
        zList.append(z)
        probList.append(prob / 100)
        
    # Prints the Probability for the Minimum and Maximum Rolls
    print ("\nProbability of max (" + str(dice) + "): " + str(prob) + "%")
    print ("Probability of min (" + str(numOfDice) + "): " + str(prob) + "%")
    
    # Finds and Prints the Average Roll
    average = 0
    for a in range(1,len(zList)):
        average += zList[a] * probList[a]
    print ("The average roll is: " + str(average))

start()