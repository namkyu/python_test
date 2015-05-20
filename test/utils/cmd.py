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
	print("??Όλ―Έν„° ?…‹?… ? •λ³?")
	print("===============================================================")
	print("1 λ²μ§Έ ??Όλ―Έν„° : command")

	if command == "find":
		print("2 λ²μ§Έ ??Όλ―Έν„° : κ²??ƒ‰ ?””? ‰?† λ¦? μ§?? •")
		print("3 λ²μ§Έ ??Όλ―Έν„° : κ²??ƒ‰ ??Ό ?΄λ¦?")

	sys.exit()  # κ°•μ  μΆ…λ£


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

	# ??Όλ―Έν„° ?…‹?…
	params = []
	for idx, arg in enumerate(sys.argv):
		if idx != 0:
			params.append(arg)

	# ??Ό κ²??ƒ‰
	command = params[0]
	if command == "find":
		find()