# -*- coding: utf-8 -*-

class ListClassTest(list):
	def __init__(self, a_name=""):
		list.__init__([])
		self.name = a_name


a = ListClassTest("AAA")
type(a)