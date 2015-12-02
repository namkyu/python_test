test = "/home/test/ROOT##3/test/test/test.jsp"
resultArr = test.split("##")
webRoot = resultArr[0]
filePath = resultArr[1]
destinationSourcePath = filePath[filePath.find("/"):]
print(webRoot + destinationSourcePath)




