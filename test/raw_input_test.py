#!/usr/bin/python
# -*- coding: utf-8 -*-


files = ["a.jsp", "b.jsp"]

for idx, fileName in enumerate(files):
	print(idx, fileName)

selected = raw_input("중복 파일이 존재합니다. 배포할 파일을 선택해 주세요. (번호 입력) ==> ")
print(selected)

#print (files[int(selected)])

print (files[0])
