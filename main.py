import re

readFile = open("./testconv.py")
writeFile = open("./converted.cpp", "w")
lines = readFile.readlines()
writeLines = []

tabNumber = 0
classDict = {}
filePointer = 1

def lineWrite(text, writeLines=writeLines, filePointer=filePointer, tabNumber=tabNumber):
    if re.findall(";\n", text) == []:
        text = text + ";\n"
    print(filePointer)
    print(tabNumber)
    text = (tabNumber * 4) * " " + text
    writeLines.insert(filePointer, text)

# layer/stage 1: modifications for conversion
def fixClass(findClass="main", filePointer=filePointer, tabNumber=tabNumber):
    for line in lines:
        if re.findall("class main():", line) == "class main():":
            return True
    writeLines.append("int main() {\n")
    filePointer += 1
    tabNumber += 1
    lineWrite("int num = 5;\n")
    classDict.update(main = 'int')
    writeLines.append("}\n")
    print(classDict)
    return False

fixClass()

writeFile.writelines(writeLines)
readFile.close()
writeFile.close()