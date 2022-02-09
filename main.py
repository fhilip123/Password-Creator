# imports
import random

# list of characters that will be used by the application
charList = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()'


# creates a randomly generated password
def createPassword(length):
    newPass = ''
    for i in range(length):
        randChar = random.randint(0, len(charList) - 1)
        newPass += charList[randChar]
    print(newPass)


# console stuff
print('---PASSWORD CREATOR---')
lengthInput = int(input('How many characters :'))
createPassword(lengthInput)
