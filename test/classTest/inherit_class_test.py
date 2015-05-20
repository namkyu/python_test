# -*- coding: utf-8 -*-

class Parent:
	parentAttr = 100
	__private_parent_attr = 200 # private 멤버 변수

	def __init__(self):
		print("Calling parent constructor")

	def parentMethod(self):
		print("Calling parent method")

	def setAttr(self, attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print "Parent attribute : ", Parent.parentAttr


class Child(Parent):

	def __init__(self):
		print("Calling child constructor")

	def __str__(self):
		return "Calling child toString"

	def childMethod(self):
		print("Calling child method")

	def __add__(self, other):
		return "__add__ tesst"


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(300)
c.getAttr()
print str(c)


print c + "test11"
