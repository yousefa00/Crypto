import threading  # Code to run two simultaneous processes
import random  # Library that allows for a variety of math functions
lock = threading.Lock()
level = ""
# xcoors is an array of x coordinates in the maze
xcoors = [271, 271, 181, 181, 146, 146, 118, 118, 147, 147, 178, 181, 240, 240, 207, 210, 272, 271, 180, 180, 148, 147, 117, 116, 56, 53, 20, 25, 84, 87, 114, 119, 176, 176, 9]
# ycoors is an array of y coordinates in the maze
ycoors = [271, 179, 178, 208, 208, 178, 177, 116, 115, 87, 85, 116, 116, 84, 84, 56, 59, 25, 25, 52, 52, 25, 24, 80, 83, 24, 23, 116, 119, 208, 211, 239, 240, 269, 270]
xcoor = 0
ycoor = 0
answer = True
offset = random.randint(1, 20)  # Generates an offset for the Ascii numbers
def game():
    global answer  # Creates a global variable
    if level.lower() == "beginner":
        x = 8
        y = 4
        nextNumx = []  # Array of X values
        nextNumy = []  # Array of Y values
        count = 0
        r1 = 1
        while count <= 35:  # Loops and adds the next x and y coordinates to two arrays for guessing
            if r1 == 1:
                x += 2
                y += 2
                r1 += 1
                nextNumx.append(x)  # Adds X to array
                nextNumy.append(y)  # Adds y to array
                count += 1
            elif r1 == 2:
                x += 2
                r1 -= 1
                nextNumx.append(x)
                nextNumy.append(y)
                count += 1

        count2 = 0
        arrayNum = 0



        while count2 <= 34 and answer is True:  # Loop to prompt user for next guess
            guessX = int(input("Guess your next X value: "))
            guessY = int(input("Guess your next Y value: "))
            if guessX == nextNumx[arrayNum] and guessY == nextNumy[arrayNum]:  # Checks if guess is equal to the next number
                global xcoor
                global ycoor
                print("Correct")
                lock.acquire()
                xcoor = xcoors[arrayNum]  # Acquires and releases variables to and from Main.py
                ycoor = ycoors[arrayNum]
                lock.release()  # Unlock var
                arrayNum += 1
                count2 += 1
            else:
                answer = False
                gameLost()
            if count2 == 35:
                gameOver()
    elif level.lower() == "expert":
        # Phrases to encrypt
        arrayPhrase = ["cat", "dog", "yellow", "next", "hello", "what", "this", "is", "a", "maze", "what", "about", "a", "number", "?", "12", "1", "oops", "dont", "lose", "or", "else", "you", "will", "fail", "ok", "was", "android", "apple", "%", "laugh", "wow", "you", "are", "now", "done"]
        arrayEncrypt = []  # Array that will hold all the encrypted phrases
        countArr = 0
        while countArr < arrayPhrase.__len__():  # Loops until the end of the array of phrases
            encWord = encryptExpert(arrayPhrase[countArr], offset)
            arrayEncrypt.append(encWord)
            countArr += 1
        print("Encrypted word:", arrayEncrypt[0])

        count3 = 0
        encarrayNum = 1
        arrayNum = 0
        while count3 <= 34 and answer is True:  # Loops to test if answer is true
            print("Next word:", arrayEncrypt[encarrayNum])
            guessEnc = input("Guess the word: ")
            if guessEnc == arrayPhrase[encarrayNum]:
                print("Correct")
                lock.acquire()
                xcoor = xcoors[arrayNum]
                ycoor = ycoors[arrayNum]
                lock.release()
                # unlock var
                arrayNum += 1
                encarrayNum += 1
                count3 += 1
            else:
                answer = False
                gameLost()
        if count3 == 35:
            gameOver()
    elif level.lower() == "insane":
        # Phrases to encrypt
        arrayPhrase = ["cat", "dog", "yellow", "next", "hello", "what", "this", "is", "a", "maze", "what", "about", "a", "number", "?", "12", "1", "oops", "dont", "lose", "or", "else", "you", "will", "fail", "ok", "was", "android", "apple", "%", "laugh", "wow", "you", "are", "now", "done"]
        arrayEncrypt = []  # Array that will hold all the encrypted phrases
        countArr = 0
        while countArr < arrayPhrase.__len__():  # Loops until the end of the array of phrases
            encWord = encryptInsane(arrayPhrase[countArr], offset)
            arrayEncrypt.append(encWord)
            countArr += 1
        print("Encrypted word:", arrayEncrypt[0])

        count3 = 0
        encarrayNum = 35
        arrayNum = 0
        while count3 <= 34 and answer is True:  # Loops to test if answer is true
            print("Next word:", arrayEncrypt[encarrayNum])
            guessEnc = input("Guess the word: ")
            if guessEnc == arrayPhrase[encarrayNum]:
                print("Correct")
                lock.acquire()
                xcoor = xcoors[arrayNum]
                ycoor = ycoors[arrayNum]
                lock.release()
                # unlock var
                arrayNum += 1
                encarrayNum -= 1
                count3 += 1
            else:
                answer = False
                gameLost()  # Runs losing code
        if count3 == 35:
            gameOver()  # Runs winning code




def gameOver():
    print("Congratulations, you have reached the end of the maze!")
def gameLost():
    print("Oops, you have fallen into a trap...GAME OVER!")
def encryptExpert(word, offset):
    index = 0
    size = word.__len__()
    encChars = []
    while index < size:  # Loops till the end of the phrase
        char = word[index]
        charCode = ord(char)  # Changes each character to ascii code
        encCharCode = charCode + offset  # Adds a random offset
        encChars.append(encCharCode)
        index += 1
    return encChars
def encryptInsane(word, offset):
    index = 0
    size = word.__len__()
    encChars = []
    while index < size:  # Loops till the end of the phrase
        char = word[index]
        charCode = str(bin(ord(char))).replace("0b", "")  # Changes each character to binary and removes "0b"
        encCharCode = charCode + "1"  # Adds one to the end of the string
        encChars.append(encCharCode)  # Appends to an array of encrypted coordinates
        index += 1
    return encChars