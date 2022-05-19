#!/usr/bin/env python
# coding: utf-8

# # Einführung

# ## Was sind Daten

# Daten sind eine digitale Repräsentation von Dingen, Entitäten, Wissen und Informationen aus bzw. in der wirklichen Welt. Um mit Daten zu arbeiten, ergeben sich folgende Kernfragen: 
# <br>
# <br>
# Welche Daten speichere ich? Wie speichere ich die Daten? Wie frage ich Daten ab? Wie erledige ich all dies effizient und sicher?
# <br>
# <br>
# Notiz: sehr verschiedene Beispiele für Daten, was sind Metadaten ?

# ## Aufbau eines Datenbanksystems 

# ![title](dbms_aufbau2.jpg)

# Ein Datenbanksystem besteht aus der Datenbank und dem Datenbankmanagementsystem(DBMS). Die Datenbak setzt sich aus den Daten selbst und den Metadaten zusammen, die die Daten beschreiben. Das DBMS ist ein Softwarekomoponente die server-basiert arbeitet. Es ermöglicht den Zugriff auf eine oder mehrere Datenbanken. 
# <br>
# <br>
# Notiz: Anwendungen

# ## Aufgaben eines Datenbanksystems(DBMS)

# Die primären Aufgaben eines Datenbanksystems sind ...
# <br>Unterstützung des Datenmodells
# <br> Bereitstellung einer Anfragesprache
# <br> Data definition language (DDL)
# <br>Data manipulation language (DML)
# <br> Effiziente Anfragebearbeitung
# <br> Robustheit
# <br> Wahrung der Datenintegrität (Konsistenz etc.)
# <br> Abfangen von Systemfehlern
# <br> Speicherverwaltung (RAM & Disk)
# <br> Transaktionsmanagement
# <br> Auch im Mehr-Benutzer-Betrieb
# <br> Nutzerverwaltung & Zugangskontrolle
# <br>
# <br>
# Notiz: Beispiele für die Aufgaben aus der echten Welt, Wieso diese Aufgaben, ist jede Aufgabe zwingend notwendig bzw. welche

# ## Anforderungen an DBMS nach Codd 1982

# ![title](anforderungen_nach_codd.jpg)

# ■ Integration
# <br>
# □ Einheitliche, nichtredundante Datenverwaltung
# <br>
# <br>
# ■ Operationen
# <br>
# □ Definieren, Speichern, Abfragen, Ändern
# <br>
# □ Deklarativ
# <br>
# <br>
# ■ Benutzersichten
# <br>
# □ Verschiedene Anwendungen, Zugriffskontrolle, Umstrukturierung
# <br>
# <br>
# ■ Integritätssicherung
# <br>
# □ Korrektheit und Konsistenz des Datenbankinhalts
# <br>
# <br>
# ■ Transaktionen
# <br>
# □ Mehrere DB-Operationen als Funktionseinheit
# <br>
# <br>
# ■ Synchronisation
# <br>
# □ Parallele Transaktionen koordinieren
# <br>
# <br>
# ■ Datenschutz
# <br>
# □ Ausschluss nicht-autorisierter Zugriffe
# <br>
# <br>
# ■ Datensicherung
# <br>
# □ Wiederherstellung von Daten nach Systemfehlern
# <br>
# □ Persistenz
# <br>
# □ Große Datenmengen, Effizienz
# <br>
# <br>
# ■ Katalog
# <br>
# □ Zugriffe auf Datenbankbeschreibungen im Data Dictionary (Metadaten)

# NICHT enthalten: S.3-5, S. 22-25, S. 28, S. 38-46
