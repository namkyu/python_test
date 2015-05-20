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
	print("?åå?ùºÎØ∏ÌÑ∞ ?Öã?åÖ ?†ïÎ≥?")
	print("===============================================================")
	print("profile_active : ?ôòÍ≤? ?†ïÎ≥? ?Öã?åÖ (op, rc, stage, live)")
	print("project_name : ?îÑÎ°úÏ†ù?ä∏ ?ù¥Î¶?")
	print("gportal_path : GPortal ?îî?†â?Ü†Î¶? ?å®?ä§")
	print("war_home : Î∞∞Ìè¨?ï† warÍ∞? Ï°¥Ïû¨?ïò?äî ?îî?†â?Ü†Î¶?")
	print("tar_path : warÎ•? ?ïïÏ∂ïÌïú ?ÉÅ?Éú?ùò tar.gz Í≤ΩÎ°ú")
	print("mode : Î∞∞Ìè¨ Î∞©Î≤ï")
	sys.exit()  # Í∞ïÏ†ú Ï¢ÖÎ£å

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
# ?Ü∞Ïº? ?ãú?ûë
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
# ?Ü∞Ïº? Ï§ëÏ?
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
# ?Ü∞Ïº? ?û¨?ãú?ûë
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
# tar ?ïïÏ∂? ?ï¥?†ú
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
# Î∞∞Ìè¨
# ===========================================
def release():

	# ?îî?†â?Ü†Î¶? ?Ç≠?†ú, ?Éù?Ñ±
	if mode == "release":
		if os.path.exists(webappspath):
			shutil.rmtree(webappspath)
		os.makedirs(webappspath)

	# ?îî?†â?Ü†Î¶? ?ù¥?èô
	print os.getcwd()
	os.chdir(webappspath)

	# Îß? Î≥? war ?ïïÏ∂? ??Í∏?
	if profile_active == "op":
		op_war_path = war_home % project_name
		execute_java(op_war_path, project_name)
	elif profile_active is not "op":
		extract_tar()
		execute_java(war_home, project_name)

	# ?Ü∞Ïº? ?û¨?ãú?ûë
	if mode == "release":
		restart_tomcat()

	# thread sleep
	time.sleep(10)


# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ?åå?ùºÎØ∏ÌÑ∞ Ï≤¥ÌÅ¨
	argument_len = len(sys.argv)
	if argument_len < 2:
		release_help()

	# ?åå?ùºÎØ∏ÌÑ∞ Ï∂îÏ∂ú
	param_map = get_param_data(sys.argv[1])
	profile_active = param_map.get("profile_active")
	gportal_path = param_map.get("gportal_path")
	java_home = param_map.get("java_home")
	war_home = param_map.get("war_home")
	tar_path = param_map.get("tar_path")    # opÎßùÏùÑ ?†ú?ô∏?ïú ÎßùÏóê?ÑúÎß? ?Ç¨?ö©
	mode = param_map.get("mode")

	project_names = param_map.get("project_name").split(",")
	for project_name in project_names:

		# webappspath ?îî?†â?Ü†Î¶?
		if profile_active == "op":
			webappspath = gportal_path + "/" + project_name + "/webapps/ROOT"
		elif profile_active is not "op":
			webappspath = gportal_path + "/" + project_name + "/tomcat/webapps/ROOT"

		# Î∞∞Ìè¨
		release()



