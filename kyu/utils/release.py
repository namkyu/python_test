#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import subprocess
import tarfile
import shutil

# ===========================================
# global variable
# ===========================================
profile_active = ""
gportal_path = ""
java_home = ""
war_home = ""
tar_path = ""
mode = ""

# ===========================================
# help
# ===========================================
def release_help():
	print("===============================================================")
	print("파라미터 셋팅 정보")
	print("===============================================================")
	print("profile_active : 환경 정보 셋팅")
	print("project_name : 프로젝트 이름")
	print("gportal_path : GPortal 디렉토리 패스")
	print("war_home : 배포할 war가 존재하는 디렉토리")
	print("tar_path : war를 압축한 상태의 tar.gz 경로")
	print("mode : 배포 방법")
	sys.exit()  # 강제 종료

# ===========================================
# common function
# ===========================================
def get_param_data(parameter_str):
	parameter_map = {}
	parameters = parameter_str.split("#")
	
	print("####################### Param Data ########################")	
	for item in parameters:
		print(item)
		items = item.split("=")
		parameter_map[items[0]] = items[1]
	print("###########################################################")

	return parameter_map


# ===========================================
# 톰켓 시작
# ===========================================
def start_tomcat(service_name):
	try:
		retcode = subprocess.call("BUILD_ID=dontKillMe %s/%s/tomcat/bin/startup.sh" % (gportal_path, service_name), shell=True)
		if retcode < 0:
			print "Unable start the tomcat service[%s]" % retcode
		elif retcode == 0:
			print "Tomcat service is started succesfully[%s]" % retcode
		else:
			print "Tomcat Service started already[%s]" % retcode
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# 톰켓 중지
# ===========================================
def stop_tomcat(service_name):
	try:
		retcode = subprocess.call("ps -ef | grep %s/%s/ | grep -v grep | awk '{print$2}' | xargs kill" % (gportal_path, service_name), shell=True)
		if retcode < 0:
			print "Unable stop the tomcat service[%s]" % retcode
		elif retcode == 0:
			print "Tomcat service is stopped succesfully[%s]" % retcode
		else:
			print "Tomcat service stopped already[%s]" % retcode
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# 톰켓 재시작
# ===========================================
def restart_tomcat(service_name):
	try:
		stop_tomcat(service_name)
		time.sleep(10)
		start_tomcat(service_name)
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# java execute
# ===========================================
def execute_java(war_home_dir, project_folder_name):
	try:
		subprocess.call("%s/bin/jar xf %s/%s.war" % (java_home, war_home_dir, project_folder_name), shell=True)
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# tar 압축 해제
# ===========================================
def extract_tar():
	try:
		tar = tarfile.open(tar_path, "r:gz")
		for item in tar:
			tar.extract(item, war_home)
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# 배포
# ===========================================
def release(webappspath, project_name):

	# 디렉토리 삭제, 생성
	if mode == "release":
		if os.path.exists(webappspath):
			shutil.rmtree(webappspath)
		os.makedirs(webappspath)

	# 디렉토리 이동
	os.chdir(webappspath)

	# 망 별 war 압축 풀기
	if profile_active == "op":
		op_war_path = war_home % project_name
		execute_java(op_war_path, project_name)
	elif profile_active is not "op":
		extract_tar()
		execute_java(war_home, project_name)

	# 톰켓 재시작
	if mode == "release":
		restart_tomcat(project_name)

	# thread sleep
	time.sleep(10)
	
# ===========================================
# 핫디플로이
# ===========================================
def hot_deploy_releae(webappspath, project_name):
	#webApps = gportal_path + "/" + project_name + "/tomcat/webapps"
	webApps = webappspath[0:webappspath.rfind("/")]
	print("webApps=" + webApps)
	
	# war 파일 리스트 추출 후 정렬
	root_files = []
	for root, dirs, files in os.walk(webApps, topdown=False):
		root_files = files
	root_files.sort()
	print("root_files=" + root_files)
	
	# latest war 버전 추출
	latest_war_file = max(root_files)
	start_num = latest_war_file.rfind("#") + 1
	end_num = latest_war_file.rfind(".")
	version = latest_war_file[start_num:end_num]
	
	# 신규 버전 war 파일 이름 생성
	new_version = version + 1
	rename_war_file_name = "ROOT##%d.war" % new_version
	print("rename_war_file_name=" + rename_war_file_name)
	
	# war 배포
	source = war_home + "/" + project_name + ".war"
	dest = webApps + "/" + rename_war_file_name
	shutil.copy2(source, dest)
	print("source=" + source + ", dest=" + dest)
	
	# 새로 배포된 application이 startup 되기를 기다린다.
	time.sleep(20)
	
	# 기존배포되어 있던 war 파일을 삭제
	for root_war_file in enumerate(root_files):
		if root_war_file != rename_war_file_name:                
			os.remove(webApps + root_war_file)

# ===========================================
# execute_main
# ===========================================
def execute_main(param):
	# 전역 변수 선언
	global profile_active
	global gportal_path
	global java_home
	global war_home
	global tar_path
	global mode
	global hot_deploy
	
	# 파라미터 추출
	param_map = get_param_data(param)
	profile_active = param_map.get("profile_active")
	gportal_path = param_map.get("gportal_path")
	hot_deploy = param_map.get("hot_deploy")
	java_home = param_map.get("java_home")
	war_home = param_map.get("war_home")
	tar_path = param_map.get("tar_path")    # op망을 제외한 망에서만 사용
	mode = param_map.get("mode")

	project_names = param_map.get("project_name").split(",")
	for project_name in project_names:

		# webappspath 디렉토리
		if profile_active == "op":
			webappspath = gportal_path + "/" + project_name + "/webapps/ROOT"
		elif profile_active is not "op":
			webappspath = gportal_path + "/" + project_name + "/tomcat/webapps/ROOT"

		# 배포 (일반디플로이, 핫디플로이)
		if hot_deploy == "Y":
			hot_deploy_releae(webappspath, project_name)
		else:
			release(webappspath, project_name)

# ===========================================
# execute_main
# ===========================================
if __name__ == "__main__":

	# 파라미터 체크
	argument_len = len(sys.argv)
	if argument_len < 2:
		release_help()

	# execute_main main
	execute_main(sys.argv[1])

