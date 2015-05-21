#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess


def release_help():
	print("===============================================================")
	print("�Ķ���� ���� ����")
	print("===============================================================")
	print("1 ��° �Ķ���� : ������Ʈ �̸�")
	print("2 ��° �Ķ���� : ���ϸ�")
	print("3 ��° �Ķ���� : ��������Ʈfile")
	sys.exit()  # ���� ����

# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# �Ķ���� üũ
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
	print("���� ��� ����")
	print("========================================================================")
	for root, dirs, files in os.walk("/home/fxdev/GPORTAL/%s/tomcat/webapps/ROOT" % project, topdown=False):
		for name in files:
			# �˻��Ϸ��� �ϴ� file�� full path ����
			if name == file_name:
				search_file_full_path = os.path.join(root, name)
				release_files.append(search_file_full_path)
				print("���� ��� ���� ==> " + search_file_full_path)
	print("\n")

	release_files_size = len(release_files)
	release_file_name = ""

	# ���� ������ �������� ������ ���� ����
	if release_files_size == 0:
		print("========================================================================")
		print("������ ������ �������� �ʽ��ϴ�. ")
		print("========================================================================")
		print("(project=%s, file_name=%s)" % (project, file_name))
		sys.exit()
	# ������ ������ 1��
	elif release_files_size == 1:
		release_file_name = release_files[0]
	# ������ ������ 1�� �̻��̸� ����ڰ� ���� �����ϰ� ����
	elif release_files_size > 1:
		for idx, file_name in enumerate(release_files):
			print(idx, file_name)
		print("========================================================================")
		selected_file_num = raw_input("�ߺ� ������ �����մϴ�. ������ ������ ������ �ּ���. (��ȣ �Է�) ==> ")
		print("========================================================================")
		release_file_name = release_files[int(selected_file_num)]

	# ���� ����Ʈ ���� ����
	server_list_info = open("/home/fxdev/shell/serverlist/%s" % server_list_file)
	for server_host in server_list_info:
		# scp�� �̿��� ���� cp
		cmd = "scp %s %s:%s" % (release_file_name, server_host.strip(), release_file_name)
		print(cmd)
		subprocess.call(cmd, shell=True)

	# close file
	server_list_info.close()