#!/bin/bash

#echo 31+21

echo "Enter Hex Number:"
read Hex

echo -n "The decimal value of $Hex is : "

echo "obase=10; ibase=16; $Hex" | bc


: '
## 3rd example
n1=4
n2=20

## 2nd example
#echo $(expr $n1 + $n2 )

echo $(expr $n1 + $n2 )
echo $(expr $n1 - $n2 )
echo $(expr $n1 \* $n2 )
echo $(expr $n1 / $n2 )
echo $(expr $n1 % $n2 )'
