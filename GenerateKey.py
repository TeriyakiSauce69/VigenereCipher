import random
import sys
import ntpath


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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Wrong number of arguements")
        sys.exit(1)
    if int(sys.argv[1])< 1:
        print("KeySize should be > 0")
        sys.exit(1)
    print(generateKey(int(sys.argv[1])))