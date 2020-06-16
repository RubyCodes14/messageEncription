
import os
from data_ei import CharList, Exit, MyTime


read = []
#caseNo = 1000
#caseID = 500

name = "DecriptedFiles"
name2 = "EncriptedFiles"
if(os.access(name, os.F_OK)):
    pass
else:
    os.mkdir(name)
    print("A folder named", name, "has been created")
    print("ALL YOUR DECRIPTED FILES WILL BE SAVED IN THE FOLDER.\n")

file_ = input("Enter the filename to be Decripted: ")
file = name2 + "/" + file_ + ".txt"

if os.access(file, os.F_OK):
    print("File", file_ + ".txt", "selected successfully!")
    print("\nHere's the content:\n" + "__" * 52 + "\n" + "**" * 52 + "\n")

    openFile = open(file, "r")
    reading = openFile.read()             #
    #openFile.close()
    neg = str(0)
    i = 1
    for c in range(len(reading)):
        char = reading[c]

        if char == "-":
            neg = char
        if char.isnumeric():
            char = neg + char
            if reading[c+1].isnumeric():
                char = char + reading[c+i]
            if reading[c-1].isnumeric():
                pass
            else:
                read.append(int(char))         
            neg = str(0)

    
else:
    if file_ != "":
        Exit()._exit("Oops... No such file exist.", False)
    else:
        Exit()._exit("Oops... No file name entered.", False)

textFile = " "
#print(read)
for i in range(len(read)):
    chars = int(read[i])
    charIndex = chars
    if charIndex < 0:
        ch = CharList().characters[prevChar + charIndex]
        textFile += ch
        prevChar = prevChar + charIndex
    else:           
        ch = CharList().characters[charIndex]
        textFile += ch
        prevChar = charIndex 
        #prevChar = chars
print(textFile)
print("\n" + "__" * 52 + "\n" + "**" * 52 + "\n\n")

saveDecFile = input("Enter 's' if you want to Save the decripted message (as a new file): ").upper()
if saveDecFile == "S":
    savedDec = open(name + "/" + file_ + "_DEC" + MyTime().MTime() + ".txt", "w")
    savedDec.write(textFile)
    savedDec.close()
    print("Your decripted file has been saved successfully as", file_ + "_DEC" + MyTime().MTime() + ".txt") 


Exit()._exit()

input("")
