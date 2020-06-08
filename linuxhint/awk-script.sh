#!/bin/bash
# need to do further learning on awk :-o

read -p "Enter the Filename to search text from: " fileName

if [[ -f $fileName ]]
then
        read -p "Enter the text to search: " grepVar
        test=$( echo -e `grep -i -c $grepVar $fileName`)
        if [ $test != 0 ]
        then
                awk '/$grepVar/ {print NF}' $fileName | tail -n 1
#                read -p "Please enter the column(s) you'd like to display: " awkVar
#                case $awkVar in
                
                DATA=$( echo -e `grep -i -c $grepVar $fileName` )
                echo "There are $DATA matching item's of \"$grepVar\""
#                grep -i -n $grepVar $fileName
        else
                echo "Unfortunately the item \"$grepVar\", doesn't exist!"
                #exit 0
        fi
else
        echo "Unfortunately the filename \"$fileName\", doesn't exist!"
fi 
