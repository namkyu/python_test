#!/usr/bin/python
# -*- coding: utf-8 -*-


files = ["a.jsp", "b.jsp"]

for idx, fileName in enumerate(files):
	print(idx, fileName)

selected = raw_input("중복 ?��?��?�� 존재?��?��?��. 배포?�� ?��?��?�� ?��?��?�� 주세?��. (번호 ?��?��) ==> ")
print(selected)

#print (files[int(selected)])

print (files[0])
