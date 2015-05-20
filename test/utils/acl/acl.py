#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess


# copy ??Ό
copy_file_name = ["ACL_CHECK_SERVER_LIST.txt", "check_network.py"]

# ?Έ?€?Έ ?λ²? ? λ³? μΆμΆ
server_list_info = open("HOST_SERVER_LIST.txt")

# script ???₯ dir
script_home_dir = "/home/nklee/"

# ??Ό ? ?¬
for server_host in server_list_info:
	for send_file in copy_file_name:
		# ??Ό ???₯ ?? ? λ¦? ??±
		arg = 'mkdir -p %s' % script_home_dir
		mkdirCmd = "ssh %s '%s'" % (server_host.strip(), arg)
		subprocess.call(mkdirCmd, shell=True)

		# scpλ₯? ?΄?©? ??Ό cp
		cmd = "scp %s %s:%s" % (send_file, server_host.strip(), script_home_dir + send_file)
		subprocess.call(cmd, shell=True)
print("===========================================")
print("File Sent Done!!")
print("===========================================")

# ?κ²©μ? ??΄?¬ script ?€?
server_list_info.seek(0)
for server_host in server_list_info:
	arg = "'cd %s; python check_network2.py'" % script_home_dir
	cmd = "ssh %s %s" % (server_host.strip(), arg)
	subprocess.call(cmd, shell=True)
print("===========================================")
print("ACL Check Done!!")
print("===========================================")