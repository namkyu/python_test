#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, datetime, os, sys

class SearchLog:

	# ===========================================
	# init
	# ===========================================
	def __init__(self, param_map):
		self.user_name = param_map.get("user_name")
		self.selected_release_num = param_map.get("selected_release_num")
		self.remote_home_dir = param_map.get("remote_home_dir")
		self.search_file = param_map.get("search_file")
		self.server_list_dir = param_map.get("server_list_dir")
		self.download_root_dir = param_map.get("download_root_dir")
		self.server_info = param_map.get("server_info")
		self.my_own_dir = "nklee_" + datetime.date.today().strftime("%Y%m%d")
		
		self.server_list_file_name = self.server_info.get(self.selected_release_num)[0]
		self.project_name = self.server_info.get(self.selected_release_num)[1]
	
	# ===========================================
	# 다운로드 받을 디렉토리 생성
	# ===========================================
	def make_my_own_download_dir(self):		
		cmd = "mkdir -p %s" % (self.get_download_dir())
		print(cmd)
		subprocess.call(cmd, shell=True)
	
	# ===========================================
	# 다운로드 디렉토리 경로
	# ===========================================
	def get_download_dir(self):
		return self.download_root_dir + os.sep + self.my_own_dir
	
	# ===========================================
	# 로그 가져오기
	# ===========================================
	def get_log_files(self):		
		server_list = open(self.server_list_dir + "/" + self.server_list_file_name)
		for server in server_list:
			# 파일 추출
			ssh_cmd = """
				ssh %s "cd ~/GPORTAL/%s/tomcat/logs; find -name '%s'"
			""" % (server.strip(), self.project_name, self.search_file)
			popen = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			(stdoutdata, stderrdata) = popen.communicate()
			file_list = stdoutdata.split("\n")
			
			# 파일 다운로드
			for file_name in file_list:
				if len(file_name) > 0:
					file_name = file_name[2:len(file_name)]
					cmd = "scp %s@%s:~/GPORTAL/%s/tomcat/logs/%s %s/%s" % (
											  self.user_name
											, server.strip()
											, self.project_name
											, file_name
											, self.get_download_dir()
											, server.strip() + "_" + file_name.split("/")[-1]
											)
					print("download file name : " + server.strip() + "_" + file_name.split("/")[-1])
					subprocess.call(cmd, shell=True)

	# ===========================================
	# 실행
	# ===========================================
	def execute(self):
		# 오늘날짜의 다운로드 디렉토리 생성
		self.make_my_own_download_dir()
		# 로그 다운로드
		self.get_log_files()
		print("Done!!")

# ===========================================
# execute_main
# ===========================================
if __name__ == "__main__":
	
	server_info = {
		1 : ["g2-api", "NShop-API-G2"],
		2 : ["g2-front", "NShop-Front-G2"],
		3 : ["api", "NShop-API"],
		4 : ["front", "NShop-Front"],
	}

	for key in server_info:
		print(str(key) + " : " + str(server_info.get(key)))
		
	print("========================================================================")
	selected_release_num = raw_input("배포 대상을 선택해주세요. (번호 입력) ==> ")
	print("========================================================================")

	print("==========================================================")
	print("Please write log file name")
	print("ex) N2 프로젝트 : catalina.2015-11-12.log.gz, catalina.out, gate_info.20151112_17.gz")
	print("ex) G2 프로젝트 : catalina.2015-11-12.log.gz, catalina.out, rest_api.20151112_17.gz")
	print("==========================================================")
	search_file = sys.stdin.readline().strip()

	param_map = {}
	param_map["user_name"] = "fxdev"
	param_map["selected_release_num"] = int(selected_release_num)
	param_map["remote_home_dir"] = "/home/fxdev"
	param_map["search_file"] = search_file
	param_map["server_list_dir"] = "/home/fxdev/shell/serverlist"
	param_map["download_root_dir"] = "/home/fxdev/shell/logs"
	param_map["server_info"] = server_info
	
	searchLog = SearchLog(param_map);
	searchLog.execute()