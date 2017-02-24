
from kyu.utils.search_log import *


server_info = {
    1 : ["g2-api", "NShop-API-G2"],
    2 : ["g2-front", "NShop-Front-G2"],
    3 : ["api", "NShop-API"],
    4 : ["front", "NShop-Front"],
}

param_map = {}
param_map["user_name"] = "administrator"
param_map["selected_release_num"] = 3
param_map["remote_home_dir"] = "/home/administrator"
param_map["search_file"] = "catalina.2016-05-25.log.gz"
param_map["server_list_dir"] = "E:\\test\\python\\serverlist"
param_map["download_root_dir"] = "E:\\test\\python\\log_download"
param_map["server_info"] = server_info

searchLog = SearchLog(param_map);
#searchLog.execute()

log_file_name = "./gate/20160523/gate_info.20160523_14.gz"
log_file_name_result = log_file_name[2:len(log_file_name)] 
print log_file_name_result

log_file_name1 = "./gate_info.20160523_14.gz"
log_file_name1_result = log_file_name1[2:len(log_file_name1)]
print log_file_name1_result


print log_file_name_result.split("/")[-1]

print log_file_name1_result.split("/")[-1]