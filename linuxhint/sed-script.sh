#!/bin/bash
# need to do further learning on awk :-o

read -p "Enter the Filename to subsitute using sed: " fileName

if [[ -f $fileName ]]
then
        #cat $fileName | sed 's/x/X' # modify 'x' to 'X'
        #sed 's/i/I/g' $fileName # output 'i' to 'I' & g=global
        #sed 's/i/I/g' $fileName > filesed2.txt # output to a file
        #sed -i 's/i/I/g' $fileName # update the file permanently :-o
        sed 's/Linux/UNIX/' $fileName # again, just output

else
        echo "Unfortunately the filename \"$fileName\", doesn't exist!"
fi 
