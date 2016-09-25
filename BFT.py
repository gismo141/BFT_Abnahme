import Person.py

class BFT (object):
	def __init__(self, zs, zk, z1000m, person):
		self.zeitSprint = zs
		self.zeitKlimm = zk
		self.zeit1000m = z1000m
		if int(person.age) > 35:
			self.faktorAlter = (int(age) - 35) * 0.005
		else:
			self.faktorAlter = 1
		if person.gender is 'w':
			self.faktorKlimm = 1.4
			self.faktorSprint = 1.15
			self.faktor1000m = 1.15
		else:
			self.faktorKlimm = 1
			self.faktorSprint = 1
			self.faktor1000m = 1
		self.punkteSprint = ((1100 - 16.667 * self.zeitSprint) * self.faktorAlter) * self.faktorSprint
		self.punkteKlimm = ((75 + 5 * self.zeitKlimm) * self.faktorAlter) * self.faktorKlimm
		self.punkte1000m = ((100 + ((390 - self.zeit1000m) * 1.81818181)) * self.faktorAlter) * self.faktor1000m
		self.noteSprint = 5.49 - (self.punkteSprint * 0.01)
		self.noteKlimm = 5.49 - (self.punkteKlimm * 0.01)
		self.note1000m = 5.49 - (self.punkte1000m * 0.01)
		self.noteGesamt = (self.noteSprint + self.noteKlimm + self.note1000m) / 3
	
	def getPunkte(self):
		print("Punkte")
		print("\tKlimmhang: " + str(self.punkteKlimm))
		print("\tSprint: " + str(self.punkteSprint))
		print("\t1000m: " + str(self.punkte1000m))
		
	def getNoten(self, sender):
		'@type sender: ui.Button'
		print("Note")
		print("\tKlimmhang: " + str(self.noteKlimm))
		print("\tSprint: " + str(self.noteSprint))
		print("\t1000m: " + str(self.note1000m))
		print("\nGesamt: " + str(self.noteGesamt))
		
		sender.superview['noteSprint'].text = str(self.noteSprint)
		sender.superview['noteKlimm'].text = str(self.noteKlimm)
		sender.superview['note1000m'].text = str(self.note1000m)
		sender.superview['noteGesamt'].text = str(self.noteGesamt)
