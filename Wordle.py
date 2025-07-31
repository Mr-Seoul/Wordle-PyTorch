import random

words = []
def readWords():
    global words
    #Read Words
    with open("words.txt",'r') as f:
        words = [line.strip() for line in f]
        words = words[245:len(words)]

def feedBack(guess,target):
    #Construct feedback
    response = ""
    for charIndex in range(0,len(guess)):
        if guess[charIndex] == target[charIndex]:
            response += "G"
        elif guess[charIndex] in target:
            response += "Y"
        else:
            response += "N"
    return response


def game():
    global words
    #Get random word
    target = words[random.randint(0,len(words)-1)]

    #Function to define valid guesses
    def valid(str):
        if str not in words:
            return False
        else:
            return True
    
    #Start with n user guesses.
    n = 5
    for i in range(0,n):
        #Get user guess
        guess = ""
        while not valid(guess):
            guess = input("Write your guess: ")
            if not valid(guess):
                print("Invalid guess")
        
        response = feedBack(guess,target)
        
        #If correct, return the winning signal. Otherwise, give feedback
        if response == "GGGGG":
            return "You Win!"
        print(response)
    #If all guesses are wrong, return the losing signal
    return "You Lose!"

def generateData(n,targetDir):

    def deconstructArr(target,guesses):
        deconstructedData = [target]
        for wordPair in guesses:
            deconstructedData.append(wordPair[0])
            deconstructedData.append(wordPair[1])
        return deconstructedData

    #Generate trainingData
    with open(targetDir,'a') as f:
            data = []
            for i in range(n):
                randGuesses = [["X","X"],["X","X"],["X","X"],["X","X"],["X","X"]]
                randTarget = words[random.randint(0,len(words)-1)]

                #Not included in data
                for j in range(3):
                    randGuess = words[random.randint(0,len(words)-1)]
                    curfeedBack = feedBack(randGuess,randTarget)
                    randGuesses[j] = [randGuess,curfeedBack]
                
                #Included in data
                for j in range(1):
                    randGuess = words[random.randint(0,len(words)-1)]
                    curfeedBack = feedBack(randGuess,randTarget)
                    randGuesses[j] = [randGuess,curfeedBack]

                    data.append(deconstructArr(randTarget,randGuesses))
                
            for line in data:
                writeLine = ""
                for argument in line:
                    if writeLine != "":
                        writeLine += " "
                    writeLine += str(argument)
                writeLine += "\n"
                f.write(writeLine)

#Init wordlist
readWords()

generateData(25000,"TrainingData.txt")