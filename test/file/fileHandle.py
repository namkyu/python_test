# -*- coding: utf-8 -*-

import os
print os.getcwd()
os.chdir("E:/test/python")
print os.getcwd()

# 인코딩 확인 하기
import sys
print sys.getdefaultencoding()


print
print
print "========================================="
print "파일 읽기 테스트"
print "========================================="

# 파일 오픈 후 한 줄 읽기
data = open("test1.txt")
print data.readline()

# 파일 첫 번째 row로 포인트 이동
data.seek(0)
for each_item in data:
	print each_item,
data.close()

print
print
print "========================================="
print "split 테스트"
print "========================================="

import os

if os.path.exists("test3.txt"):
	data3 = open("test3.txt")
	for each_line in data3:
		try:
			if not each_line.find(":") == -1:
				(num, text) = each_line.split(":", 1)
				print("num : " + num + ", text : " + text),
		except:
			pass
	data3.close()
else:
	print "The data file is missing!"

print
print
print "========================================="
print "exception 테스트"
print "========================================="

try:
	data3 = open("test31.txt")
	for each_line in data3:
		try:
			if not each_line.find(":") == -1:
				(num, text) = each_line.split(":", 1)
				print("num : " + num + ", text : " + text),
		except:
			pass
	data3.close()
except IOError as ex:
	print "The data file is missing"
except Exception:
	print "internal code error"



print
print
print "========================================="
print "파일 쓰기 테스트"
print "========================================="

man = []
other = []

try:
	data3 = open("test3.txt")
	#data3 = open("test311.txt")
	for each_line in data3:
		try:
			if not each_line.find(":") == -1:
				(num, text) = each_line.split(":", 1)
				num = num.strip()
				if num == 'man':
					man.append(text)
				elif num == 'other':
					other.append(text)
		except:
			pass

except IOError as ex:
	print "The data file is missing! ==>" + str(ex)

finally:
	if 'data3' in locals():
		data3.close()

print(man)
print(other)

# print 내용을 파일에 쓰기, finally 테스트
try:
	out = open("data_out.txt", "w")
	print >> out, man
	print >> out, other

except IOError:
	print "IO error"

finally:
	if out in locals():
		out.close()


print
print
print "========================================="
print "file with as 사용하기"
print "========================================="
try:
	with open("its.txt", "w") as data4:
		print(data4)
except IOError as err:
	print "File error ==>" + str(err)



print
print
print "========================================="
print "pickle 테스트"
print "========================================="

import pickle

try:
	# wb 의 의미는 writeable, binary 이다.
	with open("pickle_mydata.txt", "wb") as mysavedata:
		pickle.dump([1, 2, 'three'], mysavedata)

	with open("pickle_mydata.txt", "rb") as myrestoredata:
		select_my_save_data = pickle.load(myrestoredata)
		print(select_my_save_data)

except IOError as err:
	print "File error ==>" + str(err)
except pickle.PickleError as perr:
	print "Pickling error ==>" + str(perr)


print
print
print "========================================="
print "테스트"
print "========================================="
mins = [1, 2, 3]
secs = [m * 60 for m in mins]  # for 문 없이 한 줄 코드로도 가능
print(secs)
print(secs[0:2])


print
print
print "========================================="
print "중복 제거"
print "========================================="
distances = set()
distances = {1, 2, 3, 4, 5, 1, 3}
print(distances)


import socket
print(socket.gethostname())
