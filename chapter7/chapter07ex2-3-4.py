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

class Family:
	def __init__(self, parent1, parent2, children):
		self.parent1 = parent1
		self.parent2 = parent2
		self.children = children

	def __str__(self):
		return self.parent1.name +", "+ self.parent2.name +", "+" ".join(self.children)

	def add(self,child):
		self.children.append(child)

	def __eq__(self,value):
		return len(self.children) == len(value.children)

	def __ge__(self,value):
		return len(self.children) >= len(value.children)

	def __gt__(self,value):
		return len(self.children) > len(value.children)

	def __le__(self,value):
		return len(self.children) <= len(value.children)

	def __lt__(self,value):
		return len(self.children) < len(value.children)

	@property
	def parent1(self):
		return self._parent1

	@parent1.setter
	def parent1(self, parent1):
		self._parent1 = parent1

	@property
	def parent2(self):
		return self._parent2

	@parent2.setter
	def parent2(self, parent2):
		self._parent2 = parent2

	@property
	def children(self):
		return self._children

	@children.setter
	def children(self, children):
		self._children = children


p1 = Person("Michael", 45, "M")
p2 = Person("Jane", 43, "M")
children = ["Bimmy", "Jimmy"]
f1 = Family(p1,p2,children)
f1.add("Bob")

p3 = Person("Jim", 905, "Lemon")
p4 = Person("Betty", 68, "Dinosaur")
f2 = Family(p3,p4,["Dave"])
f2.add("Gerald")
f2.add("Arnold")
print(f1)
#print(p1)
print(f2)
if f1==f2:
	print("Equal")
elif f1 > f2:
	print("f1 is greater")
elif f1 < f2:
	print("f2 is greater")
else:
	print("banana")


