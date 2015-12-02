test = "aaa"

server_info_map = {}
server_info_map["TestApp-API"] = test + "/shell/serverlist/api"
server_info_map["TestApp-Front"] = "/shell/serverlist/front"            
server_info_map["TestApp-Front-InGame"] = "/shell/serverlist/ingame"

get_file = "TestApp-API"
result = server_info_map.get(get_file)
print(result)


import time, datetime
now = time.localtime()
print(now)

d = datetime.date.today()
time = "nklee_" + d.strftime("%Y%m%d")
print(time)

filePath = "a/b/c/test.gz"
destinationSourcePath = filePath[filePath.rfind("/") + 1:]
print(destinationSourcePath)
