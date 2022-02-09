from hashlib import new
from operator import le
import random

from scipy import rand

charList = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()'


def createPassword(length):
    newPass = ''
    for i in range(length):
        randChar = random.randint(0, len(charList) - 1)
        newPass += charList[randChar]
    print(newPass)


def new_func(length):
    len(length)


print('---PASSWORD CREATOR---')
lengthInput = int(input('How many characters :'))
createPassword(lengthInput)
