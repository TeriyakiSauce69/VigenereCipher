import random
import sys

#Return Generated Random KeySize of Size N
def generateKey(keySize):
    k = []
    for i in range(keySize):
        k.append(chr(random.randrange(26)+ord('A')))
    return("".join(k))

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

#Encryption
#Input: path to a html file and the file that has the key
#Output: Encrypted html file (add _end to the end of the new filename)
def encrptyHTMLFile(key,file):
    encryptedText = []
    plainText = ""

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            #print(line)
            plainText+=line

    repeated_Key = repeat_to_length(key,len(plainText))


    for i in range(len(plainText)):
        if alpha.find(plainText[i].upper()) == -1:
            #print(plainText[i])
        #if ord(plainText[i]) <= 64:

            encryptedText.append((plainText[i]))
            continue

        x = (ord(plainText[i].upper()) + ord(repeated_Key[i])) % 26
        x += ord('A')

        if plainText[i].isupper():
            encryptedText.append(chr(x))
        elif plainText[i].islower():
            encryptedText.append(chr(x).lower())

    return (("".join(encryptedText)))

def originalText(cipher_text, key):
    orig_text = []

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    repeated_Key = repeat_to_length(key, len(cipher_text))

    for i in range(len(cipher_text)):
        # if ord(cipher_text[i]) < 65 or ord(cipher_text[i]) > 122:
        #     continue
        if alpha.find(cipher_text[i].upper()) == -1:
            orig_text.append(cipher_text[i])
            continue

        x = (ord(cipher_text[i].upper()) -
             ord(repeated_Key[i]) + 26) % 26
        x += ord('A')
        #orig_text.append(chr(x))

        if cipher_text[i].isupper():
            orig_text.append(chr(x))
        elif cipher_text[i].islower():
            orig_text.append(chr(x).lower())

    return("" . join(orig_text))

x = generateKey(10)

y =encrptyHTMLFile(x,"C:/Users/ihate/Desktop/htmlexample.html")
print(y)

print(originalText(y,x))
# y= repeat_to_length(x,37)
# print(y,len(y))
# print(x)
#
# encryptedstuff = (encrptyHTMLFile("C:/Users/ihate/Desktop/htmlexample.html",10))
# cipher_text =encryptedstuff
# print(cipher_text)
# # da_key = encryptedstuff[1]
# #print((encrptyHTMLFile(x,4))[0])
#
# print(originalText(cipher_text,x))
# print(generateKey(10))