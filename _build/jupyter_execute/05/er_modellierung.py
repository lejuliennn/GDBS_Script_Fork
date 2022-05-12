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

# ## Rolle von Relationships

# Entitytypen können mehr als einmal in einer Relationship auftauchen.
# <br>
# Entsprechend mehrere Kanten
# <br>
# Jede Kante entspricht einer anderen Rolle.
# <br>Die Kanten werden mit den entsprechenden Rollen annotiert.

# ![title](rolle_relationship.jpg)

# ![title](rolle_relationship2.jpg)

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
