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
# <img src="er_diagramm_bsp.jpg" width ="700" />

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
# <img src="mn_kardinalitaet.jpg" width="100" />
# 
# - Beispiele: Filme und Schauspieler*innen, Produkte und Kund*innen, Studierenden und Vorlesungen
# 
# 
# 
# ### 1:n Beziehungen
# 
# - **1:n Beziehungen** sagen aus, dass jede Entity des einen Typen mit maximal einem Entity des anderen Typen verbunden sein **kann**. Diese Beziehung gilt aber nur in eine Richtung. 
# 
# <img src="1n_kardinalitaet.jpg" width="100" />
# 
# - Beispiele: Ein Studio kann die Rechte an mehreren Filmen besitzen. Ein Film kann nur von einem Studio besessen werden.
# 
# - Darstellung mittels eines Pfeils zur „1er“ Seite.
# 
# 
# ### 1:n Beziehungen
# 
# - **1:1 Beziehung** sagen aus, dass jede Entity des einen Typen mit maximal einem Entity des anderen Typen verbunden sein **kann und umgekehrt**.
# 
# <img src="11_kardinalitaet.jpg" width="100" />
# 
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
# <img src="minmax-beispiel.jpg" width="500" />
# 
# 
# ### Numerische Notation (Partizipationssemantik)
# 
# Die numerische Notation ist eine vereinfachende Form, in der man ausdrück mit wie vielen Instanzen des gegenüberliegenden Typen eine Verbindung maximal aufgebaut wird. 
# 
# Im folgenden Beispiel besagt die Angabe von "n" auf der Seite der Filme, dass bis zu n Filme mit einem Studio verbunden sein können. Die "1" auf der Seite von Studio besagt, dass jeder Film mit maximal einem Studio verbunden sein kann.
# 
# 
# <img src="numerisch-beispiel.jpg" width="500" />

# In der folgenden Tabelle sind nochmal alle drei Möglichkeiten Kardinalitäten anzugeben gegenübr gestellt.
# 
# 
# |Beziehungsart|(min,max) links|(min, max) rechts| Numerisch links|Numerisch rechts|Grafische Notation|
# |-------------|---------------|-----------------|----------------|----------------|------------------|
# |many-to-many |     (0,* )    | (0,* )          |        n       |        n       |<img src="nn_notation.jpg" width="300"/>|
# |one-to-many  |     (0,* )    | (0,1 )          |        1       |        n       |<img src="1n_notation.jpg" width="300"/>|
# |many-to-one  |     (0,1 )    | (0,* )          |        n       |        1       |<img src="n1_notation.jpg" width="300"/>|
# |one-to-one   |     (0,1 )    | (0,1 )          |        1       |        1       |<img src="11_notation.jpg" width="300"/>|

# ### Totale Beziehung
# 
# Bisher haben wir hauptsächlich Beziehungstypen kennen gelernt, die auf "kann" basieren. Lediglich mit der Min-Max-Notation können wir bisher sicherstellen, dass jede Entity eines Types an einer Beziehung teilnehmen muss, in dem wir den Minimalwert auf eine Zahl größer als 0 setzen: (1,* ) bedeutet, dass jede Entity mindestens einmal an einer Beziehung teilnehmen muss. Entsprechend bedeutet (1,1), dass jedes Entity genau einmal an einer Beziehung teilnehmen muss.
# 
# Die totale Abbildung stellt man grafisch entweder durch einen offenen Pfeil auf der Seite der totalen Abbildung dar oder anhand eines Doppelstriches:
# 
# |Offener Pfeil|Doppelstrich|
# |-------------|------------|
# |<img src="1n_total_notation1.jpg" width="300"/>|<img src="1n_total_notation2.jpg" width="300"/>|
# 
# Analog kann man eine totale 1:1 Beziehung folgender Maßen darstellen:
# 
# <img src="11_total_notation.jpg" width="300"/>
# 
# 

# ### Entitytypen und Rollen

# Entitytypen können mehr als einmal in einer Relationship auftauchen, beziehungsweise kann Entitytyp durch ein Relationshiptyp mit sich selbst verbunden sein. Dabei tauchen Sie jeweils in unterschiedlichen **Rollen** auf. Die ER-Modellierung ermöglicht die explizite Modellierung von Rollen durch Annotation an den Kanten der Relationships. 
# 
# **Beispiel (Rolle 1):** Im folgenden Beispiel wird modelliert, dass Filme Fortsetzungen von einander sein können. Dabei taucht der Entitytyp Film ein mal in der Rolle des Originals und ein mal in der Rolle der Fortsetzung mit dem Relationshiptypen "ist_Fortsetzung" auf.
# 
# <img src="rolle_relationship.jpg" />

# **Beispiel (Rolle 2):** Im folgenden Beispiel taucht Studio in zwei Rollen auf: als Stammstudio und als Vertragsstudio. 
# <img src="rolle_relationship2.jpg" />
# 
# Diese Modellierung impliziert, dass das Stammstudio eines Schauspielers einem anderen Studio erlaubt den/die Schauspieler*in für einen bestimmten Film
# auszuleihen. 
# 
# 
# Mit Hilfe von Rollen vermeidet man unnötig redundante Entitytypen zu modellieren. Theoretisch könnte man jede Rolle als einen Entitytypen modellieren. Dies würde bedeuten, dass wir zwei Entitytypen mit den gleichen Attributen und höchstwahrscheinlich einer großen Überlappung von Entities haben würden. 
# 
# 

# ### n-äre Relationships

# Relationshiptypen können auch zwischen mehreren bis zu "n" Entitytypen existieren. Beispielsweise könnte man die Beziehung, dass  ein/e Schauspieler*in  bei einem Studio für eine bestimmten Film unter Vertrag steht als einen ternären Relationshiptypen wie folgt dargestellt modellieren. 
# 
# <img src="n-aer_relationships.jpg" width="500"/>
# 
# Die Instanz eines solchen Relationshiptypen kann man dann als Tripel darstellen.
# 
# 
# Normalerweise versucht man n-äre Relationshiptypen zu vermeiden, da diese schwer nachzuvollziehen sind. Insbesondere sind Kardinalitäten nicht sofort ersichtlich. In unserem Beispiel muss man genau überlegen, wie der Pfeil am Studio zu interpretieren ist. Eine mögliche Interpretation ist des Pfeiles ist, dass jede Kombination von Schauspieler*in und Film mit nur einem Studio in Beziehung stehen. Man könnte aber auch rauslesen, dass jede Schauspieler*in mit beliebig vielen Filmen aber nur einem Studio in einer Beziehung steht. Analog kann jeder Film nur mit einem Studio aber beliebig vielen Schauspieler*innen in Verbindung stehen. Um solche Mehrdeutigkeiten zu verhindern, sollte man sich bei der Modellierung auf binäre Relationshiptypen einschränken.

# ### Konvertierung in binäre Relationships

# Manchmal bietet sich im Modellierungsprozess an zunächst komplexe Relationshiptypen als n-äre Relationshiptypen zu modellieren und diese erst dann in binäre Relationshiptypen umzuwandeln. Bei dieser Konvertierung entsteht ein neuer Entitytyp welches durch binäre N:1 Relationshiptypen alle anderen Entitytypen verbindet. 
# 
# Falls ein Entitytyp mehrere Rollen spielt, entsteht pro Rolle ein Relationshiptyp.
# Attribute des Relationshiptyps werden an den neuen Entitytyp angehängt.
# 
# **Beispiel (Konvertierung in binäre Relationshiptypen):** Im folgenden haben wir unser Modell mit dem 4-ären Relationshiptypen ist_unter_vertrag von **Beispiel (Rolle 2)** in ein Modell mit nur binären Relationshiptypen umgewandelt.
# 
# | n-äre Relationshiptypen | konvertiert zu binären Relationshiptypen |
# |-------------------------|------------------------------------------|
# <img src="rolle_relationship2.jpg" width="500" /> | <img src="n-aer_relationships_konvertiert.jpg" width="500" />
# 
# Wir haben einen neuen Entitypen "Vertrag" definiert welche in N:1 Beziehung die ursprünglichen Beziehungen darstellt. Die Modellierung ist nicht vollständig äquivalent. Theoretisch könnte es nun mehrere Verträge mit der gleichen Kombination von  Studios, Schauspiler*innen und Filmen existieren. Das wären dann Vertragsduplikate. In der ursprünglichen Modellierung könnte das nicht passieren, da der Vertrag als Relationshiptyp mit entsprechenden Kardinalitäten eingeschränkt ist. 

# ### Attribute an Relationships

# In manchen Fällen ist es hilfreich, Relationships Attribute zuzuordnen. Damit stellt man sicher, dass das Attribut nur gesetzt ist, wenn eine Beziehung zwischen zwei Entitytypen existiert. 
# 
# **Beispiel:** Im folgenden Modell wird modelliert, dass in einem Vetrag ein Gehalt festgestellt wird. Eine Zuordnuung an Schauspieler*in, Film oder Studio ist hier nicht sinnvoll
# Eine Schauspieler*in könnte für verschiedene Filme unterschiedliche Gehälter bekommen. Verschiedene Schauspieler*innen könnten für den selben Film unterschiedliche Gehälter bekommen. Ein Studio könnte verschiedenen Schauspieler*innen unterschiedliche Gehälter zahlen.
# 
# <img src="attribute_relationship.jpg"  width="500"/>
# 
# 

# ## Spezielle Relationshiptypen: IST-Beziehung

# Das ER-Modell erlaubt spezielle Beziehungen, wie Subklassenbeziehungen explizit zu modellieren. Dabei wird modelliert, dass ein Entitytyp in einer Subklassenbeziehung zu einem anderen Entitytypen steht. Dabei ist die Subklasse jeweils eine Spezialisierung der oberen Klasse. Somit gibt könnte es weniger Entitäten in der Subklasse geben, die jedoch mehr spezialisiere Attribute haben und in weiteren speziellen Relationshiptypen auftauchen. 
# Im ER-Modell gibt es hierzu den Relationshiptypen IST oder is-a. Zudem wird der Relationshiptyp als Dreieck dargestellt wobei die Spitze des Dreiecks zur Superklasse zeigt. IST-Relationshiptypen haben immer eine 1:1 Kardinalität: Ein Entity der Subklasse ist auch immer Entity der Superklasse. Pfeile sind bei dieser Darstellung nicht notwendig. 
# Das ist anders als bei objekt-orientierte (OO) Modelle
# In OO sind Objekte immer einer Klassezugehörig und Subklassen erben von Superklasse.
# In ER sind Entities in allen Subklassen repräsentiert, in die sie gehören, und der jeweiligen Superklasse.
# 
# **Beispiel (ist-relationship):** In folgenden Beispiel wurde modelliert, dass jede Filmentität entweder der Subklasse Krimi oder Zeichentrickfilm beiden oder keinem angehören kann. Die Entität muss dann entsprechend in den jeweiligen Entitytypen auftauchen.
# 
# <img src="ist_relationship.jpg" WIDTH="500" />

# Beispielfilme:
# - „Krieg der Sterne“ ist weder ein Zeichentrickfilm noch ein Krimi und hat somit vier Attribute.
# - „Prinzessin Mononoke“ ist ein Zeichentrickfilm und hat somit vier Attribute und „Stimmen“-Relationships.
# - „Prisoner“ hat vier Attribute und zusätzlich das Attribut „Waffen“.
# - „Roger Rabbit“ ist sowohl ein Krimi als auch ein Zeichentrickfilm und hat somit die vier Filmattribute, zusätzlich das Attribut „Waffen“ und „Stimmen“-Relationships.

# ## Nebenbedingungen(Constraints)

# Daten unterliegen häufig bestimmten Einschränkungen und Nebenbedingungen. Nebenbedingungen dienen oft dazu Entitytypen und Relatioshiptypen eindeutig identifizieren oder einschränken zu können. 
# Zu den gebräuchlichen Nebenbedingungen gehören unter anderem Schlüssel und Fremdschlüssel. Schlüssel sind Attributkombinationen die Entities eindeutig identifizierbar machen. Fremdschlüssel andererseits stellen referenzielle Integrität her. Damit wird die Existenz von bestimmten Entitytypen von anderen abhängig. Andere Einschränkungen betreffen Wertebereiche von Attribute und Kardinalitäten. Wir werden im Folgenden die wichtigsten Nebenbedingungen, die man im Rahmen der ER-Modellierung verwendet genauer betrachten. Wichtig ist bei der Bewertung von Nebenbedingung, dass diese als Teil des konzeptionellen Entwurfes allgemeingültig definiert werden. Zufällig existierende Beziehungen in konkreten Daten können nicht automatisch zur Nebenbedingung qualifiziert werden.

# ### Schlüssel

# Ein Schlüssel ist eine (minimale) Menge von Attributen eines Entitytyps, für die gilt, dass keine zwei Entities gleiche Werte in allen Schlüsselattributen haben. Beispielsweise könnte für unseren Entitytypen Filem die Kombination aus Film und Jahr als Schlüssel fungieren. Die Wahl eines solchen Schlüssels muss mit Bedacht geschehen. Die Unterscheidbarkeit von Entities in der realen Welt muss durch die Schlüsseleigenschaften gewährleistet sein. Anderenfalls wird man ähnliche Entities nicht zeitgleich im Modell aufnehmen und von einander unterscheiden können. Würde man beispielsweise, nur den Titel eines Films als den Schlüssel auswählen, könnte man nicht mehr unterschiedliche Filme mit dem gleichen Titel von einander unterscheiden. Dabei gibt es oft Wiederverfilmungen der gleichen Geschichte mit dem gleichen Titel, wie z.B. "Hamlet", "King Kong". Die Kombination {Titel, Jahr} ist hier wahrscheinlich sinnvoller. 
# 
# Generell muss bei der ER-Modellierung für jeden Entitytypen ein Schlüssel angegeben werden. Manchmal gibt es mehrere Möglichkeiten einen Schlüssel zu definieren. Beispielsweise wird in Deutschland jede Person durch die Personalausweisnummer sowie der Steuernummer eindeutig identifiziert. Bei Modellierung von Entitytypen ist es jedoch üblich einen Primärschlüssel auszuwählen. Bei IST-Beziehungen muss die Wurzel-Superklasse sämtliche Schlüsselattribute enthalten.
# 
# 
# Schlüsselattribute werden im ER-Modell durch Unterstreichen der Attributnamen dargestellt. 
# 
# **Beispiel:** Im folgenden Beispiel haben wir für jeden Entitytypen Schlüsselattribute angegeben. Filme werden durch {Titel, Jahr} , Schauspieler\*innen durch {Name, Adresse} und Studios durch {Name} jeweils eindeutig identifziert. 
# 
# <img src="schluesselbeispiel_film.jpg" width="500" />
# 

# ### Referentielle Integrität

# Referentielle Integrität erzwingt die Zuordnung von Entities zu einem Entity eines anderen Entitytypen. Bisher haben wir N:1-Relationshiptypen betrachtet, bei denen gilt, dass eine Beziehung zwischen einem Entity der n-Seite mit höchstens einem Entitytypen der 1-Seite existiert. Aber in diese Modellierung kann ein Entity der n-Seite auch mit keinem Entity der 1-Seite in Verbingung stehen. Beispiesweise kann in unserem Film-Beispiel ein Film zu höchstens einem Studio gehören. Ein Film kann auch ohne ein Studio existieren. 
# Referentielle Integrität erzwingt die Existenz und Repräsentation des Studios. Damit stellt man sicher, dass nur Filme in der Datenbank aufgenommen werden, die auch wirklich einem Studio zugehören. 
# Das heißtl, dass das Datenbanksystem beim Einfügen/Ändern eines Films muss prüfen muss, dass ein entsprechendes Studio vorhanden ist. Weiterhin wird sicher gestellt, dass ein Studio nicht gelöscht werden darf, solange es noch Filme besitzt.
# 
# Die Darstellung von referenzieller Integrität erfolgt im ER-Modell anhand eines offenen Pfeiles. Diese Darstellung haben wir für die Modellierung von totalen Beziehungen kennen gelernt. Eine referenzielle Integrität beschreibt tatsächlich eine totale Abbildung eines Entitytypen auf einen anderen Entitytypen.

# **Beispiel:** Im folgenden Beispiel wird an zwei Stellen referenzielle Integrität erzwungen. Zunächst wird erzwungen, dass jeder Film genau einem Studio zugeordnet werden muss. Weiterhin leitet jede/r Vorsitzend/e genau ein Studio. Vorsitzende können nicht ohne Studios existieren. Ein Studio kann jedoch ohne Vorsitzende existieren. 
# 
# <img src="referentielle_integritaet.jpg" width="500"/>

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
