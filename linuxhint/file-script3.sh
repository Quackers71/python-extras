#!/bin/bash

read -p "Enter the file from which you want to read : " fileName

if [[ -f "$fileName" ]]
then
        echo "The File \"$fileName\" exists and reads: "
        while IFS= read -r line
        do
                echo "$line"
        done < $fileName
else
        echo "The File \"$fileName\" doesn't exist"
fi
