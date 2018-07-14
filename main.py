from person import Person

#Create blank family members (names only)
wally = Person("Wally")
jovan = Person("Jovan")
jonna = Person("Jonna")
jorge = Person("Jorge")
delcie = Person("Delcie")
lee = Person("Lee")
simona = Person("Simona")
kylee = Person("Kylee")
rosalie = Person("Rosalie")

#Create list of family members
family = [wally, jovan, jonna, jorge, delcie, lee, simona, kylee, rosalie]

#define eligible people list for each person
for member in family:
	member.addPeople(family)

#define ineligible matches
wally.removePerson(jovan)
jovan.removePerson(wally)
wally.removePerson(jonna)
jonna.removePerson(wally)
delcie.removePerson(lee)
lee.removePerson(delcie)


#sort family members by number of elible matches
family.sort(key=lambda t: len(t.eligible_people))

#Print eligible matches for each person
for member in family:
	print()
	print(f"{member.name}'s eligible matches are:")
	for person in member.eligible_people:
		print(f"  {person.name}")

print()
print("Results are:")
for member in family:
	member.drawName()
	print(f"  {member.name} has {member.assignedperson.name}")
	
	#remove drawn member from each family member's eligible people list after picking
	for fam_member in family:
		fam_member.removePerson(member.assignedperson)





