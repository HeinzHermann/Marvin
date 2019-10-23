#!/bin/sh;

#echo "Hello, World!";

var1="Hello, World!";
q='"'

echo "var1 is $q${var1}$q";
echo "length of var1 is ${#var1}";

echo "first letter of var1 is ${var1:0:1}";

match1=$(expr index "$var1" "HoW");
match2=$(expr index "$var1" "W");

echo $match1;
echo $match2;

echo "${var1:$match1-1:$match2-2-$match1}";

echo ${var1//"Hello"/"Fuck off"};
