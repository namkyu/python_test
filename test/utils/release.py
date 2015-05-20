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
	print("??Όλ―Έν° ?? ? λ³?")
	print("===============================================================")
	print("profile_active : ?κ²? ? λ³? ?? (op, rc, stage, live)")
	print("project_name : ?λ‘μ ?Έ ?΄λ¦?")
	print("gportal_path : GPortal ?? ? λ¦? ?¨?€")
	print("war_home : λ°°ν¬?  warκ°? μ‘΄μ¬?? ?? ? λ¦?")
	print("tar_path : warλ₯? ?μΆν ??? tar.gz κ²½λ‘")
	print("mode : λ°°ν¬ λ°©λ²")
	sys.exit()  # κ°μ  μ’λ£

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
# ?°μΌ? ??
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
# ?°μΌ? μ€μ?
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
# ?°μΌ? ?¬??
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
# tar ?μΆ? ?΄? 
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
# λ°°ν¬
# ===========================================
def release():

	# ?? ? λ¦? ?­? , ??±
	if mode == "release":
		if os.path.exists(webappspath):
			shutil.rmtree(webappspath)
		os.makedirs(webappspath)

	# ?? ? λ¦? ?΄?
	print os.getcwd()
	os.chdir(webappspath)

	# λ§? λ³? war ?μΆ? ??κΈ?
	if profile_active == "op":
		op_war_path = war_home % project_name
		execute_java(op_war_path, project_name)
	elif profile_active is not "op":
		extract_tar()
		execute_java(war_home, project_name)

	# ?°μΌ? ?¬??
	if mode == "release":
		restart_tomcat()

	# thread sleep
	time.sleep(10)


# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ??Όλ―Έν° μ²΄ν¬
	argument_len = len(sys.argv)
	if argument_len < 2:
		release_help()

	# ??Όλ―Έν° μΆμΆ
	param_map = get_param_data(sys.argv[1])
	profile_active = param_map.get("profile_active")
	gportal_path = param_map.get("gportal_path")
	java_home = param_map.get("java_home")
	war_home = param_map.get("war_home")
	tar_path = param_map.get("tar_path")    # opλ§μ ? ?Έ? λ§μ?λ§? ?¬?©
	mode = param_map.get("mode")

	project_names = param_map.get("project_name").split(",")
	for project_name in project_names:

		# webappspath ?? ? λ¦?
		if profile_active == "op":
			webappspath = gportal_path + "/" + project_name + "/webapps/ROOT"
		elif profile_active is not "op":
			webappspath = gportal_path + "/" + project_name + "/tomcat/webapps/ROOT"

		# λ°°ν¬
		release()



