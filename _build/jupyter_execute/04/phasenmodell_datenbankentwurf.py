#!/usr/bin/env python
# coding: utf-8

# # Phasenmodell für den Datenbankentwurf

# ![title](phasenmodell.jpg)

# ### Einführung (Entwurfsaufgabe, Entwurfsprozess)

# ■ Datenhaltung für mehrere Anwendungssysteme und mehrere Jahre
# <br>
# □ Daher: besondere Bedeutung
# <br>
# <br>
# ■ Anforderungen an Entwurf
# <br>
# □ Anwendungsdaten jeder Anwendung sollen aus Daten der Datenbank ableitbar sein.
# <br>
# – Möglichst effizient
# <br>
# □ Nur „vernünftige“ (wirklich benötigte) Daten sollen gespeichert werden.
# <br>
# □ Nicht-redundante Speicherung

# ### Anforderungsanalyse

#  Vorgehensweise
#  <br>
# □ Sammlung des Informationsbedarfs in den Fachabteilungen
#  <br>
# ■ Ergebnis
#  <br>
# □ Informale Beschreibung des Fachproblems
#  <br>
# – Texte, tabellarische Aufstellungen, Formblätter, …
#  <br>
# □ Trennen der Information über Daten (Datenanalyse) von den Information über Funktionen (Funktionsanalyse)
#  <br>
#  <br>
# ■ „Klassischer“ DB-Entwurf
#  <br>
# □ Nur Datenanalyse und Folgeschritte
#  <br>
#   <br>
# ■ Funktionsentwurf
#  <br>
# □ Siehe Methoden des Software-Engineering

# ### Konzeptioneller Entwurf

# ■ Erste formale Beschreibung des Fachproblems
# <br>
# □ Diskurswelt (Universe of Discourse)
# <br>
# <br>
# ■ Sprachmittel: semantisches Datenmodell
# <br>
# □ ER-Modell (Entity-Relationship-Modell)
# <br>
# <br>
# ■ Vorgehensweise
# <br>
# □ Modellierung von Sichten z.B. für verschiedene Fachabteilungen
# <br>
# □ Analyse der vorliegenden Sichten in Bezug auf Konflikte
# <br>
# – Namenskonflikte (Synonyme, Homonyme)
# <br>
# – Typkonflikte
# <br>
# – Bedingungskonflikte
# <br>
# – Strukturkonflikte
# <br>
# □ Integration der Sichten in ein Gesamtschema
# <br>
# ■ Ergebnis: konzeptionelles Gesamtschema, z.B.(E)ER-Diagramm

# ### Verteilungsentwurf (Partitionierung)

# ■ Sollen Daten auf mehreren Rechnern verteilt vorliegen, muss Art und Weise der verteilten Speicherung festgelegt werden.
# <br>
# <br>
# ■ Z.B. bei Relation KUNDE (KNr, Name, Adresse, PLZ, Konto)
# <br>
# □ Horizontale Partitionierung
# <br>
# – KUNDE_1 (KNr, Name, Adresse, PLZ, Konto)
# <br>
# where PLZ < 50000
# <br>
# – KUNDE_2 (KNr, Name, Adresse, PLZ, Konto)
# <br>
# where PLZ >= 50000
# <br>
# □ Vertikale Partitionierung (Verbindung über KNr Attribut)
# <br>
# – KUNDE_Adr (KNr, Name, Adresse, PLZ)
# <br>
# – KUNDE_Konto (KNr, Konto)

# ### Logischer Entwurf

# ■ Sprachmittel: Datenmodell des ausgewählten DBMS
# <br>
# □ z.B. DB2, Oracle, … ® relationales Modell
# <br>
# □ Tamino ® XML
# <br>
# □ Dynamo, Redis ® key-value Modell
# <br>
# □ OO, JSON, RDF, …
# <br>
# <br>
# ■ Vorgehensweise
# <br>
# □ (Automatische) Transformation des konzeptionellen Schemas
# <br>
# – z.B. ER in relationales Modell
# <br>
# □ Verbesserung des relationalen Schemas anhand von Gütekriterien
# <br>
# – Normalisierung, Redundanzvermeidung, …
# <br>
# <br>
# ■ Ergebnis: logisches Schema, z.B. Sammlung von Relationen-schemata
# <br>
# <br>

# ### Datendefinition

# ■ Umsetzung des logischen Schemas in ein konkretes Schema
# <br>
# <br>
# ■ Sprachmittel: SQL
# <br>
# □ DDL (data definition language) und
# <br>
# DML (data manipulation language) eines DBMS
# <br>
# – z.B. Oracle, DB2, SQL Server, …
# <br>
# □ Datenbankdeklaration in der DDL des DBMS
# <br>
# – CREATE TABLE …
# <br>
# □ Realisierung der Integritätssicherung
# <br>
# – Schlüssel, Fremdschlüssel, Nebenbedingungen, Datentypen
# <br>
# □ Definition von Benutzersichten
# <br>
# – CREATE VIEW …

# ### Physischer Entwurf

# ■ DBMS nimmt automatisiert physischen Entwurf vor.
# <br>
# <br>
# ■ Ergänzen um Zugriffsunterstützung zur Effizienzverbesserung
# <br>
# <br>
# □ z.B. Definition von Indizes
# <br>
# □ CREATE INDEX …
# <br>
# ■ Index
# <br>
# □ Datenstruktur für effizienten, Suchschlüssel-basierten Zugriff auf
# <br>
# Datensätze
# <br>
# (<Schlüsselattributwert, Tupeladresse>)
# <br>
# □ Meist als Baumstruktur oder Hashtabelle realisiert
# <br>
# <br>
# ■ Beispiel
# <br>
# □ Tabelle mit 10 GB Daten
# <br>
# □ Festplattentransferrate ca. 50 MB/s
# <br>
# □ Operation: Suchen einer Bestellung (Selektion)
# <br>
# □ Implementierung: sequentielles Durchsuchen
# <br>
# □ Aufwand: 10.240/50 = 205 sec. = 3,5 min.

# ### Implementierung und Wartung

# ■ Wartung des DBMS
# <br>
# □ Parameter, Festplatten, etc.
# <br>
# <br>
# ■ Datenbank Tuning
# <br>
# □ Weitere Optimierung der physischen Ebene
# <br>
# <br>
# ■ Anpassung an neue Anforderungen
# <br>
# <br>
# ■ Anpassung an neue Systemplattformen
# <br>
# <br>
# ■ Portierung auf neue Datenbankmanagementsysteme
# <br>
# <br>
# ■ Kostenaufwändigste Phase
# <br>
# <br>
# ■ Software Engineering
