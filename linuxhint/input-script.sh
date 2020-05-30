#!/bin/bash

echo "enter 1st string :"
read st1

echo "enter 2nd string :"
read st2

# Capitalize all chars
echo ${st1^^}

# Capitalize 1st char
echo ${st1^}
echo ${st2^}


## 3rd example
# concatenating both string inputs
: '
c=$st1$st2
echo $c'

## 2nd example
: '
if [ "$st1" \< "$st2" ] 
then
        echo "$st1 is smaller than $st2"
elif [ "$st1" \> "$st2" ]
then
        echo "$st2 is smaller than $st1"
else
        echo "Both strings are equal"
fi'

## 1st example
#if [ "$st1" == "$st2" ] # 1st example
