#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys


def release_help():
	print("===============================================================")
	print("?��?��미터 ?��?�� ?���?")
	print("===============================================================")
	print("1 번째 ?��?��미터 : ?��로젝?�� ?���?")
	print("2 번째 ?��?��미터 : ?��?���?")
	print("3 번째 ?��?��미터 : ?��버리?��?��file")
	sys.exit()  # 강제 종료

# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ?��?��미터 체크
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
	print("배포 ???�� ?��?��")
	print("========================================================================")
	for root, dirs, files in os.walk("/home/fxdev/GPORTAL/%s/tomcat/webapps/ROOT" % project, topdown=False):
		for name in files:
			# �??��?��?���? ?��?�� file?�� full path 추출
			if name == file_name:
				search_file_full_path = os.path.join(root, name)
				release_files.append(search_file_full_path)
				print("배포 ???�� ?��?�� ==> " + search_file_full_path)
	print("\n")

	release_files_size = len(release_files)
	release_file_name = ""

	# 배포 ?��?��?�� 존재?���? ?��?���? 강제 종료
	if release_files_size == 0:
		print("========================================================================")
		print("배포?�� ?��?��?�� 존재?���? ?��?��?��?��. ")
		print("========================================================================")
		print("(project=%s, file_name=%s)" % (project, file_name))
		sys.exit()
	# 배포?�� ?��?��?�� 1�?
	elif release_files_size == 1:
		release_file_name = release_files[0]
	# 배포?�� ?��?��?�� 1�? ?��?��?���? ?��?��?���? ?��?�� �??��?���? ?��?��
	elif release_files_size > 1:
		for idx, file_name in enumerate(release_files):
			print(idx, file_name)
		print("========================================================================")
		selected_file_num = raw_input("중복 ?��?��?�� 존재?��?��?��. 배포?�� ?��?��?�� ?��?��?�� 주세?��. (번호 ?��?��) ==> ")
		print("========================================================================")
		release_file_name = release_files[int(selected_file_num)]

	# ?���? 리스?�� ?���? 추출
	server_list_info = open("/home/fxdev/shell/serverlist/%s" % server_list_file)
	for server_host in server_list_info:
		# scp�? ?��?��?�� ?��?�� cp
		cmd = "scp %s %s:%s" % (release_file_name, server_host.strip(), release_file_name)
		print(cmd)
		subprocess.call(cmd, shell=True)

	# close file
	server_list_info.close()