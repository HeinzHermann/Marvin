Hardware Blatt2
Marvin Glaser
4424114
Gruppe G26 (Freitag 13:00 bis 15:00 Uhr)
Paul Zuegel


1.
a)

Es werden 5 bits benoetigt, da durch den Uebertrag (Overflow) von 1 bit im letzten Rechenschritt ein 5 bit
erzeugt werden kann.
Bsp.:
    1000
  + 1000
________
   10000


b)

Bei der Berechnung werden im schlechtesten Fall zwei 8 bit Zahlen miteinander addiert. Somit werden 2 mal 2 Bit-
Paeckchen (je 4 Bits) mitteinander Addiert. Weiterhin kann bei jeder dieser Rechnungen ein Uebertrag (Overflow)
zum naechsten Bit entstehen, dass ebenfalls Addiert werden muss (also eine weitere Addition fuer jede Berechnugn)
--> 2 Additionen + 2 Additionen Overflow = hoechstens 4 Berechnungen.


c)
Im besten Fall bestehen die Zahlen a und b aus Bitfolgen, deren letzte vier Bits nur aus nullen bestehen und somit
weggelassen werden koennen. In einem solchen Fall muessen nur die ersten vier Bits der jeweiligen Zahlen in das
Rechenwerk geladen und addiert werden. Entsteht hierbei kein Overflow koennen die Zahlen in nur einem Schritt addiert
werden.

d)
Zweierkomplemente koennen genau wie normale Binaerzahlen normal miteinander addiert werden. Hierbei muss allerdings
darauf geachtet werden, dass der Overflow ab dem achten Bit nicht mehr zu der Zweierkomplementzahl gehoert. Entsteht
durch Overflow bei der Addition also ein neuntes Bit, muss dieses Hardware- oder Softwaretechnisch geloescht/ignoeriert
werden.




2.

k=0		k=1		k=2		k=3

push A		load C		mul C, B	mul C, B, B
push C		mul B		sub C, A	sub C, A, A
sub		stor B		mul C, A	mul C, A, A
push C		load A		mul D, D	mul D, D, D
push D		mul D		mul D, A	mul D, A, A
mul		mul D		dif B, A	dif B, A, Z
mul		dif B		move A, Z	
push C		stor Z		
push B		
mul		
div		
pop


Definitionen fuer k=0:

		b
wenn Stack	a	+ Befehl div	--> Stack a/b


		d
wenn Stack	c	+ Befehl sub 	--> Stack c-d




3.

n^2 + 5n + 6

move #0, d4		-- setze d4 auf 0 fuer counter
quad:
    add d0, d2
    add #1, d4
cmp d4, d0		-- wenn counter < d0, wiederhole quad
bne quad		-- wenn counter = d0, dann n^2 in d2
move #5, d4		-- setze d4 zu 5 fuer counter vergleich
move #0, d5		-- setze d5 zurueck auf 0
multip:
     add d4, d3
     add #1, d5
cmp d5, d4		-- wenn counter < 5, wiederhole multip
bne multip		-- wenn counter = 5, dann n*5 in d3
move d2, d1
add d3, d1
add #6, dn		-- fuege d2, d3 und 6 zusammen in d1
