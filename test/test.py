# -*- coding: utf-8 -*-

import os
import shutil
import tarfile


# ??Όλ―Έν° ??±
parameter_map = {}
parameter_str = "a=1 b=2 c=3"
parameters = parameter_str.split(" ")
print(parameters)

for item in parameters:
	print(item)
	items = item.split("=")
	parameter_map[items[0]] = items[1]

print(parameter_map)
print(parameter_map.get('a'))


# tar.gz ?μΆ? ??κΈ?
print os.getcwd()
os.chdir("E:/test/python/tar")

tar = tarfile.open("1111.tar.gz", "r:gz")
for item in tar:
	tar.extract(item, "E:/test/python/tar/test")
print("Done")



# if ??€?Έ
profile_active = "rc"
if profile_active == "op":
	print "op"
elif profile_active is not "op":
	print "rc"


# split ??€?Έ (?΅)
str = "1#2#3"
print(str.split("#"))


shutil.rmtree("E:/test/python/src_dir2")
shutil.copytree("E:/test/python/src_dir", "E:/test/python/src_dir2")


# ?? ? λ¦? ?¨?€ κ΅¬λΆ?? / λ‘? ?€?΄κ°??Ό ??€. \ ? ? ?¨
shutil.copy2("D:/goldensection.gso", "E:/test/python/backup_dir")