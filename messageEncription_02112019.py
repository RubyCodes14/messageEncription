
import os
from data_ei import CharList, Exit, MyTime


whole_Encription = []       #contains the total encription for all text input

encripted  = []
#textCases = []
currentPos = 0

name = "EncriptedFiles"
if(os.access(name, os.F_OK)):
    pass
else:
    os.mkdir(name)
    print("A folder named", name, "has been created")
    print("ALL YOUR ENCRIPTED FILES WILL BE SAVED IN THE FOLDER.\n")


def getFileName():
    global filename, fn
    filename = input("Enter a Filename to save your data: ")
    fn = filename
    filename = name + "/" + filename + ".txt"
    #flag = 0
    #flg = flag
    """if condition:
        if flag < 3:
           getFileName(flag, condition)
           function
        else:
            quit()"""
        
getFileName()


def checkFileName(flag = 1):
    global overwrite, existing
    overwrite = False
    if(os.access(filename, os.F_OK)):
        existing = input("A file already exist with that name. Do you want to \nOverwrite - 1\n\
Save a sequel copy - 2\nAppend - 3\n[Press Enter to enter a name again]\nGo for Option: ")
        exist = existing
        
        if exist == "1":
            pass
        else:
            exist = 0
        
        overwrite = bool(exist)
        
        if overwrite:
            print("The file will be overwritten once you enter your message.")
        else:
            if existing == "2":
                print("Save a Sequel copy as", fn + "-Copy" + MyTime().MTime())
            elif existing == "3":
                print("Append...")
            elif existing == "":
                if flag <= 2:
                    getFileName()
                    flag += 1
                    checkFileName(flag)
                else:
                    copy = True
                    print("since you could not get a different filename, we are saving a copy for you as", fn + "-Copy")


checkFileName()

text = input("Enter Message (or Press Enter to upload a file to encript): ")
if text == "":
    print("Make sure your file is located in the directory: ", os.getcwd())
    fileUpload = input("Enter the File name here: ")
    if (os.access((fileUpload + ".txt"), os.F_OK)):
        upload = open(fileUpload + ".txt", "r")
        text = upload.read()
        upload.close()
print("\nFile Encripted Successfully" + "\n" + "__" * 52)
for letter in text:
    _letter = letter
    for char in CharList().characters:
        if _letter == "":
            letter = "\n"
            
        if letter == char:                    
            cipher = CharList().characters.index(char)             #encription
            if currentPos > cipher:    
                encripted.append(cipher - currentPos)
            else:
                encripted.append(cipher)                    
            currentPos = cipher
print(encripted)
    
if not(os.access(filename, os.F_OK)) or overwrite:    #if file does not exist already, this will create the new file to save encripted data
    save = open(filename, "w")
    save.write(str(encripted))
    save.close()
    print("__" * 52 + "\nEncripted Data saved successfully")
else:
    if existing == "2" or copy:
        filename = fn + "-Copy" + MyTime().MTime() + ".txt"
        save = open(filename, "w")
        save.write(str(encripted))
        save.close()
        print("Encripted Data saved successfully")
    elif existing == "3":
        save = open(filename, "a")              #if the file already exist, then the newly entered data will be appended to it
        save.write(str(encripted))
        save.close()
        print("Encripted Data saved successfully")   



Exit()._exit()


input("")
