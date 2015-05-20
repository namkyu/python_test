#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys


def release_help():
	print("===============================================================")
	print("??Όλ―Έν° ?? ? λ³?")
	print("===============================================================")
	print("1 λ²μ§Έ ??Όλ―Έν° : ?λ‘μ ?Έ ?΄λ¦?")
	print("2 λ²μ§Έ ??Όλ―Έν° : ??Όλͺ?")
	print("3 λ²μ§Έ ??Όλ―Έν° : ?λ²λ¦¬?€?Έfile")
	sys.exit()  # κ°μ  μ’λ£

# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ??Όλ―Έν° μ²΄ν¬
	argument_len = len(sys.argv)
	if argument_len != 4:
		release_help()

	project = sys.argv[1]
	file_name = sys.argv[2]
	server_list_file = sys.argv[3]
	release_files = []
	print("========================================================================")
	print("Argument Info")
	print("========================================================================")
	print("project=" + project + ", file_name=" + file_name + ", server_list_file=" + server_list_file)
	print("\n")

	print("========================================================================")
	print("λ°°ν¬ ??? ??Ό")
	print("========================================================================")
	for root, dirs, files in os.walk("/home/fxdev/GPORTAL/%s/tomcat/webapps/ROOT" % project, topdown=False):
		for name in files:
			# κ²???? €κ³? ?? file? full path μΆμΆ
			if name == file_name:
				search_file_full_path = os.path.join(root, name)
				release_files.append(search_file_full_path)
				print("λ°°ν¬ ??? ??Ό ==> " + search_file_full_path)
	print("\n")

	release_files_size = len(release_files)
	release_file_name = ""

	# λ°°ν¬ ??Ό?΄ μ‘΄μ¬?μ§? ??Όλ©? κ°μ  μ’λ£
	if release_files_size == 0:
		print("========================================================================")
		print("λ°°ν¬?  ??Ό?΄ μ‘΄μ¬?μ§? ??΅??€. ")
		print("========================================================================")
		print("(project=%s, file_name=%s)" % (project, file_name))
		sys.exit()
	# λ°°ν¬?  ??Ό?΄ 1κ±?
	elif release_files_size == 1:
		release_file_name = release_files[0]
	# λ°°ν¬?  ??Ό?΄ 1κ±? ?΄??΄λ©? ?¬?©?κ°? ? ? κ°??₯?κ²? ?€? 
	elif release_files_size > 1:
		for idx, file_name in enumerate(release_files):
			print(idx, file_name)
		print("========================================================================")
		selected_file_num = raw_input("μ€λ³΅ ??Ό?΄ μ‘΄μ¬?©??€. λ°°ν¬?  ??Ό? ? ??΄ μ£ΌμΈ?. (λ²νΈ ?? ₯) ==> ")
		print("========================================================================")
		release_file_name = release_files[int(selected_file_num)]

	# ?λ²? λ¦¬μ€?Έ ? λ³? μΆμΆ
	server_list_info = open("/home/fxdev/shell/serverlist/%s" % server_list_file)
	for server_host in server_list_info:
		# scpλ₯? ?΄?©? ??Ό cp
		cmd = "scp %s %s:%s" % (release_file_name, server_host.strip(), release_file_name)
		print(cmd)
		subprocess.call(cmd, shell=True)

	# close file
	server_list_info.close()