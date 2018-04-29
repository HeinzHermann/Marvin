-- PRG2 Blatt3
-- Marvin Glaser
-- 44242114
-- Gruppe 3 (Montag 12:00 bis 14:00 Uhr)
-- Martin ....


import Data.Char

------------------------------------------------------------------------------------
-- Aufgabe 1a)

change_to_numbers :: [Char] -> Int
change_to_numbers string = sum (change_help string []) 

change_help :: [Char] -> [Int] -> [Int]
change_help string stack
         | string == [] = stack 
         | (head string) == '0' = change_help (tail string) (stack ++ [0])
         | (head string) == '1' = change_help (tail string) (stack ++ [1])
         | (head string) == '2' = change_help (tail string) (stack ++ [2])
         | (head string) == '3' = change_help (tail string) (stack ++ [3])
         | (head string) == '4' = change_help (tail string) (stack ++ [4])
         | (head string) == '5' = change_help (tail string) (stack ++ [5])
         | (head string) == '6' = change_help (tail string) (stack ++ [6])
         | (head string) == '7' = change_help (tail string) (stack ++ [7])
         | (head string) == '8' = change_help (tail string) (stack ++ [8])
         | (head string) == '9' = change_help (tail string) (stack ++ [9])
         | (head string) == 'a' = change_help (tail string) (stack ++ [1])
         | otherwise = change_help (tail string) (stack ++ [0])

------------------------------------------------------------------------------------
-- Aufgabe 1b)

change_captation string = change_help string [] where
        change_help string stack
                | string == [] = stack
                | (head (reverse (head string))) == '!' = change_help (tail string) (stack ++ (all_caps (head string) []))
                | otherwise = change_help (tail string) (stack ++ (all_lower (head string) []))

all_caps string stack
        | string == [] = [stack]
        | isLower (head string) = all_caps (tail string) (stack ++ [toUpper (head string)])
        | otherwise = all_caps (tail string) (stack ++ [(head string)])

all_lower string stack
        | string == [] = [stack]
        | isUpper (head string) = all_lower (tail string) (stack ++ [toLower (head string)])
        | otherwise = all_lower (tail string) (stack ++ [(head string)])


------------------------------------------------------------------------------------
-- Aufgabe 1c)

merge_lists list = merge_help list [] where
        merge_help list stack
                | list == [] = stack
                | ((length (head list)) >= 4) = merge_help (tail list) (stack ++ (switch_add (head list) [])) 
                | otherwise = merge_help (tail list) stack

switch_add list stack = [head (reverse list)] ++ [head (tail (reverse list))] ++ [head (tail (tail (reverse list)))]


------------------------------------------------------------------------------------
-- Aufgabe 2a)

list_switch :: [Int] -> [Int]
list_switch list = switch_help list [] where
        switch_help list stack
                | list == [] = stack
                | (tail list) == [] = (stack ++ [(head list)])
                | otherwise = switch_help (tail (tail list)) (stack ++ [(head (tail list))] ++ [(head list)])


------------------------------------------------------------------------------------
-- Aufgabe 2b)

list_adder :: [[[Int]]] -> Int
list_adder list = adder_help list [] where
        adder_help :: [[[Int]]] -> [Int] -> Int
        adder_help list stack
                | list == [] = (sum stack)
                | otherwise = adder_help (tail list) (stack ++ (adder_help2 (head list) []))

adder_help2 :: [[Int]] -> [Int] -> [Int]
adder_help2 list2 stack2
        | list2 == [] = stack2
        | otherwise = adder_help2 (tail list2) (stack2 ++ adder_help3 (head list2))

adder_help3 :: [Int] -> [Int]
adder_help3 list3
        | list3 == [] = [0] 
        | otherwise = [(head list3)]


------------------------------------------------------------------------------------
-- Aufgabe 2c)
