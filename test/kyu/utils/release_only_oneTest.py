#test = "/home/test/ROOT##3/test/test/test.jsp"
test = "/home/test/ROOT/test/test/test.jsp"

if test.find("##") > -1:
    resultArr = test.split("##")
    webRoot = resultArr[0]
    filePath = resultArr[1]
    destinationSourcePath = filePath[filePath.find("/"):]
    print(webRoot + destinationSourcePath)
else:
    print(test)


