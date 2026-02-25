## Aufgabenbeschreibung
Die Daten sollen in einer Datenbank gespeichert werden.

1. **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.
2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.
3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.
4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
   a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
   b) **Löschen**: Daten werden aus der Datenbank gelöscht.
   c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
   d) **Auslesen**: Daten werden aus der Datenbank abgerufen.

### Fragen:

- Welche Datenbanken gibt es? 
   MySQL
   SQLite
   PostgreSQL
   MongoDB
   Redis

- Wann macht welcher Typ Sinn? 
   Rationale Datenbanken -> überall wo Bezihungen und klare Struktur wichtig ist
   Dokumenten Datenbank -> wenn sich datenstruktur oft ändert
   Key-Value Datenbank -> um Userdaten speichern 

- Was ist ein Primary Key und was ein Foreign Key?
   Primary:
      Ein Primary Key ist eine eindeutige Kennung für jeden Zeile in einer DB wodurch der Datensatz findbar ist, dieser darf nicht doppelt vorkommen und nicht 0/Leer sein. Bei einer Rationalen Datenbank ist dieser Primary Key meist durch eine spalte ganz am anfang gekennzeichnet, jede zeile bekommt eine nummer zugewiesen welche dann die zeile repräsentiert.
   Foreign:
      Ein Foreign Key ist eine Verknüpfung auf eine andere Tabelle, das Feld mit dem Foreign Key ist ein eintag der auf eine andere Tabelle (oder ein ihnhalt daraus) zeigt. Zum Beispiel gibt es zwei listen:
      Liste 1 (Käufer):       Käufer ID,  Name,    Adresse
                              1           Tom      muster Str
      Liste 2 (Bestellungen): Bestell ID, Wahren Preis,  Käufer
                              1782912     3,99€          1
      Die Spalte "Käufer" (Liste 2) ist der Foreign Key. Er zeigt auf "Käufer ID" (Liste 1) und weist darauf hin das die Bestellung zu ihm gehöhrt 

- Was ist ein nativer und was ein künstlicher Primary Key?
   Ein Nativer Key ist eine Information, die fest zu den Daten gehört wie z.B. die Besteller ID, diese wird dann als Key Benutzt.
   Bei einem Primary Key wird eine spalte eingefügt und jeder Zeile ein Key Zugewiesen welcher dann genutz wird

- Welche Beziehungstypen zwischen Tabellen gibt es?
   Es gibt 3 arten von Beziehungen zwischen Tabellen.
   1. die 1/1 beziehung in der sich eine Zeile aus einer Tabelle auf die einer anderen bezieht
   2. die 1/n beziehung in der sich eine Zeile aus einer Tabelle auf mehrere einer andere bezieht
   3. die m/n beziehung in der sich mehrere Zeilen aus einer Tabelle auf mehrere andere bezieht

- Welche Wildcards gibt es in MySQL und was bedeuten sie?
   Wildcards sind platzhalter die bei dem suchen/filtern von daten hilft.
   Es gibt "%" was signalisiert das hier noch mehr Zeichen kommen können
   Beispiel: bl% -> dazu zählt "bl, black, blue"
   Es gibt "_" was signalisiert eine genau anzahl an Zeichen die kommen können
   Beispiel: H_t -> dazu zählt "hot, hat, hit"

- Was ist ein Join?
   Join hilft Daten von einer Tabelle in eine andere zu übertragen indem es die daten zusammen zählt die verknüpft sind.

- Was ist ein left- und was ein right-Join?
   Bei einem Left-join werden alle daten von der linken Tabelle genommen und aus der Rechten nur passende eingefügt.
   Bei einem Right-join ist es genau umgekert.

- Was ist das kartesische Produkt zweier Tabellen?
   Dadurch entsteht eine neue Tabelle die alle informationen enthält. Die spalten anzahl wird Miteinander Multipliziert und jede mögliche beziehung aufgeschrieben

- Was ist Kaskadierung?
   Bei einer Kaskadierung hängen die Tabellen zusammen und übernehmen Veränderungen auf untergeordnete Tabellen automatisch. Zum Beispiel wenn ein Kunde in der Kunden Tabelle gelöscht wird, werden alle bestellungen von diesem Kunden in untergeordneten Tabellen ebenfalls gelöscht. Das hilft leere oder alleinestehende Zeilen zu vermeiden.

- Wann werden Gruppierungen benötigt?
   Um Daten zusammenzufassen oder Aggregationsfunktionen  für diese Gruppe zu berechnen.

- Was ist ein DBMS?
   Es ist ein Programm zur verwaltung von Datenbanken, es kann sie erstellen und kontrollieren. Man kann auch sagen das es die schnittstelle zwischen Benutzer/anwendung und den Physischen Daten.

- Was versteht man unter Datenintegrität?
   Es bezeichnet die Richtigkeit, Vollständigkeit, Konsistens und Unversehrtheit von Daten. Es stellt sicher das die Daten nicht von Unbgefugten verändert wurden

- Was ist Normalisierung?
   Die Normalisierung ist ein Prozess in dem Daten effizient in Tabellen Organisiert werden um Redundanzen zu minimieren.

- Was sind Aggregationsfunktionen und welche gibt es? (3 Beispiele)
   Es sind Funktionen die verwendet werden können um aus mehreren Daten in einer Spalte einzelne Werte zurück zugeben. 
   Mehrere Werte zusammenfassen und einen einzelnen Wert zurückgeben.
   Aggregationsfunktionen sind:
   COUNT() -> Zählt wie viele Zeilen eine Spalte hat
   SUM() -> Zählt alle Werte der einzelnen Zeilen zusammen
   MIN() -> Gibt den kleinsten wert wieder
   MAX() -> Gibt den größten werd wieder
