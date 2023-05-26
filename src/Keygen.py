'''
----------------
| Keygenerator |
----------------
'''
import os
import random
import string

# Variables
alpha = 'ABCDEFGHIJKLOPQTUVXYZabcdefghijklmnopqrstuvwyxz1234567890-_.$@'
password = []
length = 0

def generatePass(generatedPassword, leng):
    while len(generatedPassword) < leng:
        generatedPassword.append(alpha[random.randrange(0, len(alpha))])
    return generatedPassword

# Init the Program
def initProgram():
    try:
        txt = open('passwords/pass.txt', '+a')
        print('--------------------------------------------------------------')
        print('|                        Keygenerator                        |')
        print('--------------------------------------------------------------')
        print('Select a length for your pass: [8] [16] [32] [64] [128] [...]')
        length = input('> ')
        if len(length) > 0 and length != "0":
            p = generatePass(password, int(length))
            txt.write(f"[Password]: {''.join(p)} \n")
            print(f"Password generated in {txt.name}")
            input('...')
            txt.close()
    except:
        os.mkdir('passwords')
        initProgram()

initProgram()
