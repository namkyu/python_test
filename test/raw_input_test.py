#!/usr/bin/python
# -*- coding: utf-8 -*-


files = ["a.jsp", "b.jsp"]

for idx, fileName in enumerate(files):
	print(idx, fileName)

selected = raw_input("μ€λ³΅ ??Ό?΄ μ‘΄μ¬?©??€. λ°°ν¬?  ??Ό? ? ??΄ μ£ΌμΈ?. (λ²νΈ ?? ₯) ==> ")
print(selected)

#print (files[int(selected)])

print (files[0])
