from random import randrange

class DrunkPerson(object):
	location = 0
	def __init__(self, id, start):
		self.id = id
		self.start = start
		self.location = 0
	def move(self, id):
		distance = randrange(2)
		if distance == 0:
			distance = -1
		self.id = id
		self.location += distance

DrunkGroup = []
i = 0
max_location = 0
while max_location < 20:
	max_location = 0
	DrunkGroup.append(DrunkPerson(i, i))
	j = 0
	while j < i:
		DrunkGroup[j].move(j)
		print("%i is at %i" % (DrunkGroup[j].id, DrunkGroup[j].location))
		if DrunkGroup[j].location > max_location:
			max_location = DrunkGroup[j].location
		if DrunkGroup[j].location == 20:
			finisher = DrunkGroup[j].id
			finisher_start = DrunkGroup[j].start
			break
		j += 1
	i += 1

print("Drunk #%i finished in %i turns. This is a total of %i turns" % (DrunkGroup[j].id, i, i - DrunkGroup[j].start))