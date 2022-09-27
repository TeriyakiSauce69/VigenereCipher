import random
import sys
import ntpath

def main():
    generateKey(10)
    #encrptyHTMLFile(x, "C:/Users/ihate/Desktop/htmlexample.html")
    #path_to_enrypted_file = encrptyHTMLFile(x, "C:/Users/ihate/Desktop/htmlexample.html")
    #originalText(,x)

#Return Generated Random KeySize of Size N
def generateKey(keySize):
    k = []
    for i in range(keySize):
        k.append(chr(random.randrange(26)+ord('A')))


    new_file = open("KeyFile.txt", "x")
    new_file.close()

    z = ("".join(k))

    with open("KeyFile.txt", "w") as f:
        #for line in z:
        f.write(z)
    print("New file text with key created as KeyFile.txt")
    #return("".join(k))

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#Encryption
#Input: path to a html file and the file that has the key
#Output: Encrypted html file (add _end to the end of the new filename)
def encrptyHTMLFile(path_to_key,file):
    key = ""

    with open(path_to_key, "r") as f:
        lines = f.readlines()
    with open(path_to_key, "w") as f:
        for line in lines:
            key += line


    encryptedText = []
    plainText = ""

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            plainText+=line

    repeated_Key = repeat_to_length(key,len(plainText))

    for i in range(len(plainText)):
        if alpha.find(plainText[i].upper()) == -1:
            encryptedText.append((plainText[i]))
            continue

        x = (ord(plainText[i].upper()) + ord(repeated_Key[i])) % 26
        x += ord('A')

        if plainText[i].isupper():
            encryptedText.append(chr(x))
        elif plainText[i].islower():
            encryptedText.append(chr(x).lower())

    new_file = open(path_leaf(file).replace(".html","_enc.html"), "x")
    new_file.close()

    new_enc_file = path_leaf(file).replace(".html", "_enc.html")

    lines = ("".join(encryptedText))

    with open(new_enc_file, "w") as f:
        for line in lines:
            f.write(line)
    print("New encrypted file created at " + new_enc_file)
    #return new_enc_file

def originalText(cipher_text_path, path_to_key):
    key = ""

    with open(path_to_key, "r") as f:
        lines = f.readlines()
    with open(path_to_key, "w") as f:
        for line in lines:
            key += line


    cipher_text = ""

    with open(cipher_text_path, "r") as f:
        lines = f.readlines()
    with open(cipher_text_path, "w") as f:
        for line in lines:
            cipher_text += line

    orig_text = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    repeated_Key = repeat_to_length(key, len(cipher_text))

    for i in range(len(cipher_text)):
        if alpha.find(cipher_text[i].upper()) == -1:
            orig_text.append(cipher_text[i])
            continue

        x = (ord(cipher_text[i].upper()) -
             ord(repeated_Key[i]) + 26) % 26
        x += ord('A')

        if cipher_text[i].isupper():
            orig_text.append(chr(x))
        elif cipher_text[i].islower():
            orig_text.append(chr(x).lower())

    new_file = open(path_leaf(cipher_text_path).replace("_enc.html", "_dec.html"), "x")
    new_file.close()

    new_enc_file = path_leaf(cipher_text_path).replace("_enc.html", "_dec.html")

    lines = ("".join(orig_text))
    with open(new_enc_file, "w") as f:
        for line in lines:
            f.write(line)

    return None


if __name__ == '__main__':
    main()