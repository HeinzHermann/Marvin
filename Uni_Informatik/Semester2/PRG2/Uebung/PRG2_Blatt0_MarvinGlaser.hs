-- Marvin Glaser
-- 4424114
-- Gruppe 3 Montags 12:00 bis 14:00

-- ==================================================================================================
-- Aufgabe 1

-- checks if bonus can be added to total points
check_bonus rechne rechnen
        | rechne == True && rechnen == True  = True
        | otherwise = False

-- checks if student has passed the exam
check_passed passed bonus punkte
        | punkte >= 50 = True
        | punkte >= 40 && passed == True && bonus >= 10 = True
        | otherwise = False

-- calculates grade of student, based on total points
gradification points
        | points >= 86 = 1.0
        | points >= 82 = 1.3
        | points >= 78 = 1.7
        | points >= 74 = 2.0
        | points >= 70 = 2.3
        | points >= 66 = 2.7
        | points >= 62 = 3.0
        | points >= 58 = 3.3
        | points >= 54 = 3.7
        | points >= 50 = 4.0
        | otherwise = 5.0

-- called function, calls gradification functio with total points
note rechne rechnen bonus punkte
        | check_passed (check_bonus rechne rechnen) bonus punkte == True = gradification (bonus + punkte)
        | otherwise = gradification punkte


-- ==================================================================================================
-- Aufgabe 2 a)

-- function checks if absolute difference between x1/x2 and y1/y2 is constant
-- and therefore diagonal
istZugDiagonal x1 y1 x2 y2 = abs (x1 - x2) == abs (y1 - y2)


-- ==================================================================================================
-- Aufgabe 2 b)

zeigeFeld feld = putStrLn $ unlines [[feld i (5-j) | i <- [1..5]] | j <- [1..4]]

feldA 1 1 = 's'
feldA 1 2 = 's'
feldA 1 3 = 's'
feldA 1 4 = 's'
feldA 5 1 = 'w'
feldA 5 2 = 'w'
feldA 5 3 = 'w'
feldA 5 4 = 'w'
feldA _ _ = ' '


-- inverts given colour
inverseCol string
        | string == 'w' = 's'
        | string == 's' = 'w'
        | otherwise = ' ' 

-- checks if field is out of range and then calls functions to check if field is contested
bedrohtRichtung x y colour direction feld
        | x > 5 || x < 1 || y > 4 || y < 1 = False
        | colour == (feld x y) = False
        | colour == inverseCol (feld x y) = True 
        | (feld x y) == ' ' && direction == 0 = bedrohtRichtung (x - 1) (y + 1) colour direction feld 
        | (feld x y) == ' ' && direction == 1 = bedrohtRichtung (x + 1) (y + 1) colour direction feld 
        | (feld x y) == ' ' && direction == 2 = bedrohtRichtung (x - 1) (y - 1) colour direction feld 
        | (feld x y) == ' ' && direction == 3 = bedrohtRichtung (x + 1) (y - 1) colour direction feld 
        | otherwise = False


-- ==================================================================================================
-- Aufgabe 2 c)

-- checks if given field is contested by any opposing figure on the board
-- to do so, calls function bedrohtRichtung for all four directions
bedroht x y colour feld
        | (bedrohtRichtung x y colour 0 feld) == True = True 
        | (bedrohtRichtung x y colour 1 feld) == True = True 
        | (bedrohtRichtung x y colour 2 feld) == True = True 
        | (bedrohtRichtung x y colour 3 feld) == True = True 
        | otherwise = False


-- ==================================================================================================
-- Aufgabe 2 d)

-- checks if target field is contested by opposing figure
goalSave x2 y2 colour feld
        | (bedroht x2 y2 colour feld) == False = True
        | otherwise = False

 -- compares starting and anding field to determine movement direction
direcFind x1 y1 x2 y2
        | (x1 > x2) == True && (y1 < y2) == True = 0
        | (x1 < x2) == True && (y1 < y2) == True = 1
        | (x1 > x2) == True && (y1 > y2) == True = 2
        | (x1 < x2) == True && (y1 > y2) == True = 3
        | otherwise = 99

-- checks if chosen path is free of figure of same colour (would prevent movement)
-- check for opposing figure not needed, otherwise starting point contested (not possible)
freePath :: Int -> Int -> Int -> Int -> Char -> Int -> (Int -> Int -> Char) -> Bool
freePath x1 y1 x2 y2 colour direction feld
        | x1 == x2 && y1 == y2 = True
        | colour == (feld x1 y1) = False
        | direction == 0 = freePath (x1 - 1) (y1 + 1) x2 y2 colour direction feld
        | direction == 1 = freePath (x1 + 1) (y1 + 1) x2 y2 colour direction feld
        | direction == 2 = freePath (x1 - 1) (y1 - 1) x2 y2 colour direction feld
        | direction == 3 = freePath (x1 + 1) (y1 - 1) x2 y2 colour direction feld
        | otherwise = False

-- checks if move fullfills all conditions to be a allowed
istZugGueltig x1 y1 x2 y2 feld
        | istZugDiagonal x1 y1 x2 y2 == False = False
        | (x1 == x2) == True && (y1 == y2) == True = False
        | (bedroht x1 y1 (feldA x1 y1) feld) == True = False 
        | (goalSave x2 y2 (feldA x1 y1) feld) == False = False
        | (direcFind x1 y1 x2 y2) == 0 = (freePath (x1 - 1) (y1 + 1) x2 y2 (feld x1 y1) 0 feld)
        | (direcFind x1 y1 x2 y2) == 1 = (freePath (x1 + 1) (y1 + 1) x2 y2 (feld x1 y1) 1 feld)
        | (direcFind x1 y1 x2 y2) == 2 = (freePath (x1 - 1) (y1 - 1) x2 y2 (feld x1 y1) 2 feld)
        | (direcFind x1 y1 x2 y2) == 3 = (freePath (x1 + 1) (y1 - 1) x2 y2 (feld x1 y1) 3 feld)
        | otherwise = False


-- ==================================================================================================
-- Aufgabe 2 e)

-- could not figure out how to redifine colours in 'feld' inside of a function

{-
reWrite x1 y1 x2 y2 feld
        | (feld x1 y1) == ' ' = feld
        | otherwise = feld


zieheWennGueltig :: Int -> Int -> Int -> (Int -> Int -> Char) -> (Int -> Int -> Char)
zieheWennGueltig x1 y1 x2 y2 feld
        | (istZugGueltig x1 y1 x2 y2 feld) == True = reWrite x1 y1 x2 y2 feld 
        | otherwise = zeigeFeld feld

-}

-- ==================================================================================================
-- Aufgabe 2 f)

-- helping function, returns True if all figures are in opposing positions to feldA
-- iterates through field and checks for correct coloours
istGeloest :: Int -> Int -> (Int -> Int -> Char) -> Bool
istGeloest x y feld
        | x == 5 && y == 0 = True
        | x == 1 && y == 0 = istGeloest 5 4 feld
        | x == 1 && y >= 1 && (feld x y) == 'w' = istGeloest x (y - 1) feld
        | x == 5 && y >= 1 && (feld x y) == 's' = istGeloest x (y - 1) feld
        | otherwise = False

-- executing function, calls helper function
geloest :: (Int -> Int -> Char) -> Bool
geloest feld
        | (istGeloest 1 4 feld) == True = True
        | otherwise = False
