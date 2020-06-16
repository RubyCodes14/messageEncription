import time

class CharList():
    def __init__(self):
        
        self.characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
                      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", \
                      "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
                      "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
                      " ", "0", "1", "2", \
                      "3", "4", "5", "6", "7", "8", "9", "\n", ".", ",", ":", ";", "-", "_", "+", "=", \
                      "(", ")", "*", "!", "\\", "\"", "\'"] 

class Exit():
    def __init__(self):
        pass
    def _exit(self, message = "", e = True):
        print(message) #any message before exting comes here!
        print("\n", "__" * 51)
        print(" Powered By:".rjust(56, "*"), "**"*23, "\n \t \t \t\t\tEne-Une Reuben OCHEDI\n", "All Rigths Reserved.".rjust(60, " "), "\n", "(c)2019-2020".rjust(56, " "))
        print("\n", "+-" * 51)
        print("\tEmail: rubycodes14@gmail.com\t  LinkedIn: Ene-une Ochedi\t  GitHub: RubyCodes14\n\
    \tFacebook: Ene-une Reuben Ochedi\t  Twitter: @rubycodes14\t\tWhatsApp: +234 (813)-602-0460")
        print("", "==" * 51)
        if e:           
            input("Press Enter to Exit>>>")     # by default, uses this method to wait for user to exit
        else:
            exit()      #uses this to exit if the 2nd (boolean) argument is passed as False

class MyTime():         #Returns the time a file was created as string, to append to a file name
    def __init__(self):
        self.epochTime = time.gmtime(time.time())
    def MTime(self):  
        concat_Time, unit_Time = "", ""
        for i in range(6):
            if i != 3:
                unit_Time = str(self.epochTime[i])
            else:
                unit_Time = str(int(self.epochTime[3]) + 1)
                
            if len(unit_Time) == 1:
                unit_Time = "0" + unit_Time
            concat_Time += unit_Time
        return concat_Time
