## Aufgabenbeschreibung

### 1. Erstellen eines UML-Klassendiagramms basierend auf den gegebenen Daten:
- **Analysiere die Struktur des JSON-Dokuments** und identifiziere die relevanten Klassen und ihre Attribute sowie Beziehungen zueinander.
- **Zeichne ein UML-Klassendiagramm**, das die Klassen, ihre Attribute und Methoden sowie die Beziehungen zwischen den Klassen (z.B. Assoziationen, Vererbungen) darstellt.

### 2. Implementierung der Klasse in Python:
- **Erstelle eine Python-Klasse oder Klassen**, die die Struktur des UML-Klassendiagramms widerspiegeln.
- **Definiere die Attribute und Methoden** entsprechend den Daten und Anforderungen aus dem JSON-Dokument.

### 3. Einlesen der JSON-Daten als Objekte der erstellten Klasse(n):
- **Schreibe ein Python-Skript**, das die JSON-Daten einliest.
- **Erstelle Instanzen der zuvor definierten Klasse(n)** und initialisiere sie mit den Daten aus dem JSON-Dokument.

### 4. Methode zum Hinzufügen eines Members:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein neues Mitglied zum Team hinzufügt.
- Die Methode sollte die benötigten Informationen (z.B. Name, ID) als Parameter entgegennehmen und ein neues Mitgliedsobjekt erstellen und zur entsprechenden Liste hinzufügen.

### 5. Methode zur Ausgabe des Teams mit den jeweiligen Mitgliedern:
- **Implementiere eine Methode in der entsprechenden Klasse**, die das gesamte Team und deren Mitglieder auf eine lesbare Weise ausgibt.
- Die Methode sollte durch die Mitglieder des Teams iterieren und deren Details anzeigen.

### 6. Methode zum Löschen eines Members anhand der ID:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein Mitglied anhand seiner ID löscht.
- Die Methode sollte die Liste der Mitglieder durchsuchen, das Mitglied mit der passenden ID finden und es aus der Liste entfernen.




## Fragen zur Objektorientierung

1. Warum verwendet man Objektorientierung?
    um einen Code mehrmals wieder verwenden zu können aber mit anderen variablen werten
2. Welche weiteren Vorgehensweisen gibt es? 
    Es gibt z.B. noch die prozedurale Programmierung in der der Code auf Funktionen aufgebaut ist
3. Was ist ein Objekt und was eine Klasse?  
    Eine Klasse legt fest welche Eigenschaften Objekte haben können (z.B. Die Klasse Auto hat die eigenschaften "Marke, Model, Farbe"), ein Objekt besitzt dann die jeweiligen Werte für die Eigenschaften (z.B. ein Objekt für die Auto Klasse wäre "Audi, RS6, Schwarz").
4. Was versteht man unter Kapselung?
    Darunter versteht man das Daten nicht Preisgegeben werden müssen, man weiß zwar das sie da sind aber nicht was diese entsprechen
5. Was ist Vererbung?
    Vererbung ist wenn eine höhere Klasse (Basis Klasse) Attribute oder Methoden einer neuen Klasse (Subklasse) weiter gibt
6. Was versteht man unter Refactoring?
    darunter versteht man einen code zu verbesseren ohne etwas an seinen funktionen zu ändern
7. Welche Rolle spielt das Refactoring bzgl. der Wiederverwendung von Code?
    Dadurch das der code einfacher/verständlicher geschrieben ist kann er für andere Projekte (oder auch im selben code) einfacher wieder verwendet werden.
8. Für was gibt es die `__init__`-Funktion in einer Klasse?
    Die Funktion dient dazu die Anfangszustände der Objekte festzulegen
9. Für was braucht man den `self` Parameter?
    damit die durch __init__ gespeicherten daten in eine variable eingespeichert werden können
10. Wie schreibt man einzeilige und mehrzeilige Kommentare in Python?
    einzeilige entweder mit einem "#" (alles was dahinter steht wird als kommentag gewärtet)
    und mehr Zeilig mit 3." also """ & """ alles was zwischen diesen Anführungsstrichen steht wird als kommentar gewärtet
11. Welche weiteren objektorientierten Programmiersprachen neben Python gibt es? (3 Beispiele)
    Java, C#, C++
12. Korrigiere die Fehlerhaften Skripte.

### Code 1. 
es fehlt das "self" in der __init__ funktion
```python
class MyClass:
    def __init__(name):
        self.name = name

    def greet():
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()
```


### Code 2 
print ist zu weit ausgerückt
```python
def say_hello():
print("Hello, World!")  

say_hello()
```


### Code 3 
zu wenige "=" bei dem if vergleich
```python
x = 10
if x = 5:   
    print("x is 5")
```


### Code 4 
Tupel sind nicht änderbar (numers[i] kann den wer nicht austauschen)
```python
numbers = (1, 2, 3, 4, 5) 
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```


### Code 5 
zu viele daten zum einspeichern (zu entpacken gibt es 5,aber es ist nur platz für 3)
```python
values = [1, 2, 3, 4, 5]
a, b, c = values
```
