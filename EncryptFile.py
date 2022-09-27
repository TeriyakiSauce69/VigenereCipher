import random
import sys
import ntpath



def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def encrptyHTMLFile(path_to_key,file):
    key = ""

    with open(path_to_key, "r") as f:
        lines = f.readlines()

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


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(len(sys.argv))
        print("Wrong number of arguements")
        sys.exit(1)
    # if int(sys.argv[1])< 1:
    #     print("KeySize should be > 0")
    #     sys.exit(1)
    print(encrptyHTMLFile(sys.argv[1],sys.argv[2]))
