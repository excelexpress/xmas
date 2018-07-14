import random

class Person():
	def __init__(self, name):
		self.name = name
		self.eligible_people = []
		self.ineligible_people = [self] #can't have oneself
		self.assignedperson = None
	
	def addPerson(self, Person):
		#add eligible person to eligible people list
		if Person in self.ineligible_people:
			#do nothing if already defined as an ineligible match
			pass
		elif Person in self.eligible_people:
			#do nothing if person is already in eligible people list
			pass
		else:
			self.eligible_people.append(Person)
	
	def removePerson(self, Person):
		if Person in self.ineligible_people:
			#don't add to ineligible people list if already in it
			pass
		else:
			self.ineligible_people.append(Person)
		
		if Person in self.eligible_people:
			self.eligible_people.remove(Person)
	
	def addPeople(self, PeopleArray):
		#note: won't add people that are previously defined as ineligible
		for person in PeopleArray:
			self.addPerson(person)
	
	def removePeople(self, PeopleArray):
		for person in PeopleArray:
			self.removePerson(person)
	
	def drawName(self):
		if len(self.eligible_people) > 0:
			index = random.randint(0,len(self.eligible_people)-1)
			self.assignedperson = self.eligible_people[index]
		else:
			print(f"No eligible people left for {self.name}")