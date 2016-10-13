#!/usr/bin/env python3

class Person:

	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, age):
		self._age = age

	@property
	def sex(self):
		return self._sex

	@sex.setter
	def sex(self, sex):
		self._sex = sex

	def __str__(self):
		return self.name + " : " + str(self.age) + " year old " + self.sex

p1 = Person("Michael", 45, "M")
print(p1)


