#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys


# ===========================================
# help
# ===========================================
def release_help():
	print("===============================================================")
	print("?��?��미터 ?��?�� ?���?")
	print("===============================================================")
	print("1 번째 ?��?��미터 : command")

	if command == "find":
		print("2 번째 ?��?��미터 : �??�� ?��?��?���? �??��")
		print("3 번째 ?��?��미터 : �??�� ?��?�� ?���?")

	sys.exit()  # 강제 종료


# ===========================================
# find
# ===========================================
def find():
	argument_len = len(params)
	if argument_len != 3:
		release_help()
	search_parent_dir = params[1]
	search_file = params[2]

	for root, dirs, files in os.walk(search_parent_dir, topdown=False):
		for name in files:
			if name == search_file:
				search_file_full_path = os.path.join(root, name)
				print(search_file_full_path)


# ===========================================
# execute
# ===========================================
if __name__ == "__main__":

	# ?��?��미터 ?��?��
	params = []
	for idx, arg in enumerate(sys.argv):
		if idx != 0:
			params.append(arg)

	# ?��?�� �??��
	command = params[0]
	if command == "find":
		find()