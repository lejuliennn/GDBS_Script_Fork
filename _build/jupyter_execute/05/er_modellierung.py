#!/usr/bin/env python
# coding: utf-8

# # ER-Modellierung
# 
# Beim konzeptionellen Entwurf möchten wir aus einer informellen Beschreibung einer Datenbank eine formelle Beschreibung erstellen in der Mehrdeutigkeiten und jegliche Namen- und Typkonflikte behoben sowie Einschränkungen und Bedingungen sinnvoll ausgedrückt werden können. 
# 
# Eine Modellierungssprache für eine solche Modellierung ist das Entity-Relationship-Modell (ER-Modell). 
# 

# ## Einführung: Das Entity-Relationship-Modell
# 
# Die ER-Modellerung wurde 1976 von Peter Chen vorgestellt und wird seitdem als das Standardmodell für die frühe Entwurfsphase des Datenbankentwurfes verwendet.

# Original Publikation von 1976         |  Peter Chen
# :-------------------------:|:-------------------------:
# <img src="peter_chen_paper.jpg" width="400" /> | <img src="peter_chen.jpg" width="400" />
# 
# 

# Das Ergebnis einer ER-Modellierung sind ER-Diagramme, die Datenbanken beschreiben, die eine Instanz haben werden. Wir werden jetzt die zentralen Komponenten dieser Modellierungssprache und die Möglichkeiten damit Datenbedingungen und -beziehungen auszudrücken kennen lernen. 

# ## Begriffe

# ### Komponenten
# Die zentralen Komponenten der ER-Modellierung sind Entities, Entitytypen Relationships und Relationshiptypen.
# 
# 
# 
# 
# **Entity:** Ein Ding / Objekt der realen oder der Vorstellungswelt
# 
# **Relationship:** Beschreibt Beziehungen zwischen zwei („konkreten“) Entities
# - Entities und Relationships sind nicht direkt darstellbar und werden nicht explizit im Diagram sichtbar, sondern nur über Eigenschaften ihrer Klassen beobachtbar
# 
# **Entitytyp (entity set):** Eine Klasse für gleichartige Objekte
# 
# **Relationshiptyp:** Eine Klasse für gleichartige Beziehungen
# 
# Komponente| Darstellung| Visuel|
# ----------|------------|--------|
# Entitytyp |Rechteck|<img src="rechteck.jpg" />|
# Relationshiptyp |Raute|<img src="raute.jpg" />|
# Attribut | Oval | <img src="oval.jpg" />|
# 
# **Attribut:** repräsentiert eine Eigenschaft von Entities oder von Relationships
# - Es gibt Attribute die nur aus primitiven Datenwerten (String, Integer, …) und Operationen darauf bestehen und auch komplexere zusammengesetzte Attribute, die wir in dieser Vorlesung jedoch nicht detailliert behandeln werden. Komplexe Attribute werden dem Erweiterten ER-Modell zugeordnet. 
# 
# Attribute an Entitytypen: 
# <img src="entitytypattribut.jpg" />
# 
# Attribute an Relationshiptypen:
# <img src="relationshiptypattribut.jpg" />

# **Beispiel:** Im folgenden Diagram wollen wir Informationen über Filme, Schauspieler*innen und Studios modellieren. 
# - Ein Film enthält daten über Titel, Jahr, Länge und Typ. 
#     - Dargestellt über einen Entitytypen und vier Attribute
# - Über Schauspieler*innen sollen Name und Adresse gespeichert werden
#     - Dargestellt über einen Entitytypen und zwei Attribute
# - Über Studios sollen Name und Adressen gespeichert werden.
#     - Dargestellt über einen Entitytypen und zwei Attribute
# - Es soll abgebildet werden dass Schauspieler*innen in Filmen mitspielen.
#     - Dargestellt über einen Relatioshiptypen der Filme und Schauspieler*innen verbindet
# - Es soll dargestellt werden, dass Studios die Rechte an Filmen besitzen. Insbesondere soll ein Film genau einem Studio gehören. 
#     - Dargestellt über einen Relatioshiptypen der Filme und Studios verbindet. Den letzten Punkt über "genau einem Studio" werden wir später im Kontext von Kardinalitäten genauer betrachten. 
# 
# <img src="er_diagramm_bsp.jpg" width =700 />

# ### Instanz eines ER-Diagramms

# Wie bereits gesagt beschreiben ER-Diagramme Datenbanken, die eine Instanz haben (werden).
# Dabei gilt, dass der „Wert“ eines Entitytypen die (endliche) Menge der zugehörigen Entities ist. Jeder Entity hat bestimmte Werte für seine Attribute, z.B., Baisc Instinct = {Titel=Basic Instinct, Jahr = 1992, Länge = 127, Typ = Farbe}. Die Instanz eines n-ären Relationshiptypen ist eine Menge von n-Tupel, z.B spielt_in_instanz_1= (Basic Instinct, Sharon Stone).
# Dies alles ist an dieser Stelle nur abstrakte Denkhilfe. Die Modellierung im relationalen Modell wird sich nochmal unterscheiden, sodass sich die Abspeicherung durch ein DBMS auch unterscheiden wird. 
# 
# **Beispiel:** Die Folgenden Tabellen stellen die Instanzen eines Teiles unseres Modells in der finalen Datenbank im **relationalen Modell** (als Tabellen) dar. 
# 
# 
# <table>
# <tr><th>Filme</th><th></th><th>Schauspieler*in</th><th></th><th>spielt_in</th></tr>
# <tr><td>
# 
# 
# |Titel|Jahr |Länge|Typ|
# |------|----|------|----|
# |Basic Instinct |1992|127|Farbe|
# |Schindler's List |1993|187| S/W|
# |Django Unchained| 2012|165| Farbe|
# 
# </td><td>
# </td><td> 
# 
# |Name|Adresse|
# |----|-------|
# |Sharon Stone|Hollywood|
# |Johnny Depp |Paris|
# |Jaimie Foxx| Hidden Valley|
#     
# </td><td> 
# </td><td> 
#     
# |Name|Titel|
# |----|-------|
# |Sharon Stone|Baisc Instinct|
# |Johnny Depp |Dead Men|
# |Jaimie Foxx| Django Unchained|
#     
# </td></tr> </table>

# ## Kardinalitäten von Relationshiptypen

# Allgemein: Ein binärer Relationshiptyp kann beliebig viele Entities des einen Typen mit beliebig vielen des anderen Typen verbinden. Betrachten wir zum Beispiel unsere Beispieldatenbank über Filme. Hier kann eine Schauspieler*in in mehreren Filmen mitspielen und gleichzeitig mehrere Schauspieler*innen in einem einzigen Film. Hierbei nutzen wir bewusst "kann", da nicht jede Entity mit einem anderen Entity des jeweiligen typen verbunden sein muss. Beispielsweise spielen in Animationsfilme keine Schauspieler*innen. Anders ist es bei Relationshiptypen, bei denen eine Verbindung erzwungen werden muss. Beispielsweise muss jeder Film von einem Studio produziert werden - in diesem Fall sogar von genau einem Studio.
# 
# Man kann diese Kardinalitäten im ER-Modell genau spezifizieren. Es gibt im Allgemeinen drei häufige Kardinalitäten:
# 
# ### m:n Beziehungen
# - **m:n Beziehungen** sagen aus, dass jede Entity des einen Typen mit keinem oder mehreren Entities des anderen typen verbunden sein kann.
# 
# <img src="mn_kardinalitaet.jpg" width=100/>
# 
# - Beispiele: Filme und Schauspieler*innen, Produkte und Kund*innen, Studierenden und Vorlesungen
# 
# 
# 
# ### 1:n Beziehungen
# 
# - **1:n Beziehungen** sagen aus, dass jede Entity des einen Typen mit maximal einem Entity des anderen Typen verbunden sein **kann**. Diese Beziehung gilt aber nur in eine Richtung. 
# <img src="1n_kardinalitaet.jpg" width=100/>
# - Beispiele: Ein Studio kann die Rechte an mehreren Filmen besitzen. Ein Film kann nur von einem Studio besessen werden.
# 
# - Darstellung mittels eines Pfeils zur „1er“ Seite.
# 
# 
# ### 1:n Beziehungen
# 
# - **1:1 Beziehung** sagen aus, dass jede Entity des einen Typen mit maximal einem Entity des anderen Typen verbunden sein **kann und umgekehrt**.
# 
# <img src="11_kardinalitaet.jpg" width=100/>
# - Beispiel: Ein Studio kann nur von einer Vorsitzenden geleitet werden. Eine Vorsitzende kann nur ein Studio leiten. Auch hier gilt immernoch "kann". Wir werden eine Notation für eine totale Abbildung, d.h., wo die Beziehung stattfinden muss, noch kennen lernen. In unserem Beispiel kann ein Studio theoretisch (vorübergehend) keinen Vorsitzenden haben.
# - Darstellung mittels eines Pfeils zu beiden Seiten.
# 

# ## Weitere Notationen für Kardinalitäten
# 
# Sie werden in der Literatur verschiedene Notationen für die Darstellung von Kardinalitäten finden. Diese sind unterschiedlich mächtig. Bisher haben wir lediglich die grafische Notation kennen gerlernt, die über Pfeiltypen ausgedrückt wird. Eine Verbindung ohne ein Pfeil eine beliebige Anzahl von verbindungen also "n" suggeriert und ein Pfeil maximal eine Verbindung also "1". Diese Notation lässt noch keine Nebenbedingungen hinsichtlich konkreter "n"-Werte zu.
# Im folgenden werden wir noch die Min-Max-Notation und Numerische Notation kennen lernen. 
# 
# 
# ### Min-Max-Notation (Look-Up-Semantik)
# 
# Die Min-Max-Notation schränkt die möglichen Teilnahmen von Instanzen der beteiligten Entitytypen an der Beziehung ein. Insbesondere drückt sie aus wie häufig eine Instanz minimal bzw. maxima. an einer Beziehung teilnimmt. Die Notation ist (Min,Max) an der Seite des Entitytypen. 
# 
# Im folgenden Beispiel sagt (0,1) an der Seite des Produktes aus, dass ein Produkt entweder in einem oder keinem Regal gelagert wird. Andersherum sagt (0,3) auf der Seite des Regals aus, dass in einem Regal 0 bis 3 unterschiedliche Produkte gelagert werden können. 
# 
# <img src="minmax-beispiel.jpg" width=500/>
# 
# 
# ### Numerische Notation (Partizipationssemantik)
# 
# Die numerische Notation ist eine vereinfachende Form, in der man ausdrück mit wie vielen Instanzen des gegenüberliegenden Typen eine Verbindung aufgebaut wird. 
# 
# 
# <img src="numerisch-beispiel.jpg" width=500/>

# <img src="kardinalitaeten_notation.jpg" width=500 />

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
