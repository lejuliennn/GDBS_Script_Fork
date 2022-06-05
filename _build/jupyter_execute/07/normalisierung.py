#!/usr/bin/env python
# coding: utf-8

# # Normalisierung

# ### Motivation
# <br>
# Bisher haben wir eine direkte Übersetzung von ER-Diagrammen in das relationale Modell behandelt. Dabei sind wir davon ausgegangen, dass das Ursprungsmodell sinnvoll erstellt und alle dazugehörigen Kardinalitäten sinnvoll auch im Sinne der Vermeidung von Redundanz modelliert wurden. In der Realität kann man aber nicht immer davon ausgehen, dass die Modellierung fehlerfrei durchgeführt wird. Zudem kann es nachdem konzeptionellen Entwurf zu Veränderungen hinsichtlich der Nutzung der Daten und den beziehungen zwischen den ursprünglichen Entitytypen und Relationshiptypen kommen, die zu Problem führen können. Insbesondere könnten vorher unbekannte funktionale Abhängigkeiten sichtbar werden, die eine Verfeinerung des (logischen) Entwurfes erfordern. 

# ### Beispiel
# 
# In der folgenden Filmtabelle werden Informationen zu Filmen abgespeichert. Bei der Modellierung wurde darauf geachtet, dass die Tabelle einen Schlüssel und mehrere Attribute hat. 
# 

# |FilmID|Titel|Länger|Genre|Studio|Produktionsland|
# |-----|-----|------|-----|-------|--------|
# |1|Matrix I|136|SciFi|Warner Bros.|USA|
# |2|Lord of the Rings I|178|Fantasy|Warner Bros.|USA|
# |3|The Breakfast Club|97|Drama|Universal|USA|

# Bei diesem Beispiel fällt auf, dass bestimmte Informationen mehrfach auftauchen. Insbesondere ist das bei Studio und USA der Fall. Es stellt sich heraus, dass das Produktionsland vom Studionamen abhängt. Dies ist nicht nur zufällig in dieser dargestellten Tabelle so, sondern konzeptionell auch begründet werden. Die Produktion wird dem Land zugerechnet, in dem sich das Studio befindet. 
# An und für sich ist das kein großes Problem. Oft werden solche Abhängigkeiten hingenommen. Wenn wir jedoch eine Minimierung von Redundanz bei unserer Modellierung vornehmen wollen, müssen wir diese Abhängigkeit nutzen um Informationen die herleitbar sind nicht wiederholt zu speichern. Eine redundante Speicherung solcher Informationen kann dazu führen, dass bei zukünftigen Änderungen der Daten, die Abhängigkeit nicht in Betracht gezogen wird und Inkonsistenzen entstehen, die unsere nun erkannte Beziehung verletzen könnten.
# Die folgende Darstellung weist dieses Problem nicht mehr auf.

# ### Filmtabelle
# 
# |FilmID|Titel|Länger|Genre|Studio|
# |-----|-----|------|-----|-------|
# |1|Matrix I|136|SciFi|Warner Bros.|
# |2|Lord of the Rings I|178|Fantasy|Warner Bros.|
# |3|The Breakfast Club|97|Drama|Universal|
# 

# ### Studiotabelle
# 
# |Studio|Produktionsland|
# |-----|-----|
# Warner Bros.|USA|
# Universal|USA|

# Jetzt haben wir die Informationen zu jedem Studio in einer separaten Tabelle ausgelagert. Die Beziehung zwischen den Filmen ist über den Studionamen erhalten worden. Die neue Modellierung würde uns auch erlauben weitere Informationen pro Studio zu speichern ohne diese jeweils für jeden Film zu wiederholen. Es stellt sich heraus, dass in der neuen Studiotabelle das Attribut Studio die Funktion des Schlüssels übernommen hat. Das heißt, dass jeder Studioname nur ein mal vorkommt und die jeweiligen Studioeigenschaften genau bestimmt. Es gibt auch weitere Auswirkungen: Insbesondere können jetzt Studios unabhängig von Filmen existieren. Auch verschwinden Studios nicht aus unserer Datenbank, wenn wir die jeweiligen Filme löschen. In der usprünglichen Version hatten wir nur jede Studios für die wir auch Filme abgespeichert hatten. 
# 
# Was wir in diesem Beispiel getan haben ist eine Relation zu dekomponieren. Dafür haben wir die funktionale Abhängigkeit zwischen Studioname und Produktionsland verwendet. Im folgenden werden wir diese Konzepte genauer besprechen um ein systematisches Vorgehen für die Dekomposition von Relationen herzuleiten.

# ## Funktionale Abhängigkeiten (FDs)

# Funktionen kennen Sie aus der Mathematik. Funktionen sind Abbildungen von Elementen einer Menge (Definitionsbereich) auf Elemente einer anderen Menge (Wertebereich), wobei jedem Element des Definitionsbereiches genau ein Element aus dem Werte Bereich zugeordnet wird. Die linke Abbildung unten zeigt den Graphen einer mathematischen Funktion. Die rechte Abbildung stellt jedoch keine Funktion dar, da einem X-Wert mehrere A-Werte zugeordnet wurden. Funktionale Abhängigkeiten folgen einer analogen Definition wie folgt. 

# 
# <img src="funktionen.jpg" alt="Funktionen" width="500"/>

# **Definition – Funktionale Abhängigkeit** Gegeben eine Relation mit einer Attributmenge $X \subset R$ und einem Attribut $A \in R$, dann ist $X \rightarrow A$ eine funktionale Abhängigkeit wenn gilt, dass immer wenn zwei Tupel in den Werten der Attributmenge X übereinstimmen, stimmen sie auch im Attributwert
# für A überein.

# **Notation:**
# - Begriffe: Funktionale Abhängigkeit oder FA, oder Functional Dependency oder FD
# - …, X, Y, Z sind Attributmengen
# - A, B, C, … sind Attribute
# - X → A: „X bestimmt A funktional.“
# - Kurzform: ABC statt {A, B, C}
# - Kurzform: Falls X → A, X → B, X → C schreiben wir auch X → ABC oder auch X → Y
# 
# **Beispiele:**
# 
# - Titel, Jahr $\rightarrow$ Länge
# - FilmID $\rightarrow$ Titel
# - Studio $\rightarrow$ Produktionsland
# 

# ### Dekomposition und Vereinigung

# Bevor wir funktionale Abhängigkeiten einsetzen, wollen wir noch einige nützliche Transformationsregeln kennen lernen. 
# 
# 
# **Dekompositionsregel** $A_1,A_2,…A_n \rightarrow B_1,B_2,…,B_m \Rightarrow  \forall i \in [1:m]. A_1,A_2,…A_n \rightarrow B_i$
# Die Dekompositionsregel besagt, dass wir jede FD mit mehr als einem Attribut auf der rechten Seite auch als eine Menge von FDs aufschreiben können, die jeweils immer die gleiche linke Seite aber nur eine Teilmenge bzw. nur ein Element aus der ursprünglichen rechten Seite aufzeigen. Mit dieser Regel können wir FDs vereinfachen und weitere Eigenschaften, wie zum Beispiel Minimalität (wird später erklärt) leichter prüfen.
# 
# **Vereinigungsregel** $ \forall i \in [1:m]. A_1,A_2,…A_n \rightarrow B_i \Rightarrow  A_1,A_2,…A_n \rightarrow B_1,B_2,…,B_m$
# Die Vereinigungsregel zeigt, dass die Umkehrung der Dekomposition möglich ist. Wir können alle FDs, die genau die gleiche Menge an Attributen auf der linken Seite aufzeigen zu einer FD zusammenfassen, indem wir die Attribute der rechten Seite aller ursprünglichen FDs vereinigen. Diese Regel dient der Zusammenfassung und Darstellbarkeit von FDs.
# 
# 
# **Beispiel**
# - Titel, Jahr → Länge 
# - Titel, Jahr → Typ
# - Titel, Jahr → StudioName 
# - $\Leftrightarrow$ Titel, Jahr → Länge, Typ, StudioName 
# 
# ■ Beide zuvor genannte Regeln funktionieren nur für die rechte Seite von FDs. Wir können nicht die linke Seite wie im folgenden Beispiel gezeigt dekomponieren. 
#   
# Titel, Jahr → Länge $\not\Rightarrow$ Titel → Länge $\vee$ Jahr → Länge

# ### Triviale FDs

# ■ Trivial: Attribute rechts sind Teilmenge der Attribute links
# <br>
# □ Titel, Jahr → Titel
# <br>
# □ Es gilt immer für jede triviale FD:
# <br>
# – „Zwei Tupel, die in einer Menge von Attributen übereinstimmen, stimmen auch in einem dieser Attribute überein.“
# <br><br>
# ■ Nicht-trivial: Wenigstens ein Attribut rechts kommt links nicht vor.
# <br>
# □ Titel, Jahr → Jahr, Länge
# <br><br>
# ■ Völlig nicht-trivial: Die Attribute links und rechts sind disjunkt.
# <br>
# □ Titel, Jahr → Länge
# <br>
# □ Im Weiteren interessieren uns nur diese.
# <br><br>
# ■ Formal: Triviale-Abhängigkeitsregel
# <br>
# □ A1,A2,…An → Ai1, …, Aik,B1,B2,…,Bm
# <br>
# <=>
# <br>
# A1,A2,…An → B1,B2,…,Bm

# ![title](tabelle.jpg)

# ■ Titel, Jahr → Länge
# <br>
# ■ Titel, Jahr → Typ
# <br>
# ■ Titel, Jahr → StudioName
# <br>
# ■ Titel, Jahr → Länge, Typ, StudioName
# <br>
# ■ Wenn zwei Tupel den gleichen Titel und das gleiche Jahr haben, dann haben sie auch gleiche Länge, gleichen Typ und gleichen Studionamen.
# <br>
# □ Klar, denn Titel und Jahr sind Schlüssel für die ursprüngliche Film-Relation: Gegeben Titel und Jahr haben wir einen eindeutigen Film, der wohl auch eine eindeutige Länge und Typ hat.
# <br>
# □ Wegen 1:n Beziehung zwischen Studios und Filmen ist auch zu erwarten, dass das Studio eindeutig ist.
# <br>
# ■ Aber Titel, Jahr → SchauspName ist falsch! Warum?

# ### Schema vs. Instanz

# ![title](tabelle.jpg)

#  FDs sind Aussagen über das Schema, nicht die Instanz!
#  <br>
# ■ Titel → Typ scheint zu gelten
#  <br>
# □ Aber nur zufällig bei dieser Instanz
#  <br>
# □ Wenn zwei Filme im Titel übereinstimmen, stimmen sie (hier!) auch im Typ überein.
#  <br>
# □ Gegenbeispiel: King Kong von 1924 vs. King Kong von 2005.
#  <br>
# ■ Titel, Jahr → Typ gilt hingegen

# ![title](kingkong.jpg)

# ### Schlüssel als Spezialfall einer FD

# ■ Eine Menge aus einem oder mehr Attributen {A1, A2, …, An} ist Schlüssel der Relation R, falls gilt:
# <br>
# □ Die Attribute bestimmen alle anderen Attribute funktional.
# <br>
# – Anmerkung: Relationen sind Mengen, es kann also keine zwei völlig identischen Tupel geben.
# <br>
# □ Keine echte Teilmenge von {A1, A2, …, An} bestimmt alle anderen Attribute funktional.
# <br>
# – Anmerkung: Ein Schlüssel muss also minimal sein.
# <br><br>
# ■ Ziel des Datenbankentwurfs: Normalisierung
# <br>
# □ Alle gegebenen FDs in „Schlüsselabhängigkeiten“ umformen, ohne dabei semantische Information zu verlieren.
# <br>
# □ Umformung durch Dekomposition von Relationen
# <br>
# □ Später, denn zunächst: Bestimmung aller FDs

# ![title](tabelle.jpg)

#  {Titel, Jahr, SchauspName} ist ein Schlüssel.
#  <br>
#  <br>
# ■ {Titel, Jahr} bestimmen Länge, Typ und Studioname funktional.
# <br>
# <br>
# ■ Deshalb können keine zwei Tupel gleiche Werte für Titel, Jahr und SchauspName haben. Sie
# wären insgesamt identisch.
# <br>
# <br>
# ■ Teilmengen?
# <br>
# □ {Titel, Jahr} bestimmen SchauspName nicht funktional
# <br>
# □ {Jahr, SchauspName} bestimmen Titel nicht funktional
# <br>
# □ {Titel, SchauspName} bestimmen Jahr nicht funktional
# <br>
# – Beispiele?

# ### Schlüssel und Superschlüssel

# ■ Eine Relation kann mehr als einen Schlüssel besitzen.
# <br>
# □ Wahl eines der Schlüssel als Primärschlüssel
# <br><br>
# ■ Eine Attributmenge, die einen Schlüssel enthält, ist ein Superschlüssel.
# <br>
# □ {Titel, Jahr, SchauspName} ist ein Schlüssel und ein Superschlüssel
# <br>
# □ {Titel, Jahr, Länge, SchauspName} ist ein Superschlüssel
# <br>
# – Nicht minimal
# <br>
# ■ Minimal vs. kleinster
# <br>
# □ Minimaler Schlüssel: Kein Attribut darf fehlen
# <br>
# – Ist nicht unbedingt kleinster Schlüssel
# <br>
# □ Kleinster Schlüssel: Schlüssel mit wenigsten Attributen
# <br>
# – Ist auch minimal
# <br><br>
# ■ Alternative Begriffe:
# <br>
# □ Schlüssel (=Superschlüssel)

# ### Wo kommen FDs her?

# ■ Einfach den Schlüssel K deklarieren.
# <br>
# □ Dann gelten (einzig) die FDs K → A für jedes Attribut A.
# <br><br>
# ■ FDs deklarieren.
# <br>
# □ Dann systematisch Schlüssel ableiten.
# <br><br>
# ■ FDs aus der Physik
# <br>
# □ Zwei Kurse können nicht zur gleichen Zeit im gleichen Raum stattfinden.
# <br>
# □ Zeit, Raum → Kurs
# <br>
# ■ FDs aus dem ER-Diagramm
# <br>
# □ Schlüsselattribute
# <br>
# □ 1:n Beziehungen

# ### Schlüssel aus ER-Diagrammen

# ■ Falls die Relation von einem Entitytypen stammt
# <br>
# □ Der Schlüssel der Relation besteht aus den Schlüsselattributen des Entitytypen.
# <br><br>
# ■ Falls die Relation von einem Relationshiptypen stammt
# <br>
# □ m:n: Schlüssel besteht aus den Schlüsselattributen der verbundenen Entitytypen.
# <br>
# □ 1:n: Schlüssel besteht aus den Schlüsselattributen des Entitytypen der n-Seite.
# <br>
# □ 1:1: Zwei mögliche Schlüssel
# <br>
# – Schlüssel der beiden beteiligten Entitytypen. Wahl eines der beiden Schlüssel als Primärschlüssel (egal
# welcher).
# <br><br>
# ■ Bei n-ären Relationshiptypen
# <br>
# □ Lage ist komplizierter
# <br>
# □ 1-Seite muss nie am Schlüssel beteiligt sein.

# ![title](er_diagramm1.jpg)

# ■ $Filme(\underline{Titel, Jahr}, Länge, Typ)$
# <br>
# ■ $Schauspieler*in(\underline{Name, Adresse})$
# <br>
# ■ $Studio(\underline{Name}, Adresse)$
# <br>
# ■ $besitzt(\underline{Titel, Jahr}, Name)$
# <br>
# □ -> zusammengefasst mit Filme zu Film $(\underline{Titel, Jahr}, Länge, Typ, StudioName)$
# <br>
# ■ $spielt_in(\underline{Titel, Jahr, Name, Adresse}, Gehalt)$

# ### Schlüssel aus ER-Diagrammen

# ![title](er_diagramm2.jpg)

#  $Studios(\underline{SName})$
#  <br>
# ■ $Vorsitzende(\underline{VName})$
# <br>
# ■ $leitet(\underline{SName}, VName)$ oder leitet$(SName, \underline{VName})$
# <br>
# □ sprich, zwei Schlüssel: SName und VName, ein Schlüssel als Primärschlüssel gewählt
# <br>
# □ -> zusammengefasst zu $Studios(\underline{SName}, VName)$ oder $Vorsitzende(\underline{VName}, SName)$

# ### Schlüssel aus ER-Diagrammen: n-äre Relationshiptypen

# ![title](n-aer_relationshiptypen1.jpg)

#  $Studio (\underline{Name}, Adresse)$
#  <br>
# ■$ Schauspieler*in (\underline{Name}, Adresse)$
# <br>
# ■ $Film (\underline{Titel, Jahr}, Typ, Länge)$
# <br>
# ■ $ist_unter_Vertrag (\underline{SchauspielerName, Titel, Jahr}, StudioName, Gehalt)$

# ![title](n-aer_relationshiptypen2.jpg)

# ■ $Studio(\underline{Name}, Adresse)$
# <br>
# ■ $Schauspieler(\underline{Name}, Adresse)$
# <br>
# ■ $Film(\underline{Titel, Jahr}, Typ, Länge)$
# <br>
# ■ $Vertrag(\underline{SchauspielerName, StudioName, Titel, Jahr}, Gehalt)$

# ### Schlüssel aus ER-Diagrammen: IST-Hierarchien

# ![title](IST_hierarchie.jpg)

# ■ ER-Stil
# <br>
# □ $Film(\underline{Titel, Jahr}, Länge,Typ)$
# <br>
# □ $Krimi(\underline{Titel, Jahr}, Waffen)$
# <br>
# □ $Zeichentrickfilm(\underline{Titel, Jahr})$
# <br><br>
# ■ OO-Stil
# <br>
# □ $Film(\underline{Titel, Jahr}, Länge, Typ)$
# <br>
# □ $FilmZ(\underline{Titel, Jahr}, Länge, Typ)$
# <br>
# □ $FilmK(\underline{Titel, Jahr}, Länge, Typ, Waffen)$
# <br>
# □ $FilmZK(\underline{Titel, Jahr}, Länge, Typ, Waffen)$
# <br><br>
# ■ Mit NULL-Werten
# <br>
# □ $Film(\underline{Titel, Jahr}, Länge, Typ, Waffen)$

# ## Ableitungsregeln für FDs

# ### Motivation

# ■ Gegeben eine Menge von FDs, kann man eventuell weitere FDs ableiten.
# <br>
# <br>
# ■ Ziel des Datenbankentwurfs:
# <br>
# □ Alle gegebenen und abgeleiteten FDs in „Schlüsselabhängigkeiten“ umformen, ohne dabei semantische Information zu verlieren.
# <br>
# □ Umformung durch Dekomposition von Relationen

# ### Ableitung von FDs – Beispiel

# ![title](ableitung_fd1.jpg)

# ■ Es gelte A → B und B → C
# <br>
# <br>
# ■ Dann gilt auch: A → C
# <br><br>
# ■ Beweis
# <br>
# □ Z.z.: Zwei beliebige Tupel, die in A übereinstimmen, müssen auch in C übereinstimmen.
# <br>
# □ Zwei solche beliebige Tupel, die in A übereinstimmen:
# <br>
# (a, b1, c1) und (a, b2, c2)
# <br>
# □ Da A → B => (a, b, c1) und (a, b, c2)
# <br>
# □ Da B → C => (a, b, c) und (a, b, c)
# <br>
# □ QED
# <br><br>
# ■ Instanz genügt A→B und B→C
# <br>
# □ Es gilt auch: A→C
# <br>
# □ Nicht ableitbar: C→A, B→A oder C→B

# ### FD-Mengen

# ■ Zwei Mengen S und T an FDs heißen äquivalent, falls die Menge der gültigen Instanzen unter S die gleiche wie
# unter T ist.
# <br><br>
# ■ Eine Menge S an FDs folgt aus einer Menge T an FDs, falls jede unter T gültige Instanz auch unter S gültig ist.
# <br><br>
# ■ Hüllenbildung:
# <br>
# □ Ableitung aller FDs aus einer gegebenen Menge an FDs
# <br>
# □ Gemäß Ableitungsregeln
# <br>
# □ Auch: attribute closure, closure, Attributabschluss

# ### Hülle

# ■ Gegeben eine Menge von Attributen A1,A2,…,Ak und eine Menge S von FDs.
# <br>
# ■ Die Hülle von A1,A2,…,Ak unter S ist die Menge Y aller Attribute für die gilt, dass für jede unter S gültige Relation auch A1,A2,…,Ak → Y gilt.
# <br>
# □ Menge der funktional ableitbaren Attribute
# <br>
# □ D.h. A1,A2,…Ak → Y folgt aus den FDs in S.
# <br>
# ■ Notation: Hülle von A1,A2,…,Ak ist $\{$A1,A2,…,Ak$\}^+$.
# <br>
# ■ Es gilt z.B. Ai $\in$ $\{$A1,A2,…,Ak$\}^+$ für i=1,…,k
# <br>
# □ Trivialerweise, denn A1,A2,…, Ai, …, Ak→ A

# ### Berechnung der Hülle

# ![title](berechnung_huelle.jpg)

# 1. Sei X die Menge der Attribute, die später die Hülle wird.
# <br>
# Initialisiere X mit {A1,A2,…Ak}.
# <br>
# 2. Suche wiederholt nach solchen FDs B1,B2,…,Bm→ C, dass B1,B2,…,Bm $\in$ X aber C $\notin$ X.
# <br>
# 3. Füge C zu X hinzu.
# <br>
# 4. Wiederhole 2. bis keine Attribute mehr gefunden werden
# <br>
# ■ Terminierung: X wächst nur, und Attributmenge ist endlich.
# <br>
# 5. X ist schließlich die Hülle, also $\{$A1,A2,…Ak$\}^+$ = X.

# ■ Relation mit Attributen A, B, C, D, E, F
# <br>
# <br>
# ■ Gegeben FDs
# <br>
# 1. AB → C
# <br>
# 2. BC → AD
# <br>
# 3. D → E
# <br>
# 4. CF → B
# <br>
# <br>
# ■ Gesucht: Hülle von {A, B}, also {A,B$\}+$
# <br>
# □ FD 1: X = {A, B, C}
# <br>
# □ FD 2: X = {A, B, C, D}
# <br>
# □ FD 3: X = {A, B, C, D, E} ( = {A,B$\}^+$ )

# ### Membership-Problem

# ■ Kann eine bestimmte FD X→Y aus der gegebenen FD Menge abgeleitet werden?
# <br><br>
# ■ Vorgehen: Berechne Hülle von X und teste ob Y darin enthalten ist.
# <br><br>
# ■ Beispiel:
# <br>
# □ AB → C und BC → AD und D → E und CF → B
# <br>
# □ Kann AB → D abgeleitet werden?
# <br>
# – {AB$\}^+$ = {A, B, C, D, E}
# <br>
# – D $\in$ {A, B, C, D, E}, also JA!
# <br>
# □ Kann D → A abgeleitet werden?
# <br>
# – {D$\}^+$ = {D, E}
# <br>
# – A $\notin$ {D, E}, also NEIN!

# ### Analyse des Algorithmus zur Hüllenbildung

# ■ Nur Beweisidee
# <br>
# <br>
# ■ Korrektheit: Es werden keine ungültigen FDs erzeugt.
# <br>
# □ Induktion über Anzahl der Operationen
# <br>
# □ Transitivität bzw. Argumentation über die Tupel.
# <br><br>
# ■ Vollständigkeit: Es werden alle gültigen FDs erzeugt.
# <br>
# □ Annahme des Gegenteils, d.h. es gebe eine FD X→Y, die nicht gefunden wird.
# <br>
# □ Konstruktion einer Instanz, die für FDs, aber nicht für X→Y gültig ist.

# ### Transitivitätsregel

# ■ Falls A1,A2,…,An → B1,B2,…,Bm und B1,B2,…,Bm → C1,C2,…,Ck
# <br>
# ■ => A1,A2,…,An → C1,C2,…,Ck

# ![title](tabelle.jpg)

# □ Titel, Jahr -> StudioName
# <br>
# – gilt wegen n:1 von besitzt-Beziehung
# <br>
# □ StudioName -> StudioAdresse
# <br>
# – gilt wegen Schlüsseleigenschaft von Studioname
# <br>
# □ Transitivität: Titel, Jahr ® StudioAdresse

# ### Die „Basis“

# ■ Unterscheidung zwischen gegebenen FDs und abgeleiteten FDs
# <br><br>
# ■ Wahl welche FDs zur Repräsentation aller FDs verwendet werden.
# <br>
# □ Eine Menge an FDs, aus der alle anderen FDs abgeleitet werden können, heißt Basis.
# <br>
# □ Falls keine echte Teilmenge der Basis wiederum selbst eine Basis ist, ist die Basis minimal.
# <br><br>
# ■ Beispiel
# <br>
# □ R(A, B, C); jedes Attribut bestimme funktional die anderen beiden.
# <br>
# □ Welche FDs gelten?
# <br>
# □ A->B, A->C, B->A, B->C, C->A, C->B
# <br>
# □ Abgeleitet: AB->C, AC->B, BC->A
# <br>
# □ Kurzformen: A->BC, B->AC, C->AB
# <br>
# □ Triviale FDs: A->A, B->B, C->C
# <br>
# □ Nicht-triviale FDs: AB->BC, AC->BC, …
# <br>
# □ Minimale Basis: {A->B, B->A, B->C, C->B}
# <br>
# □ Minimale Basis: {AvB, B->C, C->A}

# ### Armstrong Axiome und weitere Ableitungsregeln

# ■ R1 Reflexivität X $\supseteq$ Y => X→Y (insbes. X→X)
# <br>
# □ Triviale FDs
# <br><br>
# ■ R2 Akkumulation {X→Y} => XZ→YZ
# <br>
# □ Auch: Augmentation
# <br><br>
# ■ R3 Transitivität {X→Y, Y →Z} => X→Z
# <br><br>
# ■ R1-R3 bekannt als Armstrong-Axiome
# <br>
# □ Sound and complete
# <br>
# ■ R4 Dekomposition {X→YZ} => X→Y
# <br><br>
# ■ R5 Vereinigung {X→Y, X→Z} => X→YZ
# <br><br>
# ■ R6 Pseudotransitivität {X→Y, WY →Z} => WX→Z

# #### Armstrong Axiome

# ■ Die Menge der Armstrong-Axiome ist
# <br>
# □ Gültig (sound)
# <br>
# – Es wird nichts nicht-ableitbares abgeleitet.
# <br>
# □ Vollständig (complete)
# <br>
# – Durch diese Regeln können alle ableitbaren FDs abgeleitet werden.
# <br>
# □ Minimal
# <br>
# – Keine Regel kann weggelassen werden.

# ### FDs nach Projektionen

#  Motivation: Normalisierung bricht eine Relation in mehrere Teile.
#  <br>
# ■ Gegeben eine Relation R mit Menge F an FDs. Sei S das Ergebnis nach Entfernung einiger Attribute aus R („Projektion“).
# <br><br>
# ■ Welche FDs gelten noch für S?
# <br>
# □ Alle FDs, die aus F folgen,
# <br>
# □ und die nur Attribute aus S verwenden.
# <br><br>
# ■ Beispiel: R(A, B, C, D)
# <br>
# □ FDs: {A->B, B->C, C->D}
# <br>
# □ Projektion von B: S(A, C, D)
# <br><br>
# ■ Algorithmus: Berechne Hülle jeder Teilmenge
# <br>
# □ Wie viele gibt es?
# <br>
# □ Trick 1: Hülle der leeren und Hülle der Menge aller Attribute muss nicht gebildet werden.
# <br>
# □ Trick 2: Falls die Hülle von X bereits alle Attribute enthält, müssen die Supermengen von X nicht mehr geprüft werden.
# <br>
# – Deshalb: Beginnen mit kleinsten Teilmengen

# ■ Beispiel: R(A, B, C, D)
# <br><br>
# ■ Dann gelten FDs X -> E für jedes E $\in$ {X$\}^+$ und E $\in$ S und E $\notin$ X.
# <br><br>
# ■ {A$\}^+$ = {A, B, C, D}
# <br>
# □ A -> C und A -> D
# <br>
# □ A -> B stimmt zwar auch, aber B nicht in S.
# <br>
# □ Enthält bereits alle Attribute aus S, deshalb werden Supermengen nicht berücksichtigt.
# <br>
# <br>
# ■ {C$\}^+$ = {C, D}
# <br>
# □ C -> D
# <br><br>
# ■ {D$\}^+$ = {D}
# <br><br>
# ■ {C,D$\}^+$= {C,D}
# <br><br>
# ■ Ergebnis: A -> C, A -> D und C -> D

# ## Normalformen

# ## Schema Design – Überblick

# 1. Anomalien durch schlechtes Design
# <br>
# 2. Dekomposition (Zerlegung) von Relationen
# <br>
# 3. Boyce-Codd-Normalform (BCNF)
# <br>
# 4. Zerlegung zur Erreichung der BCNF
# <br>
# 5. Andere Normalformen
# <br>
# – Insbesondere 3NF

# ### Redundanzen führen zu Anomalien im Datenbankdesign

# ![title](redundanz1.jpg)

# Update-Anomalien
# <br>
# Veränderungen müssen an allen Stellen durchgeführt werden (neue Adresse für Herr Meyer)
# <br>
# <br>
# Insert-Anomalien
# <br>
# Hinzufügen von Inkonsistenzen (gleicher Kunde mit neuer Adresse)
# <br>
# <br>
# Delete Anomalien
# <br>
# Mehr Informationen gehen verloren als notwendig (Löschung von Auftrag 1 führt dazu, dass Reifenwechsel im Basic Format nicht mehr als Service in der Liste ist)

# #### Ursachen von Anomalien

# N zu M Beziehungen: Kunden und Servicekombinationen
# Transitive N zu 1 Beziehungen: Servicekombination und Preis
# AuftragsID à {Service, Umfang}
# {Service, Umfang} à Preis

# #### Eliminierung von Anomalien durch Dekomposition

# Dekomposition (Zerlegung)
# <br>
# Aufteilung von Attribute in zwei Teilrelationen
# <br>
# Erzeugung neuer Tupel in den neuen Relationen
# <br>
# R(A1,A2,…,An) kann in S(B1,B2,…,Bm) und T(C1,C2,…,Ck) dekomponiert werden, falls
# <br>
# {A1,A2,…,An} = {B1,B2,…,Bm} $\cup$ {C1,C2,…,Ck}
# <br>
# Tupel in S sind die Projektion aller Tupel in R auf {B1,B2,…,Bm}
# <br>
# Insbesondere: Duplikate werden entfernt
# <br>
# Dadurch: Verminderung der Redundanz
# <br>
# Tupel in T analog

# #### Beispiel einer Dekomposition

# ![title](dekomposition1.jpg)

# ### Boyce-Codd-Normalform (BCNF)

# BCNF ist eine Bedingung zur Eliminierung der Anomalien
# <br>
# Eine Relation R ist in BCNF genau dann wenn
# <br>
# Für jede nicht-triviale funktionale Abhängigkeit (FD), muss die linke Seite ein Superschlüssel sein
# <br>
# Erinnerung:
# <br>
# Nichttrivial: Wenigstens ein Attribut rechts kommt links nicht vor
# <br>
# Superschlüssel: Supermenge eines Schlüssels
# <br>
# Was darf nicht sein:
# <br>
# Eine FD ohne Superschlüssel auf der linken Seite
# <br>
# Ziel:
# <br>
# FDs zur Schlüsselabhängigkeiten machen

# #### Beispiel der BCNF-Verletzung

# ![title](redundanz1.jpg)

# Tabelle ist nicht in BCNF
# <br>
# Schlüssel: {AuftragsID}
# <br>
# Superschlüssel müssen AuftragsID enthalten
# <br>
# Eine FD: {KundenID} à {Kunde, Kundenadresse}
# <br>
# {KundenID} ist kein Superschlüssel
# <br>
# -> à BCNF ist verletzt

# #### Algorithmus für Dekomposition nach BCNF

# Grundalgorithmus für Relation R:
# <br>
# 1. Suche verletzende nichttriviale FD: X → B1, B2, … ,Bn
# <br>
# mit X ⊂ R und B1, B2, … , Bn ∈ R
# <br>
# 2. Füge auf der rechten Seite so viele Attribute hinzu wie möglich
# <br>
# 1. Betrachte Hülle der FD
# <br>
# 3. Erzeuge zwei neue Relationen:
# <br>
# R ∖ (B1, B2, … , Bn)
# <br>
# X ∪ (B1,B2,…,Bn)
# <br>
# Grundsätzlich: Jede Relation mit zwei Attributen ist in BCNF

# #### BCNF Dekomposition am Beispiel 1

# Auftrag(AuftragsID, KundenID, Kunde, Kundenaddresse, Service, Umfang, Preis)
# <br>
# BCNF verletzende FD:
# <br>
# KundenID à Kunde, Kundenadresse
# <br>
# Neue Relationen:
# <br>
# Auftrag1(AuftragsID, KundenID, Service, Umfang, Preis)
# <br>
# Auftrag2(KundenID, Kunde, Kundenadresse)

# ![title](dekomposition2.jpg)

# ![title](dekomposition3.jpg)

# R ∖ (B1, B2, … , Bn)

# ![title](dekomposition4.jpg)

# X ∪ (B1,B2,…,Bn)

# Kunde ist in BCNF
# <br>
# KundenID ist Schlüssel
# <br>
# Kundenadresse ist hier zufällig auch Schlüssel. Ignorieren diesen Fall.
# <br>
# Auftrag1 ist nicht in BCNF
# <br>
# Schlüssel: {AuftragsID}
# <br>
# Verletzende FD: {Service, Umfang}->{Preis}
# <br>
# -> erneute Dekomposition

# Auftrag2

# ![title](dekomposition5.jpg)

# R ∖ (B1, B2, … , Bn)

# Service

# ![title](dekomposition6.jpg)

# X ∪ (B1,B2,…,Bn)

# ![title](dekomposition7.jpg)

# ### Wiederherstellbarkeit

# Wiederherstellung der Ursprungsrelation durch Join
# <br>
# Korrektheit durch Widerspruchsbeweis:
# <br>
# Seien t(a,b,c) und s(x,b,z) zwei Tupel in R(A,B,C) mit B -> C
# <br>
# Dekomposition mittels Projektion ergibt:
# <br>
# t1(a,b), s1(x,b) in R1 und t2(b,c), s2(b,z) in R2
# <br>
# Join von R1 und R2 ergibt:
# <br>
# Fehler?
# <br>
# Nein, da wegen B->C gilt c=z

# ![title](wiederherstellbarkeit1.jpg)

# Dekomposition ohne FD (aus Spaß)
# <br>
# ■ Angenommen R(A,B,C) ohne B → C
# <br>
# ■ Projektionen auf R1(A,B) und R2(B,C)
# <br>
# ■ Wiederherstellung durch Join über B

# ![title](wiederherstellbarkeit2.jpg)

# ![title](wiederherstellbarkeit3.jpg)

# ###  Dekomposition zu BCNF – Beispiel 2

# ![title](tabelle.jpg)

# ■ Titel, Jahr → Länge, Typ, StudioName
# <br>
# ■ StudioName → StudioAdresse
# <br>
# ■ Transitivität: Titel, Jahr → StudioAdresse
# <br>
# ■ => {Titel, Jahr} ist Schlüssel
# <br>
# ■ StudioName → StudioAdresse verletzt also BCNF
# <br>
# ■ Zwei neue Relationen
# <br>
# □ Film1(Titel, Jahr, Länge Typ, StudioName)
# <br>
# □ Film2(StudioName, StudioAdresse)

# ![title](tabelle1.jpg)

# ![title](tabelle2.jpg)

# ### Dekomposition zu BCNF – Beispiel 3

# ■ Film(Titel, Jahr, StudioName, Präsident, PräsAdresse)
# <br>
# □ Titel, Jahr → StudioName
# <br>
# □ StudioName → Präsident
# <br>
# □ Präsident → PräsAdresse
# <br>
# □ => {Titel, Jahr} ist Schlüssel
# <br><br>
# ■ Erste Dekomposition anhand von StudioName → Präsident
# <br>
# □ Hinzufügen von möglichst vielen Attributen auf der rechten Seite: StudioName → Präsident,PräsAdresse
# <br>
# □ Film1(Titel, Jahr, StudioName)
# <br>
# □ Film2(StudioName, Präsident, PräsAdresse)
# <br>
# – Hier gilt weiter Präsident → PräsAdresse
# <br>
# – BCNF Verletzung
# <br><br>
# ■ Zweite Dekomposition
# <br>
# □ Film2 wird zu Film2(StudioName, Präsident)
# <br>
# □ Film3(Präsident, PräsAdresse)
# <br><br>
# ■ Verfahren terminiert: Jede neue Relation wird kleiner und 2er-Relationen sind garantiert in BCNF

# ### Weitere Normalformen

# ■ 1. Normalform (1NF)
# <br>
# □ Nur atomare Werte
# <br>
# ■ 2. Normalform (2NF)
# <br>
# □ 1NF und keine Abhängigkeiten von einem Teil eines Schlüssels
# <br>
# ■ 3. Normalform (3NF)
# <br>
# □ 2NF und zusätzlich keine transitiven Abhängigkeiten
# <br>
# ■ Boyce-Codd Normalform (BCNF)
# <br>
# □ 3NF und keine transitiven Abhängigkeiten auch innerhalb des Schlüssels
# 

# #### 1. Normalform

# ![title](normalform1.jpg)

# ■ 1NF: Nur atomare Werte
# <br>
# □ Relation nicht in 1NF:
# <br>
# □ Aka: NFNF oder NF2 oder NF²
# <br>
# □ Umgewandelte Relation in 1NF:
# <br>
# □ Andere Umwandlungsmöglichkeit
# <br>
# – R(Vater, Mutter, Kind1, Kind2)
# <br>
# – Nachteile?

# #### 2. Normalform

# ![title](normalform2.jpg)

# ■ 1NF und keine Abhängigkeiten eines Nicht-Schlüssel-Attributs von einem Teil eines Schlüssels
# <br>
# ■ MatrNr -> Name
# <br>
# □ Aber MatrNr ist nicht vollständiger Schlüssel
# <br>
# ■ Abhilfe: Dekomposition
# <br>
# □ $R1(\underline{MatrNr}, Name)$
# <br>
# □ $R2(\underline{MatrNr,VorlNr}, Semester)$

# #### 3. Normalform

# ![title](normalform3.jpg)

# ■ Kinoaufführungen
# <br>
# □ R(Titel, Kino, Stadt)
# <br>
# □ FDs
# <br>
# – Kino -> Stadt (ein Kino steht in nur einer Stadt)
# <br>
# – Titel, Stadt -> Kino
# <br>
# (D.h.: Ein Film wird nicht zweifach in der gleichen Stadt aufgeführt)
# <br>
# □ Schlüssel?
# <br>
# – Einzelne Attribute sind nicht Schlüssel
# <br>
# – {Titel, Stadt} ist Schlüssel, da er funktional alle anderen Attribute bestimmt.
# <br>
# – {Kino, Titel} ist auch Schlüssel, da Kino -> Stadt augmentiert werden kann zu Kino, Titel -> Stadt
# <br>
# □ BCNF-Verletzung:
# <br>
# – Kino -> Stadt (da Kino nicht Superschlüssel ist

# Lösung des Problems durch Relaxierung der BCNF
# <br>
# Eine Relation R ist in 3. Normalform genau dann wenn:
# <br>
# Für jede nicht-triviale FD A1A2…An -> B für R ist
# <br>
# {A1, A2, …, An} ein Superschlüssel für R, oder B ist Teil eines Schlüssels für R.
# <br>
# Kurz: Für jede FD ist entweder die linke Seite ein Superschlüssel oder die rechte Seite Teil eines Schlüssels.
# <br>
# Am Beispiel
# <br>
# R(Titel, Kino, Stadt) mit FDs
# <br>
# Kino -> Stadt
# <br>
# Titel, Stadt -> Kino
# <br>
# ->Verletzt nicht 3. Normalform, da Stadt Teil eines Schlüssels ist.

# #### 3NF vs. BCNF

# ■ Wichtige Eigenschaften der Dekomposition
# <br>
# 1. Wiederherstellbarkeit
# <br>
# – Projektion der ursprünglichen Relation auf die neuen Relationen und dann Rekonstruktion der ursprünglichen Relation (mittels Join).
# <br>
# 2. Bewahrung der FDs
# <br>
# – Prüfbarkeit aller FDs in den neuen Relationen
# <br><br>
# ■ BCNF garantiert 1.
# <br><br>
# ■ 3NF garantiert 1. und 2.
# <br>
# □ Aber: Es können Anomalien bestehen bleiben.
# <br><br>
# ■ Dekomposition zur 3NF
# <br>
# □ Anderer Algorithmus
# <br>
# □ Nicht hier!

# #### Zusammenfassung – Normalformen

# ![title](normalform_zusammenfassung.jpg)

# 5NF ⇒ SKNF ⇒ RFNF ⇒ ETNF ⇒ 4NF
# <br>
# Projection-join normal form (5NF)
# <br>
# Superkey normal form (SKNF)
# <br>
# Redundancy-free normal form (RFNF)
# <br>
# Essential tuple normal form (ETNF)
# <br>
# A Normal Form for Preventing Redundant Tuples in Relational Databases Hugh Darwen, C.J. Date, Ronald Fagin, ICDT 2012
# <br>
