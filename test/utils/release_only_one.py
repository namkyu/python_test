#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess


def release_help():
	print("===============================================================")
	print("파라미터 셋팅 정보")
	print("===============================================================")
	print("1 번째 파라미터 : 프로젝트 이름")
	print("2 번째 파라미터 : 파일명")
	print("3 번째 파라미터 : 서버리스트file")
	sys.exit()  # 강제 종료

# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# 파라미터 체크
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
	print("배포 대상 파일")
	print("========================================================================")
	for root, dirs, files in os.walk("/home/fxdev/GPORTAL/%s/tomcat/webapps/ROOT" % project, topdown=False):
		for name in files:
			# 검색하려고 하는 file의 full path 추출
			if name == file_name:
				search_file_full_path = os.path.join(root, name)
				release_files.append(search_file_full_path)
				print("배포 대상 파일 ==> " + search_file_full_path)
	print("\n")

	release_files_size = len(release_files)
	release_file_name = ""

	# 배포 파일이 존재하지 않으면 강제 종료
	if release_files_size == 0:
		print("========================================================================")
		print("배포할 파일이 존재하지 않습니다. ")
		print("========================================================================")
		print("(project=%s, file_name=%s)" % (project, file_name))
		sys.exit()
	# 배포할 파일이 1건
	elif release_files_size == 1:
		release_file_name = release_files[0]
	# 배포할 파일이 1건 이상이면 사용자가 선택 가능하게 설정
	elif release_files_size > 1:
		for idx, file_name in enumerate(release_files):
			print(idx, file_name)
		print("========================================================================")
		selected_file_num = raw_input("중복 파일이 존재합니다. 배포할 파일을 선택해 주세요. (번호 입력) ==> ")
		print("========================================================================")
		release_file_name = release_files[int(selected_file_num)]

	# 서버 리스트 정보 추출
	server_list_info = open("/home/fxdev/shell/serverlist/%s" % server_list_file)
	for server_host in server_list_info:
		# scp를 이용한 파일 cp
		cmd = "scp %s %s:%s" % (release_file_name, server_host.strip(), release_file_name)
		print(cmd)
		subprocess.call(cmd, shell=True)

	# close file
	server_list_info.close()