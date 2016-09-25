class Person (object):
	def __init__(self, fn, ln, age, gen):
		self.firstName = fn
		self.lastName = ln
		self.age = age
		self.gender = gen

	def newPerson(sender):
		'@type sender: ui.Button'
		gender = 'm'
		if sender.superview['genderCtrl'].selected_index is 1:
		gender = 'w'
		firstName = sender.superview['firstNameTxt'].text
		lastName = sender.superview['lastNameTxt'].text
		age = sender.superview['ageTxt'].text
		Persons.append(Person(firstName, lastName, age, gender))
	
		sender.superview['firstNameTxt'].text = ''
		sender.superview['lastNameTxt'].text = ''
		sender.superview['ageTxt'].text = ''
		sender.superview['genderCtrl'].selected_index = 0
