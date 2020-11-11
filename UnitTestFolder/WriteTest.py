class writeTest:
    fav1="AAPL"
    fav2="WMT"
    fav3="AMZN"

    def writeFile(self, str1, str2):

        if str1 == "fav1":
            self.fav1 = str2
        if str1 == "fav2":
            self.fav2 = str2
        if str1 == "fav3":
            self.fav3 = str2

        theFile= open("../settings.txt", "w")
        theFile.write("fav1=" + self.fav1 + "=\n")
        theFile.write("fav2=" + self.fav2 + "=\n")
        theFile.write("fav3=" + self.fav3 + "=\n")

        theFile.close()

test = writeTest()
test.writeFile("fav3", "CSCO")