import random
import sys
import ntpath



def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def originalText(cipher_text_path, path_to_key):
    key = ""

    with open(path_to_key, "r") as f:
        lines = f.readlines()

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(len(sys.argv))
        print("Wrong number of arguments")
        sys.exit(1)
    # if int(sys.argv[1])< 1:
    #     print("KeySize should be > 0")
    #     sys.exit(1)
    print(originalText(sys.argv[1],sys.argv[2]))