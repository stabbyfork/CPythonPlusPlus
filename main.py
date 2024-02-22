import re

readFile = open("./testconv.py")
writeFile = open("./converted.cpp", "w")

tabNumber = 0

# layer/stage 1: modifications for conversion
if re.findall("class main():", readFile.read()) == None:
    writeFile.write("int main() {")