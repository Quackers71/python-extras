#!/bin/bash

read -p "Enter the file name which you want to append : " fileName

if [[ -f "$fileName" ]]
then
        echo "The File \"$fileName\" exists"
        read -p "Enter the text you want to append : " fileText
        echo "$fileText" >> $fileName 
        exit 0
else
        echo "The File \"$fileName\" doesn't exist"
fi
