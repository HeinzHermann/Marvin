Hardware Blatt 3
Marvin Glaser
44242114
Gruppe 26
Paul Zuegel



-- ==================================================================================
-- ==== Aufgabe 1a)

Als Busse werden Verbindungen zwischen einzelnen Komponeneten eines Computers oder
zwischen verschiedenen Computern bezeichenet. In Rechnern besteht ein Bus im normal-
fall aus einer bestimmten Anzahl an prallel laufenden Leitungen, die gleichzeitig
jeweils 1 Bit uebertragen. Diese Informationen muessen synchronisiert beim Empfaenger
der Daten ankommen. Zu jedem gegebenen Zeitpunkt kann immer nur eine Einheit des
Rechners Informationen in den Bus einspeisen. Beispiele fuer unterschiedliche Bus-
systeme sind z.B. Datenbusse (uebertragen Daten zwischen unterschiedlichen Einheiten
innerhalb des Rechners) und Adressbusse (uebertragen Speicheradressen). Busse koennen
bi- (Datenfluss in beide Richtungen moeglich, Bsp. Datenbus) oder unidirektional
(Datenfluss nur in eine Richtung, Bsp. Adressbus) sein.

-- ==================================================================================
-- ==== Aufgabe 1b)

schnell -->

Add #1000, D1 (Unmittelbare Adressierung)
wenigste Adressierungen. Steuere Adresse D1 an und addiere 1000 zum Inhalt des Registers

Add D0, D1 (Register-direkte Adressierung) und Add $1000, D1 (Absolute Adressierung)
ungefaehr gleich viele Adressierungen. Steuere Speicheradresse $1000, bzw. Register D0
an und addiere den Inhalt auf Register D1 

Add (D0), D1 (Register-indirekte Adressierung)
groesste Anzahl an Schritten. Steuere Register D0, dann steuere die in D0 gespeierte 
Speicheradresse an und addiere den Inhalt dieser Speicheradresse auf Register D1

<-- langsam

-- ==================================================================================
-- ==== Aufgabe 1c)

Die ISA (Instruktions-Satz-Architektur) stellt die Schnittstelle zwischen Hardware und
Software dar und besteht im wesentlichen aus Modellen, die dem Programmierer oder dem
Kompilierer eine Abstraktion von der Hardware ermoeglichen. In der ISA werden theore-
tische Konzepte wie Register, Adressen, Datentypen und Maschinenbefehlssaetze. Die ISA
beschreibt allerdings weder den tatsaechlichen Aufbau eines Rechners, noch die letztend-
liche Verteilung von Befehlen und Instruktionen auf die einzelnen Hardwarekomponenten
des Rechners.

-- ==================================================================================
-- ==== Aufgabe 1d)

Arithmetische Operationen werden in modernen Rechnern werden in der sogenannten ALU
(arithmetic logical unit) ausgefuehrt. Im regelfall wird das Ergebnis einer solchen
Berechnung in das Register abgespeichert.
Anmerkung: Die ALU wird dazu verwendet arithmetische Operationen auf integrale Zahlen
anzuwenden. Um solche Operationen auf Gleitkommazahlen anzuwenden wird eine sog.
floating-point unit (FPU) verwendet.



-- ==================================================================================
-- ==== Aufgabe 2a)

Mit nur einer Funktionseinheit steht das Ergebnis der angegebenen Rechnung fruehestens
nach 56 Takten zur Verfuegung.

-- ==================================================================================
-- ==== Aufgabe 2b)

Besitzt der Prozessor eine weitere Funktionseinheit, dann kann das Ergebnis der Be-
rechnung schon nach 37 Takten vorliegen, da die Berechnung der Klammern parallel aus-
gefuehrt werden kann.
Anmerkung: Es wird angenommen, dass die beiden Rechenwerke gleichzeitig auf das Register
zugreifen koennen in dem der Wert fuer a steht (da die Addition und die Subtraktion
a in beiden Klammern gleichzeitig starten wuerde). Ist dies nicht der Fall, so wuerde
sich die Rechenzeit auf 38 erhoehen, da eine der beiden Recheneinheiten darauf warten
muesste, dass die andere Einheit den Wert fuer a aus dem Register geladen hat.

-- ==================================================================================
-- ==== Aufgabe 2c)

Die Hinzunahme einer dritten Funktionseinheit wuerde die Rechenzeit nicht oder nur mini-
mal weiter verbessern, da in den Klammern der gegebenen Gleichung keine zwei Rechnungen
parallel ausgefuehrt werden koennen (die dritte Einheit muss immer auf das Ergebnis einer
der anderen Einheiten warten). Im besten Fall koennte hier 1 Takt gespart werden, indem
die dritte Einheit fruehzeitig den Wert a laedt, waehrend sie auf das Ergebnis einer an-
deren Einheit wartet.



-- ==================================================================================
-- ==== Aufgabe 3a)

Bei der Zahl k muss es sich um eine Natuerliche Zahl (0 mit eingeschlossen) handeln.
Ist k bei initialisierung des Programms kleiner als 0, laeuft das Programm in einer
Endlosschleife.
Die Ausgabe D0 am Ende des Programms setzt sich aus der Summe des Vorherigen und des
Vorvorherigen D3 zusammen, wobei die Ausgabe bei k=0 und k=1 immer 1 ist.

-- ==================================================================================
-- ==== Aufgabe 3b)

Waehrend der Laufzeit des Programms wird der vorherige und der vorvorherige Wert von
D3 addiert und als neuer D1 und D3 Wert abgespeichert, wobei fuer k=0 und k=1 gild,
dass D1 und D3 immer 1 sind.
Das Programm berechnet somit das Ergebnis der Fibonacci-Folge.


-- ==================================================================================
-- ==== Aufgabe 3c)

		D0	D1	D2	D3	D4

Schritt 1	3	-	-	-	3
Schritt 2	3	1	-	-	3
Schritt 3	3	1	0	-	3
Schritt 4	3	1	0	1	3
Schritt 5	3	0	0	1	3
Schritt 6	3	1	0	1	3
Schritt 7	3	1	1	1	3
Schritt 8	3	1	1	1	3
Schritt 9	2	1	1	1	3
Schritt 10	2	2	1	1	3
Schritt 11	2	2	1	1	3
Schritt 12	2	2	1	2	3
Schritt 13	2	2	1	2	3
