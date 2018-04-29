PRG2 Uebung 2
Marvin Glaser
44242114
Gruppe 3 Montag (12:00 bis 14:00 Uhr)
Martin Parnet

------------------------------------------------------------------------------------------
-- Aufgabe 1.

-- a)
f1 referenziert (direkt): f1, f2, f4
f2 referenziert (direkt): f1, f4
f3 referenziert (direkt): f4, f5
f4 referenziert (direkt): f4
f5 referenziert (direkt): f3

-- b)
f1 referenziert: f1, f2, f4
f2 referenziert: f1, f2, f4
f3 referenziert: f3, f4, f5
f4 referenziert: f4
f5 referenziert: f3, f4, f5

-- c)
direkt rekursiv:
f1, f4

-- d)
rekursiv:
f1, f2, f3, f4, f5

-- e)
Verschraenkt Rekursiv:
(f1, f2), (f2, f1), (f3, f5), (f5, f3)
 

------------------------------------------------------------------------------------------
-- Aufgabe 2.

-- a)

					g1	g2	g3	g4

...ist iterativ				ja	nein	nein	nein

...ist endrekursiv			ja	nein	nein	nein

...ist linear rekursiv			ja	ja	nein	nein

...ist Baum-rekursiv			ja	ja	nein	ja

...ist geschachtelt Baum-rekursiv	ja	ja	ja	ja



-- b)
-- um h' endrekursiv auszufuehren wird eine hilfsfunktion h_help aufgerufen
-- diese besitzt einen stack, der mit jedem rekursiven aufruf erhoeht und
-- bei erfuellen der bedingung x < 10 ausgegeben wird
h' x = h_help x 0 where
        h_help x stack = if x < 10 then stack
        else h_help (x-1) (2*x + stack)


------------------------------------------------------------------------------------------
-- Aufgabe 2.

f a b c = if c >= 21
		then (if c < 27 then a*c else f a (f a a (c+100)) (c+9))
		else f a (f a a (c+100)) (c+9)


-- a)

D	f 1 2 3 = if 3 >= 21
		then (if 3 < 27 then 1*3 else f 1 (f 1 1 (3+100)) (3+9))
		else f 1 (f 1 1 (3+100)) (3+9)

I	f 1 2 3 = if False
		then (if 3 < 27 then 1*3 else f 1 (f 1 1 (3+100)) (3+9))
		else f 1 (f 1 1 (3+100)) (3+9)

D	f 1 (f 1 1 (3+100)) (3+9)

D	f 1 (f 1 1 (3+100)) (3+9) = if (3+9) >= 21
		then (if (3+9) < 27 then 1*(3+9) else f 1 (f 1 1 ((3+9)+100)) ((3+9)+9))
		else f 1 (f 1 1 ((3+9)+100)) ((3+9)+9)

A	f 1 (f 1 1 (3+100)) (3+9) = if 12 >= 21
		then (if (3+9) < 27 then 1*(3+9) else f 1 (f 1 1 ((3+9)+100)) ((3+9)+9))
		else f 1 (f 1 1 ((3+9)+100)) ((3+9)+9)

I	f 1 (f 1 1 (3+100)) (3+9) = if False
		then (if (3+9) < 27 then 1*(3+9) else f 1 (f 1 1 ((3+9)+100)) ((3+9)+9))
		else f 1 (f 1 1 ((3+9)+100)) ((3+9)+9)

D	f 1 (f 1 1 ((3+9)+100)) ((3+9)+9)

D	f 1 (f 1 1 ((3+9)+100)) ((3+9)+9) = if ((3+9)+9) >= 21
		then (if ((3+9)+9) < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9))
		else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

A	f 1 (f 1 1 ((3+9)+100)) ((3+9)+9) = if (12+9) >= 21
		then (if ((3+9)+9) < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9))
		else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

A	f 1 (f 1 1 ((3+9)+100)) ((3+9)+9) = if 21 >= 21
		then (if ((3+9)+9) < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9))
		else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

I	f 1 (f 1 1 ((3+9)+100)) ((3+9)+9) = if True
		then (if ((3+9)+9) < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9))
		else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

D	if ((3+9)+9) < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

A	if (12+9) < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

A	if 21 < 27 then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

I	if True then 1*((3+9)+9) else f 1 (f 1 1 (((3+9)+9)+100)) (((3+9)+9)+9)

D	 1*(12+9)

D	 1*21

D	 21


-- b)
-- schreibarbeit nicht gemacht
Die Funktion in dem gegebenen Beispiel steckt in einer Unendlichschleife fest, wenn das Programm
applikativ ausgewertet wird. Grund hierfuer ist, dass von 'innen nach aussen' ausgewertet wird.
Daher wird bei jedem rekursiven aufruf des Programms zuerst eine neue Rekursion mit c = c + 100
ausgefuehrt. Dies fuehrt dazu, dass das c immer groesser wird und nie unter den schwellenwert von
27 in der zweiten if schleife sinken kann. 

-- c)

D	f (1+1) 2 17 = if 17 >= 21
		then (if 17 < 27 then (1+1)*17 else f (1+1) (f (1+1) (1+1) (17+100)) (17+9))
		else f (1+1) (f (1+1) (1+1) (17+100)) (17+9)

I	f (1+1) 2 17 = if False
		then (if 17 < 27 then (1+1)*17 else f (1+1) (f (1+1) (1+1) (17+100)) (17+9))
		else f (1+1) (f (1+1) (1+1) (17+100)) (17+9)

D	f (1+1) (f (1+1) (1+1) (17+100)) (17+9)

D	f (1+1) (f (1+1) (1+1) (17+100)) (17+9) = if (17+9)  >= 21
		then (if (17+9) < 27 then (1+1)*(17+9) else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9))
		else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9)

A	f (1+1) (f (1+1) (1+1) (17+100)) (17+9) = if 26 >= 21
		then (if (17+9) < 27 then (1+1)*(17+9) else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9))
		else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9)

I	f (1+1) (f (1+1) (1+1) (17+100)) (17+9) = if True 
		then (if (17+9) < 27 then (1+1)*(17+9) else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9))
		else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9)

D	if (17+9) < 27 then (1+1)*(17+9) else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9)

A	if 26 < 27 then (1+1)*(17+9) else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9)

I	if True then (1+1)*(17+9) else f (1+1) (f (1+1) (1+1) ((17+9)+100)) ((17+9)+9)

D	(1+1)*(17+9)

A	2*(17+9)
D	2*26
D	52


-- d)
-- da beide else befehle in der originalen funktion gleich waren werden
-- beide beingungen gleichzeitig abgefragt und nur eine if schleife erzeugt
g a b c = if c >= 21 && c < 27
	then a*c
	else g a (g a a (c+100)) (c+9)
