#!/usr/bin/env python
# coding: utf-8

# # Architektur

# Einführungstext.

# ## Schichtenmodell

# ![title](schichtenmodell.jpg)

# ■ Interne (physische) Schicht/Sicht
# <br>
# □ Speichermedium (Tape, Festplatte)
# <br>
# □ Speicherort (Zylinder, Block)
# <br>
# Datei(en), Seiten, Blocks
# <br>
# <br>
# ■ Konzeptionelle (logische) Schicht/Sicht
# <br>
# □ Unabhängig von physischer Schicht
# <br>
# □ Definiert durch Datenmodell
# <br>
# □ Stabiler Bezugspunkt für interne und externe Schichten
# <br>
# □ Schema: Relationen, Attribute, Typen,
# Integritätsbedingungen
# <br>
# <br>
# ■ Externe (logische) Schicht/Sicht
# <br>
# □ Anwendungsprogramme
# <br>
# □ Nur auf die relevanten Daten
# <br>
# □ Enthält möglicherweise Aggregationen und Transformationen
# <br>
# „SQL Views“ (Sichten)
# <br>
# □ Anwendungen
# <br>
# <br>

# ## Systemarchitekturen

# ■ Beschreibung der Komponenten eines Datenbanksystems
# <br>
# ■ Standardisierung der Schnittstellen zwischen Komponenten

# ##### ANSI-SPARC-Architetktur

# ![title](ansi-sparc-architektur.jpg)

# ANSI-SPARC-Architektur worum gehts allgemein:
# <br>
# <br>
# ■ ANSI: American National Standards Institute
# <br>
# ■ SPARC: Standards Planning and Requirements Committee
# <br>
# ■ DBMS Architekturvorschlag von 1975
# <br>
# ■ 3-Schichten-Architektur verfeinert
# <br>
# □ Interne Ebene / Betriebssystem verfeinert
# <br>
# □ Mehrere interaktive und Programmier-Komponenten
# <br>
# □ Schnittstellen bezeichnet und normiert

# ANSI-SPARC-Architektur was für Komponenten gibt es:
# <br>
# ■ Definitionskomponenten 
# <br>
# □ DDL, Sichten, Dateiorganisation, Indizes
# <br>
# <br>
# ■ Programmierkomponenten 
# <br>
# □ Entwicklungsumgebung und Programmiersprache 
# <br>
# □ Integration von DB-Operationen 
# <br>
# <br>
# ■ Benutzerkomponenten 
# <br>
# □ Anfrageinterface für Experten 
# <br>
# □ DB-Anwendungen für Laien 
# <br>
# <br>
# ■ Transformationskomp. 
# <br>
# □ Anfrageausführung und Darstellung der Ergebnisse
# <br>
# <br>
# ■ Data Dictionary 
# <br>
# □ Metadaten (in relationalen Systemtabelle)

# Notiz: aktuelle Relevanz
