# -*- coding: utf-8 -*-

######################################
# 리스트
######################################
names = ["a", "b", "c", "d"]
print names
print names[2]
names.append("appendText")
print names
names.insert(1, "insertText")
print names
print names[0:2]
print [1, 2, 3] + [4, 5]

empty_list = []
empty_list2 = list()
print empty_list
print empty_list2

f = open("E:/test/python_perfect_guide/list_test.txt")
lines = f.readlines()
f.close()
fvaluse = [float(line) for line in lines]
print "The minimum value is ", min(fvaluse)
print "The maximum value is ", max(fvaluse)


######################################
# 튜플
######################################

portfolio = []
for line in open("E:/test/python_perfect_guide/portfolio.csv"):
    fields = line.split(",")
    name = fields[0]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name, shares, price)
    portfolio.append(stock)
    
print portfolio[0]
print portfolio[5]


######################################
# 사전 (해시 테이블)
######################################
stock = {
    "name" : "GOOG",
    "shares" : 100,
    "price" : 490.10    
}

print stock["name"]
print stock.get("price", 0.0)
print stock.get("price1", 0.0)

keys = list(stock)
print keys


######################################
# for문
######################################
for c in "Hello World":
    print c
    
for name in ["Dave", "Mark", "Ann", "Phil"]:
    print name
    
for key in {"A" : 1111, "B" : 2222, "C" : 3333}:
    print key
    
server_info = {
    "1" : ["a", "b"], "2" : ["a", "b"], "3" : ["a", "b"]
}
print ("#####")
for key in server_info:
    print(key + " : " + str(server_info.get(key)))


######################################
# 생성기 (tail -f | grep nklee)
######################################

# import time
# 
# def tail(f):
#     f.seek(0, 2)
#     while True:
#         line = f.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         yield line
# 
# def grep(lines, searchText):
#     for line in lines:
#         if searchText in line: yield line
# 
# wwwlog = tail(open("E:/test/python_perfect_guide/access-log.txt"))
# pylines = grep(wwwlog, "nklee")
# for line in pylines:
#     print line
    

######################################
# 객체와 클래스
######################################

items = [1, 2]
print dir(items)
print items.append(3)
print items.__add__([4, 5])
print items.__add__([6])

# 파이썬에서는 괄호로 상속 관계를 기술한다. 모든 파이썬 타입의 루트은 object로부터 상속을 받는다.
# 각 메서드의 첫 번째 인수는 항상 객체 자기 자신을 가르킨다. 관습적으로 이 인수의 이름으로 self를 사용한다.
class Stack(object):
    # __init__ 은 객체가 생성된 후 초기화를 위해 사용한다.
    def __init__(self):
        self.stack = []
    def push(self, obj):
        self.stack.append(obj)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)

s = Stack()
s.push("Dave")
s.push(32)
s.push([3, 4, 5])
print s.pop()
print s.pop()
del s # s를 제거한다.

class EventHandler(object):
    # 정적 메서드
    @staticmethod
    def dipatcherThread():
        print "called dipatcherThread!!"

EventHandler.dipatcherThread()


######################################
# 예외
######################################

try :
    f = open("exception.txt", "r")
except IOError as e:
    print e
    
    
######################################
# 모듈
######################################
import div
print div.multiply(1, 20)

import div as test_div
print test_div.multiply(3, 4)

from div import multiply
print multiply(2, 3)

from div import *
print multiply(3, 3)


######################################
# 타입과 객체
######################################
a = 37
import sys
print "getrefcount : %d" % sys.getrefcount(a)

line = "GOOG, 100, 490.10"
field_types = [str, int, float]
raw_fields = line.split(",")
fields = [ty(val) for ty,val in zip(field_types, raw_fields)]
print fields

a = "Your name is {0} and your age is {age}"
print a.format("nklee", age=35)

class Foo(object):
    def instance_method(self, arg):
        return arg
    @classmethod
    def class_method(cls, arg):
        return arg
    @staticmethod
    def static_method(arg):
        return arg

f = Foo()
meth = f.instance_method
print meth(37)

umeth = Foo.instance_method
print umeth(f, 37)