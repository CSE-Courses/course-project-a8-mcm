class writeTest:
    fav1="AAPL"
    fav2="WMT"
    fav3="CSCO"

    def writeFile(self, str):
        if self.fav1 != "" and self.fav2 != "" and self.fav3 != "":
            print("Favorite list is full!")
        elif self.fav1 == "":
            self.fav1 = str
        elif self.fav2 == "":
            self.fav2 = str
        elif self.fav3 == "":
            self.fav3 = str

        theFile= open("testSettings.txt", "w")
        theFile.write("fav1=" + self.fav1 + "=\n")
        theFile.write("fav2=" + self.fav2 + "=\n")
        theFile.write("fav3=" + self.fav3 + "=\n")

        theFile.close()

    def delFav(self, str):
        if str == "fav1":
            self.fav1 = ""
        if str == "fav2":
            self.fav2 = ""            
        if str == "fav3":
            self.fav3 = ""    
            print(self.fav3)

        #print(self.fav1)
        #print(self.fav2)
        #print(self.fav3)

        theFile= open("testSettings.txt", "w")
        theFile.write("fav1=" + self.fav1 + "=\n")
        theFile.write("fav2=" + self.fav2 + "=\n")
        theFile.write("fav3=" + self.fav3 + "=\n")

        theFile.close()

#unit test for writeFile
test = writeTest()
test.delFav("fav1")
#test.writeFile("PPPQ")