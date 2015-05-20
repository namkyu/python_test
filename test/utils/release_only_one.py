#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys


def release_help():
	print("===============================================================")
	print("?ŒŒ?¼ë¯¸í„° ?…‹?Œ… ? •ë³?")
	print("===============================================================")
	print("1 ë²ˆì§¸ ?ŒŒ?¼ë¯¸í„° : ?”„ë¡œì ?Š¸ ?´ë¦?")
	print("2 ë²ˆì§¸ ?ŒŒ?¼ë¯¸í„° : ?ŒŒ?¼ëª?")
	print("3 ë²ˆì§¸ ?ŒŒ?¼ë¯¸í„° : ?„œë²„ë¦¬?Š¤?Š¸file")
	sys.exit()  # ê°•ì œ ì¢…ë£Œ

# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ?ŒŒ?¼ë¯¸í„° ì²´í¬
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
	print("ë°°í¬ ???ƒ ?ŒŒ?¼")
	print("========================================================================")
	for root, dirs, files in os.walk("/home/fxdev/GPORTAL/%s/tomcat/webapps/ROOT" % project, topdown=False):
		for name in files:
			# ê²??ƒ‰?•˜? ¤ê³? ?•˜?Š” file?˜ full path ì¶”ì¶œ
			if name == file_name:
				search_file_full_path = os.path.join(root, name)
				release_files.append(search_file_full_path)
				print("ë°°í¬ ???ƒ ?ŒŒ?¼ ==> " + search_file_full_path)
	print("\n")

	release_files_size = len(release_files)
	release_file_name = ""

	# ë°°í¬ ?ŒŒ?¼?´ ì¡´ì¬?•˜ì§? ?•Š?œ¼ë©? ê°•ì œ ì¢…ë£Œ
	if release_files_size == 0:
		print("========================================================================")
		print("ë°°í¬?•  ?ŒŒ?¼?´ ì¡´ì¬?•˜ì§? ?•Š?Šµ?‹ˆ?‹¤. ")
		print("========================================================================")
		print("(project=%s, file_name=%s)" % (project, file_name))
		sys.exit()
	# ë°°í¬?•  ?ŒŒ?¼?´ 1ê±?
	elif release_files_size == 1:
		release_file_name = release_files[0]
	# ë°°í¬?•  ?ŒŒ?¼?´ 1ê±? ?´?ƒ?´ë©? ?‚¬?š©?ê°? ?„ ?ƒ ê°??Š¥?•˜ê²? ?„¤? •
	elif release_files_size > 1:
		for idx, file_name in enumerate(release_files):
			print(idx, file_name)
		print("========================================================================")
		selected_file_num = raw_input("ì¤‘ë³µ ?ŒŒ?¼?´ ì¡´ì¬?•©?‹ˆ?‹¤. ë°°í¬?•  ?ŒŒ?¼?„ ?„ ?ƒ?•´ ì£¼ì„¸?š”. (ë²ˆí˜¸ ?…? ¥) ==> ")
		print("========================================================================")
		release_file_name = release_files[int(selected_file_num)]

	# ?„œë²? ë¦¬ìŠ¤?Š¸ ? •ë³? ì¶”ì¶œ
	server_list_info = open("/home/fxdev/shell/serverlist/%s" % server_list_file)
	for server_host in server_list_info:
		# scpë¥? ?´?š©?•œ ?ŒŒ?¼ cp
		cmd = "scp %s %s:%s" % (release_file_name, server_host.strip(), release_file_name)
		print(cmd)
		subprocess.call(cmd, shell=True)

	# close file
	server_list_info.close()