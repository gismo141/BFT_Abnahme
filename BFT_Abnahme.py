import ui
import BFT.py

gui = ui
Persons = []

def ceiling(x):
    n = int(x)
    return n if n-1 < x <= n else n+1

def newAbnahme(sender):
	main = gui.load_view('neueAbnahme')
	personStrings = []
	for person in Persons:
		personStrings.append(person.firstName + ', ' + person.lastName)
	main['PersonLbl'].text = personStrings[0]
	main.present('sheet')

def selectPerson(sender):
	main = gui.load_view('personWaehlen')
	personStrings = []
	for person in Persons:
		personStrings.append(person.firstName + ', ' + person.lastName)
	main['persons'].data_source(ui.ListDataSource(items=personStrings))
	main.present('sheet')

def newBFT(sender):
	bft = BFT(int(sender.superview['timeSprint'].text),  int(sender.superview['timeKlimm'].text), int(sender.superview['time1000m'].text), Persons.pop())

	bft.getPunkte()
	bft.getNoten(sender)

if not Persons:
	gui.load_view('neuePerson').present('sheet')
else:
	gui.load_view('neueAbnahme').present('sheet')
