import random
import sys

def generateKey(keySize):
    k = []
    for i in range(keySize):
        k.append(chr(random.randrange(26)+ord('A')))
    return("".join(k))

#Encryption
#Input: path to a html file and the file that has the key
#Output: Encrypted html file (add _end to the end of the new filename)
def encrptyHTMLFile(key,file):
    encryptedText = []
    plainText = ""


    with open("C:/Users/ihate/Desktop/htmlexample.html", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            plainText+=line
    return ''.join(plainText.splitlines())
    #print(plainText)
    # with open("C:/Users/ihate/Desktop/htmlexample.html", "w") as f:
    #     for line in lines:
    #         #f.write(line)


    # for i in range(len(string)):
    #     x = (ord(string[i]) + ord(key[i])) % 26
    #     x += ord('A')
    #     encrypt_text.append(chr(x))
    #
    # return ("".join(encryptedText))

print(encrptyHTMLFile(4,4))

# print(generateKey(10))