-- PRG2 Uebung 2
-- Marvin Glaser
-- 44242114
-- Gruppe 3 Montag (12:00 bis 14:00 Uhr)
-- Martin Parnet


------------------------------------------------------------------------------------------
-- Aufgabe 2b

-- um h' endrekursiv auszufuehren wird eine hilfsfunktion h_help aufgerufen
-- diese besitzt einen stack, der mit jedem rekursiven aufruf erhoeht und
-- bei erfuellen der bedingung x < 10 ausgegeben wird

h' x = h_help x 0 where
        h_help x stack = if x < 10 then stack
        else h_help (x-1) (2*x + stack)

-- Testfaelle:
{- *Main> h' 11
 42
*Main> h' 9
0
*Main> h' 12
66
*Main> h' 0
0
*Main> h' (-12)
0
-}

------------------------------------------------------------------------------------------
-- Aufgabe 3d

-- da beide else befehle in der originalen funktion gleich waren werden
-- beide beingungen gleichzeitig abgefragt und nur eine if schleife erzeugt
g a b c = if c >= 21 && c < 27
        then a*c
        else g a (g a a (c+100)) (c+9)

-- Testfaelle:
{-
*Main> g 1 2 3
21
*Main> g (1+1) 2 17
52
*Main> g 100 100 25
2500
*Main> g 1 1 30
Interrupted.
-}
