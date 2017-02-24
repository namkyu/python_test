# -*- coding: utf-8 -*-

import shutil

# 파라미터 파싱
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


# tar.gz 압축 풀기
import tarfile
import os
print os.getcwd()
os.chdir("E:/test/python/tar")

tar = tarfile.open("1111.tar.gz", "r:gz")
for item in tar:
	tar.extract(item, "E:/test/python/tar/test")
print("Done")


# if 테스트
profile_active = "rc"
if profile_active == "op":
	print "op"
elif profile_active is not "op":
	print "rc"


# split 테스트 (샵)
str = "1#2#3"
print(str.split("#"))


shutil.rmtree("E:/test/python/src_dir2")
shutil.copytree("E:/test/python/src_dir", "E:/test/python/src_dir2")


# 디렉토리 패스 구분자는 / 로 들어가야 한다. \ 는 안 됨
shutil.copy2("D:/goldensection.gso", "E:/test/python/backup_dir")



# 디렉토리 삭제
shutil.rmtree("E:/test/war/test_dir", True)


print(os.pathsep)