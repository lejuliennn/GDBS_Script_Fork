#!/usr/bin/env python
# coding: utf-8

# # Normalisierung

# Bisher haben wir eine direkte Übersetzung von ER-Diagrammen in das relationale Modell behandelt. Dabei sind wir davon ausgegangen, dass das Ursprungsmodell sinnvoll erstellt und alle dazugehörigen Kardinalitäten sinnvoll auch im Sinne der Vermeidung von Redundanz modelliert wurden. In der Realität kann man aber nicht immer davon ausgehen, dass die Modellierung fehlerfrei durchgeführt wird. Zudem kann es nachdem konzeptionellen Entwurf zu Veränderungen hinsichtlich der Nutzung der Daten und den beziehungen zwischen den ursprünglichen Entitytypen und Relationshiptypen kommen, die zu Problem führen können. Insbesondere könnten vorher unbekannte funktionale Abhängigkeiten sichtbar werden, die eine Verfeinerung des (logischen) Entwurfes erfordern. 

# **Beispiel:** In der folgenden Filmtabelle werden Informationen zu Filmen abgespeichert. Bei der Modellierung wurde darauf geachtet, dass die Tabelle einen Schlüssel und mehrere Attribute hat. 
# 

# |FilmID|Titel|Jahr|Länge|Genre|Studio|Produktionsland|
# |-----|-----|-----|------|-----|-------|--------|
# |1|Matrix I|1999|136|SciFi|Warner Bros.|USA|
# |2|Lord of the Rings I|2001|178|Fantasy|Warner Bros.|USA|
# |3|The Breakfast Club|1985|97|Drama|Universal|USA|
# |4|Cruel Intentions|1999|97|Drama|Columbia Pictures|USA|

# Bei diesem Beispiel fällt auf, dass bestimmte Informationen mehrfach auftauchen. Insbesondere ist das bei Studio und USA der Fall. Es stellt sich heraus, dass das Produktionsland vom Studionamen abhängt. Dies ist nicht nur zufällig in dieser dargestellten Tabelle so, sondern konzeptionell auch begründet werden. Die Produktion wird dem Land zugerechnet, in dem sich das Studio befindet. 
# An und für sich ist das kein großes Problem. Oft werden solche Abhängigkeiten hingenommen. Wenn wir jedoch eine Minimierung von Redundanz bei unserer Modellierung vornehmen wollen, müssen wir diese Abhängigkeit nutzen um Informationen die herleitbar sind nicht wiederholt zu speichern. Eine redundante Speicherung solcher Informationen kann dazu führen, dass bei zukünftigen Änderungen der Daten, die Abhängigkeit nicht in Betracht gezogen wird und Inkonsistenzen entstehen, die unsere nun erkannte Beziehung verletzen könnten.
# Die folgende Darstellung weist dieses Problem nicht mehr auf.

# **Filmtabelle**
# 
# |FilmID|Titel|Jahr|Länge|Genre|Studio|
# |-----|-----|-----|------|-----|-------|
# |1|Matrix I|1999|136|SciFi|Warner Bros.|
# |2|Lord of the Rings I|2001|178|Fantasy|Warner Bros.|
# |3|The Breakfast Club|1985|97|Drama|Universal|
# |4|Cruel Intentions|1999|97|Drama|Columbia Pictures|
# 

# **Studiotabelle**
# 
# |Studio|Produktionsland|
# |-----|-----|
# Warner Bros.|USA|
# Universal|USA|
# Columbia Pictures|USA|

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

# ### Typen von FDs

# Unter den verschiedenen funktionalen Abhängigkeiten gibt es verschiedene Kategorien, die unterschiedlich interessant sind. Es gibt triviale FDs, minimale FDs und andere Spezialfälle wie Schlüssel.
# 
# 
# 
# **Trivial**: Bei trivialen FDs sind die Attribute rechts eine Teilmenge der Attribute links. Diese FDs gelten als trivial, da natürlich jedes Attribut sich selbst funktional bestimmt. Genauso bestimmt jede Attributkombination jede ihrer Teilmengen funktional. Anders ausgedrückt gilt: „Zwei Tupel, die in einer Menge von Attributen übereinstimmen, stimmen auch in einem dieser Attribute überein.“
# 
# Beispiel: Titel, Jahr → Titel
# <br>
# 
# <br><br>
# **Nicht-trivial**: Wenigstens ein Attribut rechts kommt links nicht vor.
# <br>
# □ Beispiel: Titel, Jahr → Jahr, Länge
# <br><br>
# **Völlig nicht-trivial**: Die Attribute links und rechts sind disjunkt.
# <br>
# Beispiel: Titel, Jahr → Länge
# <br>
# 
# Für die meisten Probleme, die wir betrachten interessieren wir uns immer nur für die völlig nicht-trivialen FDs. Insbesodnere können wir durch die Dekompositionsregel leicht triviale Komponenten einer FD entfernen. 

# ### Schlüssel als Spezialfall einer FD

# Eine Menge aus einem oder mehr Attributen $\{A_1, A_2, …, A_n\}$ ist Schlüssel der Relation R, falls gilt:
# Die Attribute bestimmen alle anderen Attribute funktional.
# 
# - Anmerkung: Relationen sind Mengen, es kann also keine zwei völlig identischen Tupel geben.
# 
# Besonders interessant sind in diesem Zusammenhang sogenannte **minimale** Schlüssel, bei denen gilt, dass Keine echte Teilmenge von $\{A_1, A_2, …, A_n\}$ alle anderen Attribute funktional bestimmt.
# 

# **Beispiel:** Betrachten wir wieder unser ursprüngliches Beispiel.
# 
# 
# |FilmID|Titel|Jahr|Länge|Genre|Studio|Produktionsland|
# |-----|-----|-----|------|-----|-------|--------|
# |1|Matrix I|1999|136|SciFi|Warner Bros.|USA|
# |2|Lord of the Rings I|2001|178|Fantasy|Warner Bros.|USA|
# |3|The Breakfast Club|1985|97|Drama|Universal|USA|
# |4|Cruel Intentions|1999|97|Drama|Columbia Pictures|USA|

# {FilmID} ist der Schlüssel für diese Relation und natürlich bestimmt FilmID jedes andere Attribut funktional.
# 
# Ob weitere Attributkombinationen Schlüssel sein können, hängt von der Domäne ab. In dieser kleinen Tabelle könnte man meinen, dass auch der Titel ein Schlüssel sein könnte, da jeder Titel nur einmal auftraucht und somit automatisch jedes weitere Attribut eindeutig bestimmt. Wenn wir Titel als Schlüssel betrachten, erlauben wir keine unterschiedlichen Filme mehr mit identischen Titeln. Damit könnten wir keine Filmremakes mehr in unsere Datenbank aufführen.
# Theoretisch wäre es möglich Titel und Jahr gemeinsam als Schlüssel zu betrachten, da es unwahrscheinlich ist, dass ein Film mit dem exakt selben Titel im gleichen Jahr auftaucht. 
# 

# ### Superschlüssel

# Eine Relation kann mehr als einen Schlüssel besitzen. Es gilt jedoch immer genau einen Primärschlüssel zu spezifizieren.
# Hierbei gilt es zu erkennen, dass jede Attributmenge, die alle Attribute eines Schlüssels enthält auch die Schlüsseleigenschaft aufweist. Eine Attributmenge, die einen Schlüssel enthält, nennt man einen Superschlüssel. Es können auch unnötige Attribute in einem Superschlüssel existieren. Ein (Primär)schlüssel ist jedoch grundsätzlich minimal. Das heißt, dass keine Teilmenge des Schlüssels auch die Schlüsseleigenschaft besitzt.
# 
# <img src="wikipediaPrimaryKey.svg.png" alt="wikipediaPrimaryKey" width="500" caption="by PHummel "/> 
# 
# In der Abbildung oben, sieht man auch, dass es sogenannte Schlüsselkandidaten gibt. Da wir grundsätzlich genau ein Primärschlüssel spezifizieren, sind alle anderen Attributkombinationen die minimal sind und Schlüsseleigesnchaften erfüllen Schlüsselkandidaten. Wir werden oft den Begriff Schlüssel für Schlüsselkandidaten nutzen. 
# 
# Beispiele:
# {FilmID} ist ein Schlüssel, ein Schlüsselkandidant und ein Superschlüssel.
# 
# {Titel, Jahr} ist ein Schlüsselkandidat und ein Superschlüssel. Da FilmID bereits Primärschlüssel ist, kann {Titel, Jahr} nur noch Schlüsselkandidat sein.
# 
# {Titel, Jahr, Länge} ist ein Superschlüssel und ist nicht minimal.
# 
# **Minimal vs. kleinster**
# 
# Minimaler Schlüssel: Kein Attribut darf fehlen
# - Ist nicht unbedingt kleinster Schlüssel
# - Beispiel: {Titel, Jahr}
# 
# Kleinster Schlüssel: Schlüssel mit wenigsten Attributen
# 
# - Ist auch minimal
# - Beispiel: {FilmID}
# 
# 
# 

# ### Wo kommen FDs her? Schema vs. Instanz

# Wir hatten bereits festgestellt, dass wir auch weitere zufällige FDs in unserer Filmrelation finden können. Zum Beispiel gilt in der dargestellten Instant {Länge, Jahr} $\rightarrow$ {Titel}. Nach unserer ursprünglichen Definition handelt es sich hierbei um eine funktionale Abhängigkeit. Noch schlimmer: {Länge, Jahr} könnte sogar als Schlüssel definiert werden. Es ist leicht einzusehen, dass dieser Schlüssel nicht sinnvoll ist.
# 
# Ob letztlich eine FD gelten soll, muss während der Modellierung entschieden werden. Das heißt, dass die FD unabhängig von den vorhanden Daten immer gelten muss. Das gleiche gilt auch für Schlüssel. Während Schlüssel hauptsächlich dafür definiert werden um Einträge von einander unterscheiden zu können, können FDs als Einschränkungen auf einer Relation definiert werden um so Integrität von Daten herzustellen. Die Einhaltung und Überprüfung von funktionalen Abhängigkeiten hilft die Qualität und Konsistenz von Daten aufrecht zu erhalten. Beispielsweise kann man mit der Definition einer funktionalen Abhängigkeit {Postleitzahl}$\rightarrow${Stadt} sicherstellen, dass dieselbe Postleitzahl nicht fälschlicherweise mit zwei unterschiedlichen Städten assoziiert wird. 

# ### Schlüssel aus ER-Diagrammen

# Schlüsselinformationen sind grundsätzlich bereits im ER-Modell bekannt und müssen anhand der folgenden **Regeln** übernommen werden.
# 
# 1. Falls die Relation von einem Entitytypen stammt, bestehen die Schlüsselattribute der Relation aus den Schlüsselattributen des Entitytypen.
# 
# 2. Falls die Relation von einem Relationshiptypen stammt muss man die Kardinalitäten betrachten.
# 
#     1. $m:n$: Schlüssel besteht aus den Schlüsselattributen der verbundenen Entitytypen.
#     2. $1:n$: Schlüssel besteht aus den Schlüsselattributen des Entitytypen der n-Seite.
#     3. $1:1$: Zwei mögliche Schlüssel. Hierbei ist zu beachten, dass die Umwandlung kapazitätserhöhend werden könnte.
#         - Schlüssel der beiden beteiligten Entitytypen. Wahl eines der beiden Schlüssel als Primärschlüssel (egal welcher).
# 
# 3. Bei n-ären Relationshiptypen kann es komplizierter werden. Die 1-Seite muss nie am Schlüssel beteiligt sein.
# 4. Falls die Relation aus einem schwachen Entitytypen stammt, müssen die Schlüssel der bestimmtenden Entitytypen mit übernommen werden.

# **Beispiel 1:**
# 
# 
# ![title](er_diagramm1.jpg)

# - $Filme(\underline{Titel, Jahr}, Länge, Typ)$ (Regel 1)
# 
# - $Schauspieler*in(\underline{Name, Adresse})$ (Regel 1)
# - $Studio(\underline{Name}, Adresse)$ (Regel 1)
# - $besitzt(\underline{Titel, Jahr}, Name)$ (Regel 2B)
#     - zusammengefasst mit Filme zu Film $(\underline{Titel, Jahr}, Länge, Typ, StudioName)$
# - $spielt\_in(\underline{Titel, Jahr, Name, Adresse}, Gehalt)$ (Regel 2A)

# **Beispiel 2 (1:1-Beziehungen):**
# 
# ![title](er_diagramm2.jpg)

# - $Studios(\underline{SName})$ (Regel 1)
#  <br>
# - $Vorsitzende(\underline{VName})$ (Regel 2)
# - $leitet(\underline{SName}, VName)$ oder leitet$(SName, \underline{VName})$ (Regel 2C)
#     - Es gibt zwei Schlüssel: SName und VName und ein Schlüssel muss als Primärschlüssel gewählt werden.
#     - Es gibt entsprechend zwei Möglichkeiten die Relation zusammenzufassen zu $Studios(\underline{SName}, VName)$ oder $Vorsitzende(\underline{VName}, SName)$. Je nach Umwandlung ist die Darstellung kapazitätserhöhend. In Datenbanksystemen kann man durch weitere Integritätsbedingungen wie z.B. unique verhindern, dass die Nicht-schlüsselspalte doppelte Einträge erhält.

# **Beispiel 3 (n-äre Relationshiptypen):**
# 
# ![title](n-aer_relationshiptypen1.jpg)

# - $Studio (\underline{Name}, Adresse)$
# - $ Schauspieler*in (\underline{Name}, Adresse)$
# - $Film (\underline{Titel, Jahr}, Typ, Länge)$
# - $ist\_unter\_Vertrag (\underline{SchauspielerName, Titel, Jahr}, StudioName, Gehalt)$. Studioname ist nicht teil des Schlüssels (Regel 3)

# **Beispiel 4 (Schwache Entitytypen):**
# 
# <img src="schwacheETs.png" alt="schwacheETs" width="500"/> 
# 
# 
# - $Studio(\underline{Name}, Adresse)$ (Regel 1)
# - $Schauspieler(\underline{Name}, Adresse)$ (Regel 1)
# - $Film(\underline{Titel, Jahr}, Typ, Länge)$ (Regel 1)
# - $Vertrag(\underline{SchauspielerName, StudioName, Titel, Jahr}, Gehalt)$ (Regel 4)

# ### Schlüssel aus ER-Diagrammen: IST-Hierarchien

# **Beispiel 5 (IST-Hierarchien):**
# 
# <img src="IST_hierarchie.png" alt="ist_Hierarchie" width="400"/> 
# 
# 
# Bei IST-Hierarchien müssen die Schlüsselattribute in allen Relationen mit übernommen werden. 
# 
# - ER-Stil: Im ER-Still muss sichergestellt werden, dass der selbe Schlüssel in der Basisrelation das selbe Objekt in der Unterklasse repräsentiert. 
#     - $Film(\underline{Titel, Jahr}, Länge,Typ)$
#     - $Krimi(\underline{Titel, Jahr}, Waffen)$
#     - $Zeichentrickfilm(\underline{Titel, Jahr})$
# 
# - OO-Stil: Im OO-Stil muss man zusätzlich sicherstellen, dass der selbe Schlüssel nicht in mehreren Relationen gleichzeitig auftaucht. 
#     - $Film(\underline{Titel, Jahr}, Länge, Typ)$
#     - $FilmZ(\underline{Titel, Jahr}, Länge, Typ)$
#     - $FilmK(\underline{Titel, Jahr}, Länge, Typ, Waffen)$
#     - $FilmZK(\underline{Titel, Jahr}, Länge, Typ, Waffen)$
# - Mit NULL-Werten: Die Schlüssel sind hier wie bei jeder normalen Relation. Die obengenannten Probleme beim OO-Stil und ER-Stil können nicht auftreten.
#     - $Film(\underline{Titel, Jahr}, Länge, Typ, Waffen)$

# ## Ableitungsregeln für FDs

# Während man im ER-Modell bereits Schlüssel definieren kann, kann es manchmal sein, dass man bestimmte ableitbare Abhängigkeiten übersieht. Durch die funktionale Beziehung kann man aber alle geltenden funktionalen Abhängigkeiten in einer Relation ableiten.
# Das Ziel des Datenbankentwurfes ist es alle abgeleiteten FDs an Hand von Dekomposition in Schlüsselabhängigkeiten umzuformen ohne dabei semantische Informationen zu verlieren. Diese Umwandlung dient wie im Eingangsbeispiel des Kapitels gezeigt dazu Redundanz in den Daten zu vermeiden.

# **Beispiel:** Gegeben sei die Relation R(A,B,C) mit folgender Instanz und es gelte $A\rightarrow B$ und $B\rightarrow C$
# 
# |A|B|C|
# |-|-|-|
# |$a_1$|$b_1$|$c_1$|
# |$a_2$|$b_1$|$c_1$|
# |$a_3$|$b_2$|$c_1$|
# |$a_4$|$b_1$|$c_1$|
# 
# Aus den FDs $A\rightarrow B$ und $B\rightarrow C$ lässt sich durch die transitivität der funktionalen Abhängigkeit auch $A\rightarrow C$ herleiten. 

# - Beweis:
#     - Z.z.: Zwei beliebige Tupel, die in A übereinstimmen, müssen auch in C übereinstimmen.
#     - Beweis durch Widerspruch: Es gibt zwei beliebige Tupel, die in A übereinstimmen aber nicht in C:
#         - $t_1 = (a, b_1, c_1)$ und $t_2 = (a, b_2, c_2)$ mit $c_1\neq c_2$
#         - Da $A\rightarrow B$ gilt $b_1=b_2$ und  $t_1=(a, b_1, c1)$ und $t_2= (a, b_1, c_2)$
#         - Da $B\rightarrow C$  und $b_1=b_2$ gilt  $c_1=c_2$ $\Rightarrow$ Widerspruch
# - QED
# 
# - Nicht ableitbar: C→A, B→A oder C→B

# ### FD-Mengen

# Die Tatsache, dass wir mit einer Teilmenge der geltenden FDs auf einer Relation andere geltende herleiten können ruft die Frage hervor, wann zwei solche Mengen zu den exakt gleichen FDs insgesamt führen können. Hierbei sprechen wir von Äquivalenz von FD-Mengen: 
# - Zwei Mengen S und T an FDs heißen äquivalent, falls die Menge der gültigen Instanzen unter S die gleiche wie
# unter T ist. Das heißt, dass für beide Mengen nach einer umfangreichen herleitung aller ableitbarer FDs die selbe Menge entstehen könnte. 
# 
# Wenn wir die Richtungen der Äquivalenz einzeln betrachten können wir auch aussagen: 
# - Eine Menge S an FDs folgt aus einer Menge T an FDs, falls jede unter T gültige Instanz auch unter S gültig ist.
# 
# Die Äquivalenz von FD-Mengen bieten uns die Grundlage dafür ohne Informationsverlust neue FDs abzuleiten. 
# 
# 

# ### Hüllenbildung
# 
# Da wir möglichst alle geltenden FDs in Schlüsselabhängigkeiten umwandeln wollen müssen wir auch alle geltenden minimalen FDs ableiten. Das Verfahren hierfür heißt **Hüllenbildung**:
# Hierunter versteht man genau die Ableitung aller FDs aus einer gegebenen Menge an FDs, gemäß Ableitungsregeln
# <br
# □ Auch: attribute closure, closure, Attributabschluss

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
