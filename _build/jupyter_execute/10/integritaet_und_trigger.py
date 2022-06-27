#!/usr/bin/env python
# coding: utf-8

# # Integrität und Trigger
# 
# ## Motivation – Aktive Datenbanken
# ■ Einzufügende Daten können fehlerhaft sein
# <br>
# □ Typographische Fehler, logische Fehler
# <br><br>
# ■ Lösung 1: Bessere Anwendung schreiben
# <br>
# □ Aber: Konsistenz und Korrektheit sind schwer zu prüfen (komplexe Bedingungen, abhängig von schon vorhandenen Daten).
# <br><br>
# ■ Lösung 2: Aktive Elemente im DBMS
# <br>
# □ Einmal spezifiziert
# <br>
# □ Ausgeführt wenn nötig
# <br>
# □ „Integritätsbedingungen“ (integrity constraints, ICs)

# ## Schlüssel und Fremdschlüssel
# 
# ### Schlüssel
# ■ Wichtigste Bedingung: Ein oder mehrere Attribute bilden einen Schlüssel.
# <br>
# □ Falls S die Schlüsselmenge ist, müssen sich zwei Tupel in mindestens einem Attributwert der Schlüsselmenge
# unterscheiden.
# <br>
# □ Spezifikation im CREATE TABLE Ausdruck
# <br>
# – Primärschlüssel: PRIMARY KEY
# <br>
# – Schlüssel: UNIQUE oder UNIQUE NOT NULL
# 
# #### Primärschlüssel
# ■ Maximal ein Primärschlüssel pro Relation
# <br>
# □ Zwei Tupel müssen sich in mindestens einem Attributwert der Primärschlüsselattribute unterscheiden.
# <br>
# □ Tupel dürfen keinen NULL-Werte in den Primärschlüsselattributen haben.
# Bei einem Attribut: Deklaration direkt in Attributliste
# ```
# CREATE TABLE SchauspielerIn(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1),
# Geburtstag DATE);
# ```
# ■ Bei (einem oder) mehreren Attributen: Deklaration nach den Attributen
# ```
# CREATE TABLE SchauspielerIn(
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1),
# Geburtstag DATE,
# PRIMARY KEY (Name, Adresse) );
# ```
# 
# #### Sekundärschlüssel
# ■ Spezifikation mit UNIQUE
# <br>
# □ Syntax wie für PRIMARY KEY
# <br>
# – Direkt beim Attribut
# <br>
# – Als separate Attributliste
# <br><br>
# ■ Bedeutung etwas anders:
# <br>
# □ Es darf mehrere UNIQUE Deklarationen geben
# <br>
# □ UNIQUE erlaubt NULL-Werte
# <br>
# – und NULL ≠ NULL (bzw. UNKNOWN)
# <br>
# => Zwei Tupel können in UNIQUE Attributen übereinstimmen: NULL
# <br>
# – Abhilfe: NOT NULL
# ```
# CREATE TABLE SchauspielerIn(
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1),
# Geburtstag DATE UNIQUE,
# UNIQUE (Name, Adresse));
# ```
# 
# #### Schlüsselbedingungen erzwingen
# Schlüsselbedingungen müssen stets gelten.
# <br><br>
# Relevant nur bei INSERT und UPDATE
# <br>
# Bei DELETE kann nichts passieren.
# <br><br>
# Effiziente Prüfung mittels Index
# <br>
# DBMS legen idR automatisch Indizes für Primärschlüsselattribute an.
# <br>
# Optional auch für UNIQUE Attribute
# <br>
# CREATE UNIQUE INDEX JahrIndex ON Filme(Jahr);
# <br>
# Wie CREATE INDEX JahrIndex ON Filme(Jahr), aber mit neuer UNIQUE Bedingung auf Jahr.
# <br>
# Bei Einfügen oder Ändern: Prüfen ob neuer Schlüsselwert bereits vorhanden
# <br><br>
# Ineffiziente Prüfung (falls kein Index vorhanden ist)
# <br>
# Binäre Suche falls Daten sortiert sind
# <br>
# Sequentielle Suche sonst
# 
# #### Fremdschlüssel
# Werte in bestimmten Attributen sollen „sinnvoll“ sein.
# <br>
# ManagerIn(Name, Adresse, ManagerinID, Gehalt)
# <br>
# Studios(Name, Adresse, VorsitzendeID)
# <br>
# Z.B.: Der Attributwert für VorsitzendeID sollte auf einen bestimmten, vorhandenen Manager verweisen.
# <br>
# Referentielle Integrität – dangling tuples
# <br>
# Ein Attribut oder eine Attributmenge kann als FOREIGN KEY deklariert werden, die eine entsprechende Attributmenge einer zweiten Relation referenziert.
# <br>
# Die referenzierte Attributmenge muss UNIQUE oder PRIMARY KEY sein.
# <br>
# Gemeinsame Werte der Fremdschlüsselattribute müssen als gemeinsame Werte des referenzierten Schlüssels auftauchen.
# <br>
# Ausnahme: Ein Fremdschlüssel darf den Wert NULL annehmen.
# <br>
# Das Schlüsselattribut muss nicht einen NULL-Wert besitzen (und darf es meist auch nicht).
# <br>
# Abhilfe: NOT NULL
# <br><br>
# Syntax
# <br>
# Auf einem Attribut:
# <br>
# REFERENCES Relation(Attribut)
# <br>
# Auf (einem oder) mehreren Attributen:
# <br>
# FOREIGN KEY (Attribute) REFERENCES Relation(Attribute)
# ManagerIn(Name, Adresse, ManagerinID, Gehalt)
# Studios(Name, Adresse, VorsitzendeID)
# 
# ```
# CREATE TABLE Studios(
#     Name CHAR(30) PRIMARY KEY,
#     Adresse VARCHAR(255),
#     VorsitzendeID INT REFERENCES Manager(ManagerinID));
#     
# CREATE TABLE Studios(
#     Name CHAR(30) PRIMARY KEY,
#     Adresse VARCHAR(255),
#     VorsitzendeID INT,
#     FOREIGN KEY (VorsitzendeID) REFERENCES
# ManagerIn(ManagerinID));
# ```
# 
# ### CREATE TABLE – Beispiel
# ```
# CREATE TABLE Employee(
#     FirstName CHAR(30),
#     LastName CHAR(30),
#     City VARCHAR(255) NOT NULL,
#     ZIP INT,
#     Street VARCHAR(255),
#     ProjectName VARCHAR(50),
#     ProjectYear INT,
#     DepID INT NOT NULL,
#     PRIMARY KEY (FirstName,LastName),
#     FOREIGN KEY (DepID) REFERENCES Department(DepID),
#     FOREIGN KEY (ProjectName,ProjectYear)
#         REFERENCES Project(Name, Year) );
# ```
# 
# ### Referentielle Integrität erzwingen
# Drei Varianten
# <br>
# Verletzende Änderungen ablehnen (SQL default)
# <br>
# Kaskadierung
# <br>
# Null-Werte
# <br><br>
# Beispiel
# Manager(Name, Adresse, ManagerID, Gehalt)
# <br>
# Studios(Name, Adresse, VorsitzenderID)
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID));
# ```
# 
# #### Referentielle Integrität erzwingen: Änderungen Ablehnen
# Default: Änderungen ablehnen
# <br><br>
# Für jede VorsitzendeID muss es auch einen ManagerinID geben.
# <br>
# INSERT Studio mit neuer (nicht-NULL) VorsitzendeID, die nicht in Manager gespeichert ist
# <br>
# Abgelehnt
# <br><br>
# UPDATE eines Studios mit einer neuen VorsitzendeID, die nicht in Manager gespeichert ist
# <br>
# Abgelehnt
# <br><br>
# DELETE eines ManagerIn-Tupels, dessen ManagerinID auch eine (oder mehr) VorsitzendeID ist
# <br>
# Abgelehnt
# <br><br>
# UPDATE der ManagerinID eines Manager-Tupels, die auch eine (oder mehr) VorsitzendeID ist
# <br>
# Abgelehnt
# 
# #### Referentielle Integrität erzwingen: Kaskadierung
# Idee: Änderungen im Schlüssel werden im Fremdschlüssel nachgezogen.
# <br><br>
# INSERT Studio mit neuer (nicht-NULL) VorsitzendeID, die nicht in Manager gespeichert ist
# <br>
# Abgelehnt
# <br><br>
# UPDATE eines Studios mit einer neuen VorsitzendeID, die nicht in Manager gespeichert ist
# <br>
# Abgelehnt
# <br><br>
# DELETE eines Manager-Tupels, dessen ManagerinID auch eine (oder mehr) VorsitzendeID ist
# <br>
# OK, aber alle abhängigen Studios werden ebenfalls gelöscht.
# <br><br>
# UPDATE der ManagerinID eines Manager-Tupels, die auch eine (oder mehr) VorsitzendeID ist
# <br>
# OK, die VorsitzendeIDs in Studios werden ebenfalls geändert
# 
# #### Referentielle Integrität erzwingen: Auf NULL setzen
# Idee: Bei Änderungen im Schlüssel wird der Wert des Fremdschlüssels auf NULL gesetzt.
# <br><br>
# INSERT Studio mit neuer (nicht-NULL) VorsitzendeID, die nicht in Manager gespeichert ist
# <br>
# Abgelehnt
# <br><br>
# UPDATE eines Studios mit einer neuen VorsitzendeID, die nicht in Manager gespeichert ist
# <br>
# Abgelehnt
# <br><br>
# DELETE eines Manager-Tupels, dessen ManagerinID auch eine (oder mehr) VorsitzendeID ist
# <br>
# OK, aber VorsitzendeID aller abhängigen Studios werden auf NULL gesetzt.
# <br><br>
# UPDATE der ManageID eines ManagerIn-Tupels, die auch eine (oder mehr) VorsitzendeID ist
# <br>
# OK, aber die VorsitzendeIDs in Studios werden auf NULL gesetzt.
# 
# #### Referentielle Integrität erzwingen
# SQL Syntax
# <br>
# Vorgehensweise kann individuell spezifiziert werden
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID)
# ON DELETE SET NULL
# ON UPDATE CASCADE
# );
# ```
# „Vorsichtige“ Strategie
# <br>
# Studios werden nicht gelöscht
# <br>
# Studios behalten falls möglich ihren Vorsitzenden.
# 
# ### Integritätschecks verschieben
# Es ist nicht immer möglich, Tupel einzufügen, die der referentiellen Integrität gehorchen.
# ```
# INSERT INTO Studios
# VALUES (‘Redlight‘, ‘New York‘, 23456);
# ```
# Problem: ManagerIn 23456 wurde (noch) nicht angelegt
# 
# ```
# INSERT INTO Studios(Name, Adresse)
# VALUES (‘Redlight‘, ‘New York‘);
# ```
# OK, da NULL-Werte nicht auf referentielle Integrität geprüft werden müssen.
# <br>
# Später dann (nach Einfügen des Managertupels):
# ```
# UPDATE Studios SET VorsitzendeID = 23456
# WHERE Name = ‘Redlight‘;
# ```
# Bessere Lösung: Erst den Manager, dann das Studio einfügen.
# <br><br>
# Es kann zyklische referentielle Integritätsbedingungen geben.
# <br>
# Manager sind nur Vorsitzende von Studios
# <br>
# ManagerinID ist Fremdschlüssel und referenziert VorsitzendeID.
# <br>
# Es kann nach wie vor kein Studio ohne vorhandenes Managertupel eingefügt werden.
# <br>
# Es kann nun auch kein Manager ohne vorhandenes Studio eingefügt werden.
# <br>
# Catch 22!
# <br>
# Lösung
# <br>
# Mehrere Änderungsoperationen zu einer „Transaktion“ zusammenfassen (mehr später: „Transaktionsmanagement“)
# <br>
# Integritätschecks bis ans Ende der Transaktion verschieben
# <br><br>
# ■ Jeder Constraint kann als DEFERRABLE oder NOT DEFERRABLE deklariert werden.
# <br><br>
# ■ NOT DEFERRABLE ist default
# <br>
# □ Bei jeder Änderung der Datenbank wird die Bedingung geprüft.
# <br><br>
# ■ DEFERRABLE
# <br>
# □ INITIALLY DEFERRED:
# <br>
# – Verschieben ans Ende der Transaktion
# <br>
# – oder bis wir Verschiebung aufheben
# <br>
# □ INITIALLY IMMEDIATE
# <br>
# – Zunächst nichts verschieben, bis wir Verschiebung verlangen.
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT UNIQUE REFERENCES ManagerIn(ManagerinID)
# DEFERRABLE INITIALLY DEFERRED
# );
# ```

# ## Bedingungen auf Attributen und Tupel
# 
# ### Weitere Arten der Nebenbedingungen
# ■ Verbieten Annahme bestimmter Werte
# <br><br>
# ■ Bedingungen auf einzelnen Attributen
# <br>
# □ NOT NULL
# <br>
# □ CHECK
# <br><br>
# ■ Bedingungen für ganze Tupel, also auf das Schema
# <br>
# □ CHECK
# 
# ### NOT NULL
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT NOT NULL
# REFERENCES ManagerIn(ManagerinID)
# ON UPDATE CASCADE
# );
# ```
# ■ Einfügen eines Studios ohne Manager ist nicht mehr möglich.
# <br><br>
# ■ Jedes Studio muss eine Adresse haben.
# <br><br>
# ■ Die Null-Werte Strategie beim Löschen von Managern ist nicht mehr möglich.
# 
# ### Attribut-basierte CHECK Bedingungen
# Verfeinerung der erlaubten Werte für ein Attribut durch Spezifikation einer Bedingung.
# <br><br>
# Bedingung beliebig komplex
# <br>
# Wie WHERE Klausel
# <br>
# Oder sogar als SELECT…FROM…WHERE… Anfrage
# <br><br>
# i.d.R. aber eine einfache Einschränkung der Werte
# <br><br>
# CHECK wird geprüft falls ein Attribut einen neuen Wert erhält
# <br>
# INSERT
# <br>
# UPDATE
# <br><br>
# Falls FALSE, scheitert die Änderung
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID)
# CHECK (VorsitzendeID >= 100000)
# );
# 
# CREATE TABLE SchauspielerIn (
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CHECK (Geschlecht IN (‘W‘, ‘M‘, ‘D‘)),
# Geburtstag DATE );
# ```
# CHECK Bedingung darf sich auch auf andere Attribute beziehen.
# <br>
# Nur im Zusammenhang mit einer SQL Anfrage
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT CHECK (
# VorsitzendeID IN
# (SELECT ManagerinID FROM ManagerIn))
# );
# ```
# Simuliert referentielle Integrität
# <br>
# Was kann schief gehen?
# <br>
# UPDATE und INSERT auf der Studios Relation
# <br>
# CHECK wird geprüft
# <br>
# DELETE auf der Manager Relation
# <br>
# CHECK wird nicht geprüft; CHECK Bedingung wird ungültig
# <br>
# D.h.: Andere Relationen kennen diese CHECK Bedingung nicht.
# 
# ### Tupel-basierte CHECK Bedingungen
# Bedingungen können auch für ganze Tupel deklariert werden.
# <br>
# Wie Primär- und Fremdschlüsselbedingungen kann auch einen CHECK Bedingung in der Liste der Attribute auftauchen.
# <br>
# Ebenso wie bei Attribut-basierten CHECKs: Beliebige Bedingungen wie eine WHERE Klausel.
# <br>
# Wird geprüft bei jedem INSERT und jedem UPDATE eines Tupels.
# ```
# CREATE TABLE SchauspielerIn (
# Anrede CHAR(10),
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CHECK (Geschlecht IN (‘W‘, ‘M‘, ‘D‘)),
# Geburtstag DATE,
# CHECK (Geschlecht = ‚W‘ OR Anrede NOT LIKE ‚Fr%‘ ));
# ```
# Typischer Aufbau einer Bedingung wenn wir mehrere Eigenschaften gemeinsam verbieten wollen (Männlich und Name beginnt mit „Frau…“)
# <br><br>
# Wird nicht geprüft falls eine andere (oder sogar die gleiche) Relation in einer Subanfrage der CHECK
# Bedingung erwähnt wird und diese eine Änderung erfährt.
# <br>
# D.h.: Andere Relationen kennen diese CHECK Bedingung nicht.
# <br>
# Solche Probleme gibt es bei ASSERTIONS (siehe unten) nicht. Deshalb komplexe Bedingungen lieber als ASSERTION deklarieren,
# <br>
# oder (realistischer) in die Anwendungslogik stecken.
# 
# ### Bedingungen ändern
# Zur Änderung von Bedingungen müssen Namen vergeben werden.
# ```
# CREATE TABLE SchauspielerIn (
# Anrede CHAR(19),
# Name CHAR(30) CONSTRAINT NamePrimaer PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CONSTRAINT NichtGeschlechtslos
# CHECK (Geschlecht IN (‚W‘, ‚M‘)),
# Geburtstag DATE,
# CONSTRAINT AnredeKorrektConstraint
# CHECK (Geschlecht = ‚W‘ OR Anrede NOT LIKE ‚Frau%‘ );
# ```
# Meist vergeben DBMS sowieso interne (aber hässliche) Namen.
# 
# ```
# SET CONSTRAINT MyConstraint DEFERRED;
# 
# SET CONSTRAINT MyConstraint IMMEDIATE;
# ```
# ■ Entfernen
# ```
# ALTER TABLE Schauspieler DROP CONSTRAINT NamePrimaer;
# ALTER TABLE Schauspieler DROP CONSTRAINT NichtGeschlechtslos;
# ALTER TABLE Schauspieler DROP CONSTRAINT AnredeKorrekt;
# ```
# ■ Hinzufügen
# ```
# ALTER TABLE Schauspieler ADD CONSTRAINT NamePrimaer PRIMARY KEY (Name);
# ALTER TABLE Schauspieler ADD CONSTRAINT NichtGeschlechtslos CHECK (Geschlecht IN (‚W‘, ‚M‘));
# ALTER TABLE Schauspieler ADD CONSTRAINT AnredeKorrekt CHECK (Geschlecht = ‚W‘ OR name NOT LIKE ‚Frau%‘ );
# ```
# □ Diese Bedingungen sind nun alle Tupel-basiert.
# <br>
# □ Attribut-basierte Bedingungen können nicht nachträglich eingefügt werden.

# ## Zusicherungen und Trigger
# 
# ### Motivation
# Manche Bedingungen sollen sich nicht auf bestimmte Tupel beziehen, sondern auf Schemaebene definiert werden (wie Relationen und Sichten).
# <br><br>
# Assertion (Zusicherungen)
# <br>
# Boole‘scher SQL Ausdruck, der stets wahr sein muss
# <br>
# Einfache Handhabung für Admin
# <br>
# Schwierig, effizient zu implementieren
# <br><br>
# Trigger („Auslöser“)
# <br>
# Aktionen, die bei bestimmten Ereignissen (INSERTs, …) ausgelöst werden
# <br>
# Leichter, effizient zu implementieren
# 
# ### Assertions
# CREATE ASSERTION Name CHECK (Bedingung)
# <br><br>
# Bedingung muss bei Erzeugung der Assertion bereits gelten.
# <br>
# Bedingung muss stets gelten; Änderungen, die die Assertion falsch machen, werden abgewiesen.
# <br>
# CHECK Bedingung können hingegen falsch werden!
# <br><br>
# Zur Formulierung
# <br>
# Kein direkter Bezug zu Relationen, deshalb müssen Attribute und Relationen in einer SQL Anfrage eingeführt werden.
# <br><br>
# Löschen
# <br>
# DROP ASSERTION Name;
# 
# #### Assertions – Beispiel
# ■ ManagerIn(Name, Adresse, ManagerinID, Gehalt) Studios(Name, Adresse, VorsitzendeID)
# <br>
# ■ Vorsitzende von Studios müssen mindestens 1.000.000 verdienen.
# ```
# CREATE ASSERTION ReicheVorsitzende CHECK
# (NOT EXISTS
# (SELECT *
# FROM Studios, ManagerIn
# WHERE ManagerinID = VorsitzendeID
# AND Gehalt < 1000000)
# );
# ```
# ■ Alternative:
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID),
# CHECK ( VorsitzendeID NOT IN
# (SELECT ManagerinID FROM ManagerIn
# WHERE Gehalt < 1000000))
# );
# ```
# ■ Was ist der Unterschied?
# <br>
# □ Änderungen der ManagerIn Relation (Gehalt sinkt) werden nicht erkannt.
# <br><br>
# ■ Filme(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentID)
# ```
# CREATE ASSERTION NurGrosseStudios CHECK
# (10000 <= ALL
# (SELECT SUM(Länge) FROM Filme
# GROUP BY StudioName)
# );
# ```
# □ Ein Studio muss mindestens 10,000 Minuten Filmmaterial haben
# <br><br>
# ■ Alternative beim Schema für Filme
# ```
# □ CHECK (10000 <= ALL
# (SELECT SUM(Länge) FROM Filme
# GROUP BY StudioName)
# ```
# ■ Unterschied?
# <br>
# □ Beim Löschen eines Films wird die Bedingung nicht geprüft.
# <br>
# □ Beim Studiowechsel eines Films wird die Bedingung nicht geprüft.
# 
# ### Unterschiede der CHECK Bedingungen
# 
# |Constraint-Art|Wo spezifiziert?|Wann geprüft?|Gilt immer?|
# |---|---|---|---|
# |**Attribut-basiertes**|CHECK Beim Attribut|Bei INSERT in Relation oder UPDATE des Attributs|Nein, falls Subanfragen verwendet werden.|
# |**Tupel-basiertes CHECK**|Teil des Relationenschemas|Bei INSERT oder UPDATE eines Tupels|Nein, falls Subanfragen verwendet werden.|
# |**Assertion**|Teil des Datenbankschemas|Beliebige Änderung auf einer erwähnten Relation|Ja|
# 
# ### Trigger
# ■ Auch: Event-Condition-Action Rules (ECA-Rules)
# <br><br>
# ■ Unterschiede zu Zusicherungen
# <br>
# □ Gelten nicht immer, sondern werden bei bestimmten Ereignissen (INSERT, UPDATE, DELETE, Ende einer Transaktion) ausgeführt.
# <br>
# □ Ein Ereignis wird zunächst nicht verhindert, es wird lediglich ein bestimmte Bedingung geprüft.
# <br>
# – Falls falsch, passiert nichts weiter
# <br>
# □ Falls wahr, wird eine Aktion ausgeführt. Die Aktion könnte das Ereignis verhindern oder rückgängig machen.
# <br>
# Oder auch etwas völlig anderes tun.
# 
# ### Trigger in SQL
# Eigenschaften/Fähigkeiten
# <br>
# Ausführung der Aktion vor oder nach dem Ereignis
# <br>
# Die Aktion kann sich auf alte und/oder neue Werte von Tupeln beziehen, die beim Ereignis eingefügt, verändert oder gelöscht werden.
# <br>
# Mit WHEN können neben dem Ereignis auch weitere Bedingungen angegeben werden, die gelten müssen um die Aktion durchzuführen.
# <br>
# Aktion wird durchgeführt
# <br>
# Einmal für jedes veränderte Tupel oder
# <br>
# einmalig für alle Tupel, die verändert wurden
# 
# #### Trigger – Beispiel
# ```
# CREATE TRIGGER GehaltsTrigger --Name des Triggers
# AFTER UPDATE OF Gehalt ON ManagerIn --Ereignis
# REFERENCING
#     OLD ROW AS AltesTupel,
#     NEW ROW AS NeuesTupel
# FOR EACH ROW --Für jedes veränderte Tupel einmal durchführen
# WHEN (AltesTupel.Gehalt > NeuesTupel.Gehalt) --Bedingung (condition)
#     UPDATE ManagerIn --Aktion
#     SET Gehalt = AltesTupel.Gehalt
#     WHERE ManagerinID = NeuesTupel.ManagerinID; --Nur betroffenes Tupel
# ```
# ■ Was bewirkt der Trigger?
# <br>
# □ Managergehälter werden nicht gesenkt!
# <br>
# □ Rekursionsverhalten ist DBMS-Hersteller-spezifisch.
# 
# #### Trigger  –  Alternative
# ```
# CREATE TRIGGER GehaltsTrigger                   --BEFORE
# AFTER UPDATE OF Gehalt ON ManagerIn             --INSERT / DELETE (ohne OF…)
# REFERENCING
#     OLD ROW AS AltesTupel,                      --Bei INSERT nicht erlaubt
#     NEW ROW AS NeuesTupel                       --Bei DELETE nicht erlaubt
# FOR EACH ROW                                    --Default: FOR EACH STATEMENT Dann: OLD TABLE / NEW TABLE
# WHEN (AltesTupel.Gehalt > NeuesTupel.Gehalt)    --WHEN ist optional
#     UPDATE ManagerIn                            --Auch mehrere SQL Ausdrücke (BEGIN … END)
#     SET Gehalt = AltesTupel.Gehalt
#     WHERE ManagerinID = NeuesTupel.ManagerinID;
# ```
# 
# #### Trigger - Beispiel
# ```
# CREATE TRIGGER DurchschnittsgehaltTrigger
# AFTER UPDATE OF Gehalt ON ManagerIn
# REFERENCING
#     OLD TABLE AS AlteTupel --Enthält nur die alten bzw. neuen Tupel.
#     NEW TABLE AS NeueTupel
# FOR EACH STATEMENT  --Ausführung nur einmal, egal wie viele Tupel betroffen.
# WHEN (500000 > (SELECT AVG(Gehalt) FROM ManagerIn)) --Wird nach dem UPDATE geprüft.
# BEGIN
#     DELETE FROM ManagerIn
#         WHERE (Name, Adresse, ManagerID, Gehalt) IN NeueTupel; --Es werden nur veränderte Tupel entfernt und durch die alten Tupel ersetzt.
#     INSERT INTO ManagerIn
#         (SELECT * FROM AlteTupel)
# END;
# ```
# ■ Was bewirkt dieser Trigger?
# <br>
# □ Das Durchschnittsgehalt von Managern soll nicht unter 500,000 sinken!
# <br>
# □ Je ein Trigger für UPDATE, INSERT und DELETE nötig
# 
# ## Zusammenfassung
# ■ Schlüssel
#  <br>
# □ UNIQUE, PRIMARY KEY, NOT NULL 
#  <br> <br>
# ■ Referentielle Integrität
#  <br>
# □ REFERENCES, FOREIGN KEY
#  <br> <br>
# ■ Attribut-basiertes CHECK
#  <br> <br>
# ■ Tupel-basiertes CHECK
#  <br> <br>
# ■ Zusicherungen (Datenbank-basiertes CHECK)
#  <br>
# □ ASSERTION
#  <br> <br>
# ■ Trigger
# 
