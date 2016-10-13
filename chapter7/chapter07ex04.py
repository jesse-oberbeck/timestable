#!/usr/bin/env python3

class Worker():

	def __init__(self, name, salary, years):
		self.name = name
		self.salary = salary
		self.years = years

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name


	def pension(self):
		amount = (int(self.salary) * .1) * int(self.years)
		return amount

class Manager(Worker):
	
	def pension(self):
		amount = (int(self.salary) * .2) * int(self.years)
		return amount

class Executive(Manager):

	def pension(self):
		amount = (int(self.salary) * .3) * int(self.years)
		return amount


w1 = Worker("Jimothy",10000,8)
m1 = Manager("Roderick", 15000, 15)
e1 = Executive("Hubert",15000,15)
print(w1.pension(), m1.pension(), e1.pension())


