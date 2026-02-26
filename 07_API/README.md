# Projektname: Erstellung einer API zur Datenabfrage

## Beschreibung
In diesem Projekt wird eine API erstellt, über die Daten abgefragt werden können. Es sollen zwei Endpunkte implementiert werden: Einer, der alle Datensätze zurückgibt, und ein anderer, der einen bestimmten Datensatz anhand einer speziellen ID liefert.

## Inhaltsverzeichnis
1. [Einrichten der API](#einrichten-der-api)
2. [Implementierung der Datenabfrage](#implementierung-der-datenabfrage)
3. [Fragen und Antworten](#fragen-und-antworten)

## Einrichten der API
- Richte eine API ein, die auf einem Webframework wie Flask oder Django basiert.
- Konfiguriere die Routen und Endpunkte für die Datenabfrage.

## Implementierung der Datenabfrage
- Implementiere zwei Endpunkte: Einen für die Abfrage aller Datensätze und einen für die Abfrage eines bestimmten Datensatzes anhand einer ID.
- Stelle sicher, dass die Daten korrekt formatiert und über die API zurückgegeben werden.

## Fragen und Antworten
- Was ist eine API? Erläutere den Begriff und ihre Bedeutung in der Softwareentwicklung.
    API(Application Programming Interface) ist eine schnittstelle das Software Daten von anderen Programmen zu erhalten kann.

- Woraus besteht eine API? Beschreibe die Komponenten und Funktionen einer API.
    Endpunkte (adressen/URLs), Methoden(PUT, POST, ...), Datenfluss (Request, Response), Sicherheit, Datenformat, Dokumentation 

- Wann wird eine API verwendet? Erkläre die Einsatzgebiete und Situationen, in denen APIs eingesetzt werden.
    Es wird verwendet wenn Programme daten von anderen Programmen abrufen z.B. eine Wetter app die Daten wie da Wetter ist.

- Warum sind APIs wichtig? Diskutiere die Bedeutung von APIs für die Interoperabilität und Integration von Systemen.
    Sie sind wichtig das Softwareanwendungen Daten austauschen können, zudem förden sie die Effizienz indem sie die Daten Automatisch abrufen

- Was ist ein API-Token und was ein API-Key? Unterscheide zwischen den beiden und erkläre ihre Verwendungszwecke.
    API Token sind zeitlichbegrenzte Schlüssel sie Zeigen der API werdu bist und was du darfst.
    API Keys laufen nicht ab und sind dazu dar der API zu sagen wer du bist

- Warum nicht die Daten direkt auf der DB abfragen? Diskutiere die Vorteile der Verwendung einer API zur Datenabfrage im Vergleich zur direkten Abfrage der Datenbank.
    Durch die APIs gibt es eine art Zwischenschicht die als Zugriffskontrolle fungieren, API wird offt mit https gemacht was for einem "man in the middle" schütz.

- Nenne verschiedene Bereiche, in denen APIs verwendet werden. Beschreibe die Anwendungsbereiche und Beispiele für die Verwendung von APIs.
    Online shops die Produktdaten zu bekommen,
    Socialmedia für Funktionen wie "mit google anmelden"
    APPs z.B. Wetter um Wetterinformationen zu bekommen
    Reiseportale für Echtzeitabfragen von Preisen

- Was ist REST? Erläutere den Begriff und die Prinzipien von RESTful APIs.
    REST ist eine Methode wie man Resourcen über http URLs aufrufen und verändern kann. 

- Was ist GraphQL und wie unterscheidet es sich von REST? Beschreibe die Unterschiede zwischen GraphQL und RESTful APIs.
    GraphQL lädt die daten effizienter als REST weil es bei größerer daten abfrage nicht so viele Endpunkte durchgehen muss, Graph 

- Welche Sicherheitsaspekte sind bei der Entwicklung einer API zu beachten? Diskutiere mögliche Sicherheitsrisiken und Best Practices für die API-Sicherheit.
    Schwache Authentifizierung -> wenn nicht genau überprüft wird wer die Anfrage geschickt hat können unbefugte auf sie zugreifen.
    Injection Angriffe -> Angreifer können schädliche Codes einschleusen und damit das script manipulieren
    Falsche Datenübertragung -> Wenn nicht mit https, können tokens oder passwörter mit gelesen werden
