import ui
import Person
import BFT

gui = ui
Persons = []
selectedPerson = Person.Person('','',0,'w')

def ceiling(x):
	n = int(x)
	return n if n-1 < x <= n else n+1

def newPerson(sender):
	'@type sender: ui.Button'
	gender = 'm'
	if sender.superview['genderCtrl'].selected_index is 1:
		gender = 'w'
		
	firstName = sender.superview['firstNameTxt'].text
	lastName = sender.superview['lastNameTxt'].text
	age = int(float(sender.superview['ageTxt'].text))
	Persons.append(Person.Person(firstName, lastName, age, gender))
	
	sender.superview['firstNameTxt'].text = ''
	sender.superview['lastNameTxt'].text = ''
	sender.superview['ageTxt'].text = ''
	sender.superview['genderCtrl'].selected_index = 0

def newAbnahme(sender):
	main = gui.load_view('neueAbnahme')
	selectedPerson = Persons[0]
	main['PersonLbl'].text = selectedPerson.firstName + ', ' + selectedPerson.lastName
	main.present('sheet')

def selectPerson(sender):
	main = gui.load_view('personWaehlen')
	personStrings = []
	for person in Persons:
		personStrings.append(person.firstName + ', ' + person.lastName)
	main['persons'].data_source(ui.ListDataSource(items=personStrings))
	main.present('sheet')

def newBFT(sender):
	bft = BFT.BFT(int(sender.superview['timeSprint'].text),  int(sender.superview['timeKlimm'].text), int(sender.superview['time1000m'].text), selectedPerson)

	bft.getPunkte(sender)
	bft.getNoten(sender)

if not Persons:
	gui.load_view('neuePerson').present('sheet')
else:
	gui.load_view('neueAbnahme').present('sheet')
