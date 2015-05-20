#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import sys
import tarfile
import time


def release_help():
	print("===============================================================")
	print("?��?��미터 ?��?�� ?���?")
	print("===============================================================")
	print("profile_active : ?���? ?���? ?��?�� (op, rc, stage, live)")
	print("project_name : ?��로젝?�� ?���?")
	print("gportal_path : GPortal ?��?��?���? ?��?��")
	print("war_home : 배포?�� war�? 존재?��?�� ?��?��?���?")
	print("tar_path : war�? ?��축한 ?��?��?�� tar.gz 경로")
	print("mode : 배포 방법")
	sys.exit()  # 강제 종료

# ===========================================
# common function
# ===========================================
def get_param_data(parameter_str):
	parameter_map = {}
	parameters = parameter_str.split("#")

	for item in parameters:
		print(item)
		items = item.split("=")
		parameter_map[items[0]] = items[1]

	return parameter_map


# ===========================================
# ?���? ?��?��
# ===========================================
def start_tomcat():
	try:
		retcode = subprocess.call("BUILD_ID=dontKillMe %s/%s/tomcat/bin/startup.sh" % (gportal_path, project_name), shell=True)
		if retcode < 0:
			print "Unable start the tomcat service ==> ", retcode
		elif retcode == 0:
			print "Tomcat service is started succesfully ==> ", retcode
		else:
			print "Tomcat Service started already ==> ", retcode
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# ?���? 중�?
# ===========================================
def stop_tomcat():
	try:
		retcode = subprocess.call("ps -ef | grep %s/%s/ | grep -v grep | awk '{ print$2}' | xargs kill" % (gportal_path, project_name), shell=True)
		if retcode < 0:
			print "Unable stop the tomcat service ==> ", retcode
		elif retcode == 0:
			print "Tomcat service is stopped succesfully ==> ", retcode
		else:
			print "Tomcat service stopped already ==> ", retcode
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# ?���? ?��?��?��
# ===========================================
def restart_tomcat():
	try:
		stop_tomcat()
		start_tomcat()
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
# tar ?���? ?��?��
# ===========================================
def extract_tar():
	try:
		tar = tarfile.open(tar_path, "r:gz")
		for item in tar:
			tar.extract(item, war_home)
		print("(Tar file extracted) tar_path=" + tar_path)
	except OSError, e:
		print "Execution failed:", e


# ===========================================
# 배포
# ===========================================
def release():

	# ?��?��?���? ?��?��, ?��?��
	if mode == "release":
		if os.path.exists(webappspath):
			shutil.rmtree(webappspath)
		os.makedirs(webappspath)

	# ?��?��?���? ?��?��
	print os.getcwd()
	os.chdir(webappspath)

	# �? �? war ?���? ??�?
	if profile_active == "op":
		op_war_path = war_home % project_name
		execute_java(op_war_path, project_name)
	elif profile_active is not "op":
		extract_tar()
		execute_java(war_home, project_name)

	# ?���? ?��?��?��
	if mode == "release":
		restart_tomcat()

	# thread sleep
	time.sleep(10)


# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ?��?��미터 체크
	argument_len = len(sys.argv)
	if argument_len < 2:
		release_help()

	# ?��?��미터 추출
	param_map = get_param_data(sys.argv[1])
	profile_active = param_map.get("profile_active")
	gportal_path = param_map.get("gportal_path")
	java_home = param_map.get("java_home")
	war_home = param_map.get("war_home")
	tar_path = param_map.get("tar_path")    # op망을 ?��?��?�� 망에?���? ?��?��
	mode = param_map.get("mode")

	project_names = param_map.get("project_name").split(",")
	for project_name in project_names:

		# webappspath ?��?��?���?
		if profile_active == "op":
			webappspath = gportal_path + "/" + project_name + "/webapps/ROOT"
		elif profile_active is not "op":
			webappspath = gportal_path + "/" + project_name + "/tomcat/webapps/ROOT"

		# 배포
		release()



