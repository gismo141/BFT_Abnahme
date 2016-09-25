# -*- coding: utf8 -*-

# Klasse zur Verwaltung von Personen
class Person(object):
  # Konstruktor/Initialisierer
  def __init__(self, alter, groesse, name = None):
    self.alter = alter
    self.groesse = groesse
    self.name = name

  # String-Repräsentation einer Person erstellen
  def __repr__(self):
    return repr((self.alter, self.groesse, self.name))

  # einfache String-Repräsentation einer Person erstellen
  def __str__(self):
    return '%s/%s/%s' % (self.alter, self.groesse, self.name)

  # Person altern lassen, also Alter um n Jahre erhöhen
  def altern(self, n = 1):
    self.alter += n

  # mittels eines Dekorators eine Property mytuple erzeugen;
  # Properties implementieren das Deskriptor-Protokoll
  @property
  def mytuple(self):
    # das ist der Getter; den Namen lassen wir hier im Rückgabewert aus
    return self.alter, self.groesse
  # alternativ:
  #   def mytuple(self): return self.alter, self.groesse
  #   mytuple = property(mytuple)
  
  # einen Setter für die Property definieren
  @mytuple.setter
  def mytuple(self, t):
    if t[0] > 10 and t[1] > 150:
      self.alter, self.groesse = t[:2]
      if len(t) > 2:
        # wenn t einen Namen enthält, dann diesen auch setzen
        self.name = t[2]

  # einen Deleter für die Property definieren
  @mytuple.deleter
  def mytuple(self):
    self.alter = self.groesse = 0
    self.name = ''

# Personenliste erstellen
personen = [Person(39, 172, 'ABC'), Person(88, 165), Person(15, 181), Person(88, 175)]

# Ausgabe der Personenliste
print personen
print '==='

# Attribute mytuple der letzten Person der Liste löschen
del personen[-1].mytuple

# Iteration über der Personenliste und Ausgabe der einzelnen Personen
for pers in personen:
  print pers, '==>', repr(pers)
print '==='

# alle Personen altern lassen
for pers in personen:
  pers.altern(3)

# nochmal ausgeben
print 'nach dem Altern'
print personen
print '==='

# nochmal altern lassen, diesmal funktional
map(lambda x: x.altern(3), personen)
print 'nach dem 2. Altern'
print personen
print '==='

# nochmal funktional altern lassen, diesmal mit Vorzugswert n
map(Person.altern, personen)
print 'nach dem 3. Altern'
print personen
print '==='

# Ausgabe der sortierten Personenliste
print sorted(personen, key = lambda pers: (pers.alter, pers.groesse))
print '==='

# dito mit benannter Funktion statt einer anonymen lambda-Funktion
def pers_key(pers):
  return pers.alter, pers.groesse
  
print sorted(personen, key = pers_key)

# Attribute sind public, man kann von außen zugreifen
print personen[0].alter
print personen[0].groesse
print personen[0].name

p = personen[0]
print p.alter + p.groesse

# Nutzung der Property mit Getter
print p.mytuple
p.alter += 100
print p.mytuple

# Nutzung des Setters der Property
p.mytuple = 1, 2 # wird vom Setter stillschweigend ignoriert
print repr(p.mytuple)

p.mytuple = 11, 155
print repr(p.mytuple)

# nochmal, aber mit Name
p.mytuple = 11, 155, 'Pumuckl'
print repr(p.mytuple)

for p in personen:
  print p

print 'maximales Element einer Personen-Liste bestimmen'
print max((person.alter, person.groesse) for person in personen)

# alternativ nutzbar wären
print max(map(lambda elem: (elem.alter, elem.groesse), personen))
print max(personen, key = lambda elem: (elem.alter, elem.groesse))

print

# Größe von außen ändern
personen[1].groesse += 5
for p in personen:
  print p

print

# neues Attribut setzen
personen[1].name2 = 'XYZ'
for p in personen:
  print p # __str__() wird für die String-Darstellung gerufen

print

# hier sieht man das neue Attribut
for p in personen:
  print vars(p)

print

print 'Maximum der Property mytuple'
print max(person.mytuple for person in personen)

# das Tupel der letzten Person der Liste ändern
personen[-1].mytuple = 110, 190

# Maximum erneut ausgeben
print 'Maximum der Property mytuple nach Zuweisung'
print max(person.mytuple for person in personen)

# nochmal alle Attribute mit vars()
print
for p in personen:
  print vars(p)
