# -*- coding: utf-8 -*-

import os
import os
import pickle
import sys


print os.getcwd()
os.chdir("E:/test/python")
print os.getcwd()

# ?Έμ½λ© ??Έ ?κΈ?
print sys.getdefaultencoding()


print
print
print "========================================="
print "??Ό ?½κΈ? ??€?Έ"
print "========================================="

# ??Ό ?€? ? ? μ€? ?½κΈ?
data = open("test1.txt")
print data.readline()

# ??Ό μ²? λ²μ§Έ rowλ‘? ?¬?Έ?Έ ?΄?
data.seek(0)
for each_item in data:
	print each_item,
data.close()

print
print
print "========================================="
print "split ??€?Έ"
print "========================================="


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
print "exception ??€?Έ"
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
print "??Ό ?°κΈ? ??€?Έ"
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

# print ?΄?©? ??Ό? ?°κΈ?, finally ??€?Έ
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
print "file with as ?¬?©?κΈ?"
print "========================================="
try:
	with open("its.txt", "w") as data4:
		print(data4)
except IOError as err:
	print "File error ==>" + str(err)



print
print
print "========================================="
print "pickle ??€?Έ"
print "========================================="


try:
	# wb ? ?λ―Έλ writeable, binary ?΄?€.
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
print "??€?Έ"
print "========================================="
mins = [1, 2, 3]
secs = [m * 60 for m in mins]  # for λ¬? ??΄ ? μ€? μ½λλ‘λ κ°??₯
print(secs)
print(secs[0:2])


print
print
print "========================================="
print "μ€λ³΅ ? κ±?"
print "========================================="
distances = set()
distances = {1, 2, 3, 4, 5, 1, 3}
print(distances)


