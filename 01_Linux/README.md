# Einrichten einer Virtual Machine (VM) unter Rocky Linux

## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.


### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer für das tägliche arbeiten. Du kannst ihn benennen wie du möchtest 


### Installierte Programme
a) nvim  
b) Git  
c) check-mk 
b) Erstelle ein Basis Monitoring für ein Server, Switches, Firewall 

## Fragen und Antworten
- Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
    Linux ist ein opensource betriebssystem heißt mann kann denn code einsehen ändern oder verschicken, nicht so wie bei windows
- Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
    Linux ist individuell anpassbar heißt man kann den Code selbstständig ändern und z.B. sachen installieren oder umschreiben
- Warum sollt man nicht dauerhaft mit dem root User arbeiten?
    Ein virus mit root könnte sich tief im Betriebssystem einnisten und auf alles zugreifen und ohne root nur auf ihr  daten 
    Durch missgeschicke könnten daten gelöscht werden die das Betriebssystem zum laufen benötigt
- Was ist Virtualisierung und welche Vorteile bieten VMs?
    Vitualisierung ist die erstellung von mehreren Virtuellen Umgebungen auf nur einem System
    VMs sind viel schneller und einfacher zu erstellen als ein pyshsicher server Benutzbar zu machen
- Was sind yum und dnf?
    daniil weiß es auch nicht
- Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
    IDE ist ein editor der funktionen wie z.b. compiler, Debugger hat
    In einen Texceditor kann man nur TExte schreiben oder Bearbeiten
- Was ist der Unterschied zwischen einem LSP und einem Texteditor?
    LSP ist ein Protokoll das codes (z.B. in VS Code) automatisch vervollständigen kann indem es checkt was als nächstes kommen muss.
    bei einem Texteditor gibt es keine vorgegebenen schreib möglichkeiten also kann er nicht wissen was alnächstes kommt
- Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
    Durch bestimmte zeichen wie "&" am ende eines befehls 
- Wie kann man Skripte unter Linux erstellen und ausführen?

- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
    Ein Kernel verbindet Softawre mit harwear, man kann ihn über das Terminal Aktualisiern 
- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
    symbolische Links verweisen aufden gespeicherten pfad hin wohin hardlink direkt auf das verlinkte 
    Wenn das Symbolisch verlinkte gelöscht wird ist der Link unbrauchbar, bei einem Hardlink Funkrioniert er immer noch
- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
    Linux bekommt daruch längere zeit updates und is damit immer auf dem Sichersten stand und kann optimal laufen
- Wie schreibt man Kommentare in Bash?
    Man öfnet bash wählt sich in den richtigen ordner ein und kann von da aus dann diesen Ordner verwalten
- Was ist vim?
    ein Text editor mit vielen Funktionen was das bearbeiten erleichtern soll

### Linux-Befehle
Was bewirken folgende Befehle:
- `history`
    Zeigt die zuletzteingegebenen befehle an
- `chmod`
    Dadurch kann man die zugriffsrechte einer datei/ortners ändern
- `chown`
    Dadruch kann man den Besitzer einer Datei ändern
- `mv test.txt abc`
    verschiebt datei zu ordner abc wenn nicht vorhanden benennt in abc um
- `ll | grep test`
    listet dateien auf die test enthalten
- `find . -name cisco`
    Sucht im Ordner/Unterordnern (wegen ".") nach datei namens cisco
- `find / -name cisco`
    Sucht im gesamten System (wegen "/") nach datei namens cisco
- `tar -xvf archive.tar.gz`
    tar archiviert und xvf sagt was/wie passiert
- `df -h`
    zeigt freien speicher
- `du -sh directory`
    Zeigt an wie Groß ein bestimmtes verzeichniss ist 
- `ps aux`
    List alle laufenden Prozesse aus
- `grep pattern file`
    Durchsucht angegeben datei nach Textmustern
- `top`
    zeig echtzeit Ansicht der laufenden Prozesse un Systemressoucen
- `netstat -tuln`
    Zeigt den Netzstatus an
- `ifconfig`
    Zeigt Infos zu den Netzwerkschnittstellen an wie IP
- `ping host`
    überprüft die verbindung zu einem andern Rechner


