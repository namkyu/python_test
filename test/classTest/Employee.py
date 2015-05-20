# -*- coding: utf-8 -*-

class Employee:

	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name : ", self.name, ", Salary : ", self.salary

	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"


emp1 = Employee("nklee", 1000)
emp2 = Employee("nklee2", 2000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.age = 33
print "age :", emp1.age


del emp1.age
if hasattr(emp1, "age"):
	print "age :", emp1.age
else:
	print "Employee instance has no attribute"


print "__doc__ ==>", Employee.__doc__
print "__name__ ==>", Employee.__name__
print "__module__ ==>", Employee.__module__
print "__bases__ ==>", Employee.__bases__
print "__dict__ ==>", Employee.__dict__

## destroyed test
print("")
del emp1
del emp2



