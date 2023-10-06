
def updateTxtFile(str):
    f = open("Prompts.txt", "a")
    f.write(str)
    f.close()