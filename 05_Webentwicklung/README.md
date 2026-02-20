# Projektname: Webanwendung mit Flask und ansprechendem Styling

## Beschreibung
Dieses Projekt zielt darauf ab, eine Webanwendung mit Flask aufzusetzen und sie mit einem ansprechenden Styling zu versehen. Zusätzlich sollen weitere Seiten erstellt werden, auf denen Daten aus einer Datenbank ausgelesen werden können. Die Benutzer sollen die Möglichkeit haben, Daten direkt über die Website zu bearbeiten oder zu löschen.

## Inhaltsverzeichnis
1. [Webanwendung mit Flask aufsetzen](#webanwendung-mit-flask-aufsetzen)
2. [Daten aus der Datenbank auslesen](#daten-aus-der-datenbank-auslesen)
3. [Daten bearbeiten und löschen](#daten-bearbeiten-und-löschen)
4. [Fragen und Antworten](#fragen-und-antworten)

## Webanwendung mit Flask aufsetzen
- Setze eine Webanwendung mit Flask auf.
- Verleihe der Webanwendung ein ansprechendes Styling, um eine positive Benutzererfahrung sicherzustellen.
- Erstelle weitere Seiten, auf denen die Daten aus einer Datenbank angezeigt werden.

## Daten aus der Datenbank auslesen
- Implementiere Funktionen, um Daten aus der Datenbank abzurufen und auf den Webseiten darzustellen.

## Daten bearbeiten und löschen
- Biete den Benutzern die Möglichkeit, Daten direkt über die Website zu bearbeiten oder zu löschen.

## Fragen und Antworten
- Was ist Webentwicklung? Erkläre den Prozess des "Bauens" von Webseiten oder Anwendungen für das Internet.
    Webentwicklung ist die Erstellung, Wartung und Optimirerung von Websiten die man über den Browser erreicht.
    Der Bauprozess wird in verschiedene Punkte unterteil:
    Planung, Design Entwicklung, Technische Umsetzung, Testing

- Was ist ein Framework und was ein SDK? Unterscheide zwischen den beiden und erkläre ihre Rolle in der Entwicklung.
    Framework ist ein gerüst wo man nur noch die daten hinzufügen muss und SDK sind verschiedene Bauteile die man zusammen setzen muss.
    Ihre rolle in der Entwicklung ist es den Prozess zu beschleunigen und die Qualität zu erhöhen ohne großen Aufwand daran zu setzen etwas neues zu Erstellen
    
- Welche Sprachen und Frameworks spielen eine Rolle in der Webentwicklung? Nenne Beispiele und ihre Verwendungszwecke.
    Jenach arbeitsbereich (Frontend, Backend) kommen verschiedene Sprachen und Frameworks zum einsatz. 
    Frontend: 
        -HTML: zum erstellen des Webinterfaces
        -CSS: zum Desinen des Webinterfaces
    Backend:
        -Python: Framework Flask als API
        -Java: Framework Spring Boot automatisiert Konfigurationen und bietet eingebettete Server

- Was ist Jinja2 und wofür kann ich es verwenden? Erläutere die Verwendung von Jinja2 in Flask.
    Jinja ist eine Engine die es dir ermöglicht Variablen, Schleifen und Bedingungen direkt in html dateien zu schreiben

- Was sind die Flask HTTP-Methoden, welche gibt es und wann brauche ich welche? Beschreibe die verschiedenen HTTP-Methoden in Flask und ihre Verwendung.
    Es gibt verschiedene HTTP Methoden um zu Sagen was der Client mit den übermitelten Daten machen soll. Die Haupt Merhoden sind:
    PUT -> benötigt wenn Daten überschreiben werden
    POST -> benötigt wenn Daten an den Server gesendet werden
    GET -> benötigt wenn Daten ausgelesen werden
    DELET-> benltigt wenn Daten gelöscht werden

- Was sind Strukturelemente? Erläutere die Bedeutung von Strukturelementen in der Webentwicklung.
    Strukturelementen sind die verschiedenen Bereiche die, die Website unterteilen, die häufigsten Elemente sind:
    Header -> (Kopfzeile) enthält meist Logo, Firmenname
    Footer -> (Fußzeile) enthält oft Datenschutz, Kontakt und Social-Media links
    Content -> (Hauptinhalt) enthält die Hauptinformationen 

- Was sind Flask Blueprints und welchen Vorteil bieten sie? Erkläre die Verwendung von Flask Blueprints in großen Webanwendungen.
    Blueprints ermöglicht es Anwendungen oder Routen scripts in unterschiedliche .py Dateien zu speichern wodurch sie verteilt sind aber trozdem noch zusammen hängen, Vorteile dadurch sind:
    -Übersichtlicher da nicht alles auf einer Datei gespeichert ist 
    -Einfacher neue Funktionen hinzuzufügen
    -Bestehende Funtionen zu verbessern oder bugs zu beheben
    
- Was ist Bootstrap und wie kann ich es verwenden? Beschreibe Bootstrap und seine Rolle beim Erstellen responsiver Websites.
    Bootstrap ist eine Open Source Frontend Framework, mit dem man Websiten und Webanwengungen erstellen kann. Es bietet schon vorab hergestellte Vorlagen wie Formen und Farben für Buttons.

- Was sind SVGs? Erläutere SVGs und ihre Verwendung in der Webentwicklung.
    SVG ist eine Möglichkeit Bilder auf Websiten anzeigen zulassen mit dem unterschied das nicht jeder Pixel einzeln gezeigt wird, wird das bild durch formen wie stricker, kreise oder rechtecke angezeigt. Das hat den vorteil das die Bilder auf jeder Bildschirmgröße Scharf angezeigt werden, das bringt den Vorteil das Websiten Responsive bleiben.

- Was versteht man unter responsive Design? Erkläre die Bedeutung von responsivem Design und warum es wichtig ist.
    Unter responsive Design versteht man das Webanwendungen egal auf welchem Gerät (PC, Handy, ...) funktionieren und sich automatisch an die Seiten Verhältnisse anpassen. Zum Beispiel hat ein Handy eine andere Screen größe als ein PC (bzw Bildschirm) kann also nicht das gleiche anzeigen wie ein PC und muss daher angepasst werden.
