#!/bin/bash
# need to do further learning on awk :-o

read -p "Enter the Filename to search text to print from awk: " fileName

if [[ -f $fileName ]]
then
        awk '/Linux/ {print $1}' $fileName
else
        echo "Unfortunately the filename \"$fileName\", doesn't exist!"
fi 
