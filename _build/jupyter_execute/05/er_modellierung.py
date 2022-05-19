#!/usr/bin/env python
# coding: utf-8

# # ER-Modellierung

# ## Einführung: Das Entity-Relationship-Modell

# ![title](peter_chen.jpg)

# ![title](peter_chen_paper.jpg)

# Nach Peter P. Chen 1976
# <br>
# The entity-relationship model – towards a unified view of data. ACM TODS
# <br>
# Standardmodell in der frühen Entwurfsphase
# <br>
# <br>
# <br>
# Instanz eines ER-Diagramms:
# <br>
# <br>
# ER-Diagramme beschreiben Datenbanken, die eine Instanz haben (werden).
# <br>
# Der „Wert“ eines Entitytypen ist die (endliche) Menge der zugehörigen Entities.
# <br>
# Jeder Entity hat bestimmte Werte für seine Attribute.
# <br>
# Die Instanz eines n-ären Relationshiptypen ist eine Menge von Listen der Länge n.
# <br>
# Dies alles ist nur abstrakte Denkhilfe.
# <br>
# Modellierung im relationalen Modell unterscheidet sich.
# <br>
# Speicherung in einem DBMS unterscheidet sich.

# ## Begriffe (Komponenten)

# Entity
# <br>
# Ein Ding / Objekt der realen oder der Vorstellungswelt
# <br>
# Nicht direkt darstellbar, sondern nur über Eigenschaften beobachtbar
# <br>
# <br>
# Entitytyp (entity set)
# <br>
# Eine Klasse für gleichartige Objekte
# <br>
# <br>
# Relationship
# <br>
# Beschreibt Beziehungen zwischen zwei („konkreten“) Entities
# <br>
# Meist binär
# <br>
# <br>
# Relationshiptyp
# <br>
# Eine Klasse für gleichartige Beziehungen
# <br>
# Attribut
# <br>
# repräsentiert eine Eigenschaft von Entities oder von Relationships
# <br>
# Zunächst nur primitive Datenwerte (String, Integer, …) und Operationen darauf
# <br>
# Später auch komplexe Attribute

# ![title](er_diagramm_bsp.jpg)

# ### Instanz eines ER-Diagramms

# ER-Diagramme beschreiben Datenbanken, die eine Instanz haben (werden).
# <br>
# Der „Wert“ eines Entitytypen ist die (endliche) Menge der zugehörigen Entities.
# <br>
# Jeder Entity hat bestimmte Werte für seine Attribute.
# <br>
# Die Instanz eines n-ären Relationshiptypen ist eine Menge von Listen der Länge n.
# <br>
# Dies alles ist nur abstrakte Denkhilfe.
# <br>
# Modellierung im relationalen Modell unterscheidet sich.
# <br>
# Speicherung in einem DBMS unterscheidet sich.

# ![title](instanz_er.jpg)

# ## Kardinalitäten von Relationships

# Allgemein: Eine binäre Relationship kann beliebig viele Entities des einen Typen mit beliebig vielen des anderen Typen verbinden.
# <br>
# Ein Schauspieler kann in mehreren Filmen spielen.
# <br>
# In einem Film spielen mehrere Schauspieler.
# <br>
# „Kann“: D.h. nicht jeder Entity muss mit einem anderen verbunden sein.
# <br>
# In einem Animationsfilm spielen keine Schauspieler.
# <br>
# m:n Beziehung
# <br>
# Einschränkungen („Spezialfälle“)
# <br>
# 1:n Beziehung
# <br>
# 1:1 Beziehung

# ![title](mn_kardinalitaet.jpg)

# ### 1:n Relationships

# Ein Entity vom Typ E kann mit beliebig vielen Entities des Typs F verbunden sein.
# <br>
# Ein Entity vom Typ F kann mit höchstens einem Entity des Typs E verbunden sein.
# <br>
# Beispiel
# <br>
# Ein Studio kann die Rechte an mehreren Filmen besitzen.
# <br>
# Ein Film kann nur von einem Studio besessen werden.
# <br>
# „Kann“: D.h. nicht jeder Entity muss mit einem anderen verbunden sein.
# <br>
# Ein neues Studio besitzt noch keinen Film.
# <br>
# Darstellung mittels eines Pfeils zur „1er“ Seite.

# ![title](1n_kardinalitaet.jpg)

# ### 1:1 Relationships

# Ein Entity vom Typ E kann mit höchstens einem Entity des Typs F verbunden sein.
# <br>
# Ein Entity vom Typ F kann mit höchstens einem Entity des Typs E verbunden sein.
# <br>
# Beispiel
# <br>
# Ein Studio kann nur von einem Vorsitzenden geleitet werden.
# <br>
# Ein Vorsitzender kann nur ein Studio leiten.
# <br>
# „Kann“: D.h. nicht jeder Entity muss mit einem anderen verbunden sein.
# <br>
# Ein Studio kann (vorübergehend) keinen Vorsitzenden haben.

# ![title](11_kardinalitaet.jpg)

# ### Weitere Notationen

# ![title](kardinalitaeten_notation.jpg)

# Numerische Notation (Partizipationssemantik)

# ## Rolle von Relationships

# ![title](rolle_relationship.jpg)

# Entitytypen können mehr als einmal in einer Relationship auftauchen.
# <br>
# Entsprechend mehrere Kanten
# <br>
# Jede Kante entspricht einer anderen Rolle.
# <br>Die Kanten werden mit den entsprechenden Rollen annotiert.

# ![title](rolle_relationship2.jpg)

# Stammstudio eines Schauspielers erlaubt einem anderen Studio den Schauspieler für einen bestimmten Film
# auszuleihen
# <br>
# <br>
# Kardinalitäten:
# <br>
# Gegeben Schauspieler, Film und produzierendes Studio, ist das ausleihenden Stammstudio eindeutig (höchstens
# ein Studio ist das ausleihende Stammstudio).
# <br>
# Gegeben Schauspieler, Film und Stammstudio ist das produzierende Studio eindeutig (höchstens ein Studio kann
# einen Film produzieren).
# <br>
# Gegeben Schauspieler, Stammstudio und produzierendes Studio könnte es mehrere Filme geben, die in dieser
# Konstellation gedreht werden.
# <br>
# Gegeben Film, Stammstudio und produzierendes Studio könnte es mehrere Schauspieler geben, die in dieser
# Konstellation ausgeliehen werden.

# ### n-äre Relationships

# Relationships zwischen mehr als zwei Entities
# <br>
# Ein/e Schauspieler*in steht bei einem Studio für eine bestimmten Film unter Vertrag
# <br>
# Instanz der Relationship kann man als Tripel darstellen.
# <br>
# Kardinalitäten: Jede Kombination von Schauspieler und Film kann nur mit einem
# <br>
# Studio in Beziehung stehen.

# ![title](n-aer_relationships.jpg)

# ### Konvertierung in binäre Relationships

# Umwandlung n-ärer Relationships in binäre Relationships
# <br>
# Erstellung eines neuen, verbindenden Entitytyps
# <br>
# Neue n:1 Relationships zwischen dem neuen Entitytyp und den alten Entitytypen
# <br>
# Falls ein Entitytyp mehrere Rollen spielt, entsteht pro Rolle ein Relationshiptyp.
# <br>
# Attribute des Relationshiptyps werden an den neuen Entitytyp angehängt.

# ### Attribute an Relationships

# In manchen Fällen ist es hilfreich, Relationships Attribute zuzuordnen
# <br>
# Bsp: In dem Drehvertrag wird ein Gehalt festgestellt.
# <br>
# Zuordnung zu Schauspieler? Er könnte für verschiedene Filme unterschiedliche Gehälter bekommen.
# <br>
# Zuordnung zum Film? Verschiedene Schauspieler könnten unterschiedliche Gehälter bekommen.
# <br>
# Zuordnung zum Studio? Es könnte verschiedenen Schauspielern unterschiedliche Gehälter zahlen.
# 

# ![title](attribute_relationship.jpg)

# ## IST-Beziehung

# Subklasse
# <br>
# Spezialfall / Spezialisierung
# <br>
# Weniger Entities
# <br>
# Mehr Attribute
# <br>
# Eventl. mehr Relationships
# <br>
# Besonderer Relationshiptyp
# <br>
# IST (is-a)
# <br>
# Darstellung durch Dreieck
# <br>
# Spitze zeigt zur Superklasse
# <br>
# Immer 1:1
# <br>
# Trotzdem keine Pfeile

# ### IST-Beziehung als Bäume

# IST-Beziehungen nur als Bäume
# <br>
# Keine Mehrfachvererbung
# <br>
# Ein Entity kann aus mehreren Komponenten des IST-Baumes bestehen.
# <br>
# „Krieg der Sterne“ hat vier Attribute.
# <br>
# „Cinderella“ hat vier Attribute und „Stimmen“-Relationships.
# <br>
# „Der dritte Mann“ hat vier Attribute und zusätzlich das Attribut „Waffen“.
# <br>
# „Roger Rabbit“ hat vier Attribute, zusätzlich das Attribut „Waffen“ und „Stimmen“-Relationships.
# <br>
# Anders als objekt-orientierte Modelle
# <br>
# In OO sind Objekte immer in genau einer Klasse; Subklassen erben von Superklasse(n).
# <br>
# In ER sind Entities in allen Subklassen repräsentiert, in die sie gehören.
# <br>
# In ER ist ein Entity in einer Subklasse auch automatisch in den Superklassen repräsentiert.

# ## Nebenbedingungen(Constraints)

# Schlüssel
# <br>
# Ein oder mehrere Attribute
# <br>
# Werte identifizieren eindeutig ein Entity.
# <br>
# Referentielle Integrität
# <br>
# Existenz des referenzierten Entities
# <br>
# Entspricht „dangling pointer“
# <br>
# Domänen
# <br>
# Einschränkung des Wertebereichs
# <br>
# Allgemeine Nebenbedingungen (assertions)
# <br>
# Z.B. nicht mehr als 10 Schauspieler pro Film
# <br>
# Nebenbedingungen sind Teil des Schemas. Sie leiten sich nicht aus den Daten ab!

# ## Schlüssel

# Ein Schlüssel ist eine (minimale) Menge von Attributen eines Entitytyps, für die gilt, dass keine zwei Entities gleiche Werte in allen Schlüsselattributen haben.
# <br>
# Einige Attributwerte können übereinstimmen.
# <br>
# Oft nur ein Attribut
# <br>
# Für jeden Entitytyp muss ein Schlüssel angegeben werden.
# <br>
# Es kann mehr als einen Schlüssel für einen Entitytyp geben.
# <br>
# Üblich: Primärschlüssel auswählen
# <br>
# Bei IST-Beziehungen muss die Wurzel-Superklasse sämtliche Schlüsselattribute enthalten.
# <br>
# Darstellung durch Unterstreichen der Attributnamen

# ### Referentielle Integrität

# Schlüssel: Höchstens ein bestimmter Wert für ein Attribut
# <br>
# Bzw. höchstens eine Wertekombination bei mehreren Attributen im Schlüssel
# <br>
# Referentielle Integrität: Genau ein bestimmter Wert
# <br>
# Bsp. n:1 Relationship zwischen „Filme“ und „Studios“
# <br>
# Ein Film kann zu höchsten einem Studio gehören.
# <br>
# Aber ein Film muss zu keinem Studio gehören.
# <br>
# Auch wenn ein Film zu einem Studio gehört, muss dieses nicht in der DB repräsentiert sein.
# <br>
# Referentielle Integrität erzwingt die Existenz und Repräsentation des Studios
# <br>
# „Erzwingen“
# <br>
# Bei Einfügen/Ändern eines Films muss entsprechendes Studio vorhanden sein.
# <br>
# Ein Studio darf nicht gelöscht werden, solange es noch Filme besitzt.
# <br<
# Oder: Wenn ein Studio gelöscht wird, werden auch alle entsprechenden Filme gelöscht.
# <br>
# Verschiedene Einstellungen im DBMS

# ![title](referentielle_integritaet.jpg)

# ### Weitere Nebenbedingungen

# Ohne formale Notation im ER-Diagramm
# <br>
# Datentyp
# <br>
# Integer, String, …
# <br>
# Wertebereich / Domäne
# <br>
# ≤ 100, {Krimi,Doku,Zeichentrick}
# <br>
# Länge eines Attributes
# <br>
# Stringlänge < 25
# <br>
# Kardinalität von Relationships
# <br>
# Höchstens 10 Schauspieler pro Film
# <br>
# Oder mittels min/max Notation

# ## Schwache Entitytypen

# ### Motivation

# Motivation
# <br>
# In bestimmten Situationen können Entities nicht allein anhand ihrer Attribute identifiziert werden:
# <br>
# 1. Falls sie in eine nicht-IST-Hierarchie fallen.
# <br>
# 2. Entities, die zur Eliminierung n-ärer Relationships erschaffen wurden.
# <br>
# Ein Entitytyp ist schwach wenn es zur eindeutigen Identifizierung eines Entities nötig ist, eine oder mehr n:1 Relationships zu folgen und den Schlüssel der verwandten Entities hinzuzunehmen.

# ![title](schwache_ent_bsp1.jpg)

# Ein Studio beschäftigt mehrere Filmcrews.
# <br>
# Filmcrews werden mit einer Nummer versehen.
# <br>
# Verschiedene Studios könnten eigene Crews mit gleichen Nummern beschäftigen.
# <br>
# Nummer ist also kein Schlüssel
# <br>
# Nimmt man den Schlüssel der Studios hinzu ist eine eindeutige Identifizierung möglich.

# ![title](schwache_ent_bsp2.jpg)

# Eine Spezies ist definiert durch den Namen der Gattung und des Spezies.
# <br>
# Gattung: homo
# <br>
# Spezies: homo sapiens

# ![title](schwache_ent_bsp3.jpg)

# Fall 2: Auflösung einer ternären Relationship Vertrag hat kein Attribut, das Teil des Schlüssels ist.

# ![title](schwache_ent_bsp4.jpg)

# ### Schwache Entitytypen

# Man scheut sich oft einen Schlüssel zu deklarieren.
# <br>
# Die Folge: Man schwächt ein Entitytyp und macht alle seine Relationships zu unterstützenden Relationships.
# <br>
# In der Realität werden sehr oft künstliche IDs verwendet.
# <br>
# ISBN, SNN, VIN, etc.
# <br>
# Grund für das Fehlen eines solchen Schlüssels: Es gibt keine entsprechende Autorität, die einen solchen Schlüssel vergeben könnte.
# <br>
# Bsp: Es ist unwahrscheinlich, dass jedem Fußballer der Welt eine eindeutige ID zugewiesen wird.

# ### Schlüssel schwacher Entitytypen

# Falls E ein schwacher Entitytyp ist, besteht sein Schlüssel aus…
# <br>
# … null oder mehr eigenen Attributen
# <br>
# … und den Schlüsselattributen von Entitytypen, die über bestimmte n:1
# <br>
# Relationshiptypen, den „unterstützenden Relationshiptypen“ erreicht werden können.
# <br>
# Supporting relationships
# <br>
# Unterstützende Relationshiptypen
# <br>
# n:1 vom schwachen Entitytypen zu einem anderen Entitytypen
# <br>
# Es muss referentielle Integrität gelten.
# <br>
# Falls referenzierter Entitytyp wiederum schwach ist, werden (rekursiv) weitere Schlüsselattribute übernommen. 

# ## Erweitertes ER-Modell

# ### Weitere Attributarten

# ![title](weitere_attributnamen.jpg)

# Optionales Attribut
# <br>
# Attributwert nicht für jede Entität vorhanden
# <br>
# Abgeleitetes Attribut
# <br>
# Wert wird anhand einer Berechnungsvorschrift aus nicht-abgeleiteten Attributen errechnet.
# <br>
# Mengenwertiges Attribut
# <br>
# Enthält Menge von Werten
# <br>
# Strukturiertes Attribut
# <br>
# Wird durch weitere Attribute beschrieben
# <br>
# Wert des strukturierten Attributs entspricht Verkettung der Unterattribute.

# ### Spezialisierung Generalisierung

# Spezialisierung
# <br>
# entpricht IST-Beziehung
# <br>
# Drachen sind Spezialisierung von Produkt
# <br>
# Generalisierung
# <br>
# Entities in einen allgemeineren Kontext
# <br>
# Drachen oder Windspiel als Produkt
# <br>
# Partitionierung
# <br>
# mehrere disjunkte Entity-Typen
# <br>
# Spezialfall der Spezialisierung
# <br>
# Partitionierung von Produkten in Zubehör und Drachen

# ### Aggregation

# Generalisierung (IST): Gleichartige Entitytypen (is-a)
# <br>
# Aggregation: Unterschiedliche Entitytypen
# <br>
# „Teil-von“ (part-of)
# <br>
# Entity aus einzelnen Instanzen anderer Entity-Typen zusammengesetzt.

# ![title](aggregation.jpg)

# ## Designprinzipien

# Einleitungstext. 

# ### Grundprinzipien

# Treue zur Anwendung
# <br>
# Vermeidung von Redundanz
# <br>
# Einfachheit
# <br>
# Sparsamer Einsatz von Relationships
# <br>
# Sparsamer Einsatz von Attributen
# <br>
# Sparsamer Einsatz von schwachen Entitytypen

# ### Anwendungstreue

# Entitytypen und Attribute sollten Realität widerspiegeln.
# <br>
# Filme haben keine Zylinderkopfanzahl
# <br>
# Relationshiptypen sollen Verhältnisse der Realität widerspiegeln.
# <br>
# Schauspieler und Filme stehen in einer m:n Beziehung
# <br>
# n:1, 1:n oder 1:1 wären inkorrekte Wiedergaben der Realität
# <br>
# Schwierigerer Fall: Kurs und Lehrer – je nach Semantik
# <br>
# Ein Kurs kann nur von einem (verantwortlichen) Lehrer gegeben werden.
# <br>
# Lehrer geben im Team einen Kurs.
# <br>
# Nicht aktuelle Kursvergabe sondern auch Historie

# ### Redundanz

# Redundanz tritt auf, wenn der gleiche Sachverhalt auf mehr als eine Weise ausgedrückt wird.
# <br>
# Redundanz verschwendet Platz.
# <br>
# Auf dem Papier
# <br>
# Auf der Festplatte
# <br>
# Redundanz fördert Inkonsistenz.
# <br>
# Veränderung eines Sachverhalts wird nur an einer Stelle repräsentiert.

# ![title](redundanz1.jpg)

# ![title](redundanz2.jpg)

# ### Einfachheit

# KISS: Keep It Simple, St…
# <br>
# Unnötige Verwendung von Entitytypen vermeiden.
# <br>
# Ein Film wird von einer Holding repräsentiert

# ![title](einfachheit.jpg)

# ### Relationships

# Nicht jede mögliche Beziehung sollte abgebildet werden.
# <br>
# Vermeidung von Redundanz, wenn manche Beziehungen abgeleitet werden können.
# <br>
# Änderungen auf der Datenbank werden komplex
# <br>
# Eine Änderung eines Entities verursacht viele Änderungen in den Relationships.
# <br>
# Fehlergefahr
# <br>
# Vermehrter Aufwand

# ![title](relationships1.jpg)

# ![title](relationships2.jpg)

# ### Attribut vs. Element

# Attribute sind einfacher zu implementieren als Entities und Relationships.
# <br>
# Ein Entitytyp ist gerechtfertigt falls…
# <br>
# … er mehr als nur den Namen eines Objekts darstellt,
# <br>
# … oder er der n-Teil einer 1:n Relationship ist.

# ![title](attributvselement1.jpg)

# Studio ist nur ein Name
# <br>
# Studio ist nicht der n-Teil der Relationship

# ![title](attributvselement2.jpg)

# besser

# ![title](attributvselement3.jpg)

# NICHT enthalten: S. 20 , S. 34, S. 36, S. 38, S. 43-45
