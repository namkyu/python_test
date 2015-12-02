#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, sys, datetime

class SearchLog:

	def __init__(self, user_name, project_name):
		self.user_name = user_name
		self.home_dir = "/home/" + user_name
		self.project_name = project_name
		self.download_log_dir = self.home_dir + "/shell/logs/" + self.get_log_dir_name()

	def get_log_files(self, file_name, server_list_file):		
		server_list = open(server_list_file)
		for server in server_list:
			print(server.strip())
			cmd = "scp %s@%s:%s/GPORTAL/%s/tomcat/logs/%s %s/%s" % (self.user_name
												, server.strip()
												, self.home_dir
												, self.project_name
												, file_name
												, self.download_log_dir
												, server.strip() + "." + file_name[file_name.rfind("/") + 1:])
			subprocess.call(cmd, shell=True)

	def make_log_dir(self):
		cmd = "mkdir -p %s" % (self.download_log_dir)
		subprocess.call(cmd, shell=True)
		
	def get_log_dir_name(self):
		d = datetime.date.today()
		log_dir_name = "nklee_" + d.strftime("%Y%m%d")
		return log_dir_name

	def get_server_info(self):
		server_info_map = {}
		server_info_map["TestApp-API"] = self.home_dir + "/shell/serverlist/api"
		server_info_map["TestApp-Front"] = self.home_dir + "/shell/serverlist/front"			
		server_info_map["TestApp-Front-InGame"] = self.home_dir + "/shell/serverlist/ingame"
		return server_info_map


print("==========================================================")
print("What do you want to search log of web project?")
print("TestApp-API, TestApp-Front, TestApp-Front-InGame")
print("==========================================================")
project_name = sys.stdin.readline().strip()

print("==========================================================")
print("Please write log file name")
print("ex) [API] catalina.2015-11-12.log.gz, catalina.out, gate/20151112/gate_info.20151112_17.gz")
print("ex) [Front] catalina.2015-11-12.log.gz, catalina.out, user/20151112/user_history.20151112_17.gz")
print("==========================================================")
search_file = sys.stdin.readline().strip()


searchLog = SearchLog("administrator", project_name);
searchLog.make_log_dir()

# 서버 리스트 파일 경로 추출
server_info_map = searchLog.get_server_info()
server_list_file = server_info_map.get(project_name)
print(server_list_file)

# 로그 다운로드
searchLog.get_log_files(search_file, server_list_file)