# -*- coding: utf-8 -*-

class Athlete:

	def __init__(self, a_name="", a_times=[]):
		## ?—¬ê¸°ì„œ ë©¤ë²„ ë³??ˆ˜ë¥? ?„ ?–¸?•´ ì£¼ëŠ” ê²ƒìž„
		self.name = a_name
		self.times = a_times

	def how_big(self):
		return (len(self.name))

	def add_time(self, time_value):
		self.times.append(time_value)

	def add_times(self, list_of_times):
		self.times.extend(list_of_times)

c = Athlete()
d = Athlete("i am nklee")
d.add_time("1")
d.add_times(["2", "3", "4"])

print(c)
print(d)
print(d.name)
print(d.times[0:3])


